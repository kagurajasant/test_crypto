##
# @file cmac_module.py
#
# @brief The base module for calculating a CMAC.
#
#
# @section libraries_cmac_mod Libraries/Modules
# - aes_module.py for AES_ECB
# @section references_cmac_mod References
# - NIST Special Publication 800-38B (https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-38b.pdf)
# @section author_cmac_mod Author(s)
# - Created by Satyam Sachan on 06/23/2022.
# - Modified by Satyam Sachan on 06/23/2022.
from aes_module import AES_ECB

def left_shift_128(i:int): #left shift and consider the 128 LSBs
	'''! Defined in the referenced standard. This function left shifts \p i by 1 and discards the MSB.'''
	return (i << 1) & 0xffffffffffffffffffffffffffffffff

def SUBK(k:bytes):
	'''! Subkey generation, as in the referenced standard. Derives two keys \p K1 and \p K2 from the input key \p k.
		@param[in] k The key to be used. Needs to be 16 bytes long. 
 		@param[out] K1 Subkey #1, used to derive K2 in #SUBK() and in #CMAC() for messages if the message length is a multiple of AES's blocksize (128 bits).
		@param[out] K2 Subkey #2, used in #CMAC for messages if the message length is not a multiple of AES's blocksize (128 bits).
	'''
	aes_cipher_object = AES_ECB(k)
	L = aes_cipher_object.encrypt(0x0.to_bytes(16, 'big')) #encrypt 128 bit 0 string with key k
	# print(bin(int(L.hex(), 16)))
	# print(L.hex())	
	if(int(L.hex(), 16) >> 127 == 0): #if MSB == 0
		K1 = left_shift_128(int(L.hex(), 16))
	else:
		K1 = (left_shift_128(int(L.hex(), 16))) ^ 135
	
	# print('K1 : {0}'.format(hex(K1)[2:]))

	if(K1 >> 127 == 0):
		K2 = left_shift_128(K1)
	else:
		K2 = left_shift_128(K1) ^ 135
	
	# print('K2 : {0}'.format(hex(K2)[2:]))

	return K1, K2

def CMAC(k:bytes, m:bytes, tlen:int):
	'''! CMAC routine, as in the referenced standard. Uses #SUBK() for subkey generation.
		@param[in] k The key to be used. Needs to be 16 bytes long. 
		@param[in] m The message to be CMACd. Needs to be in bytes.
		@param[in] tlen Tag length in bits. Can be up to 128 bits.
 		@param[out] ret_val Tag value in bits (type string).
	'''
	K1, K2 = SUBK(k)
	b = 128
	mlen = len(bin(int(m.hex(),16))[2:].zfill(len(m)*8))
	# print('m_len:', mlen)
	m_bit = bin(int(m.hex(),16))[2:].zfill(len(m)*8)
	# print('m_bit:', m_bit)
	if int(m.hex(), 16) == 0:
		n = 1
	else:
		n = -1 * (-mlen//b) #ceil(mlen/b)

	if mlen %128 != 0:
		m_bit += '1' + '0'*(128 - (mlen+1)%128)
		m_final = bin(int(m_bit,2) ^ K2)[2:].zfill(len(m_bit))
		# print('m_final:{0}, len:{1}'.format(m_final, len(m_bit)))

	else:
		m_final = bin(int(m_bit,2) ^ K1)[2:].zfill(len(m_bit))

	# print('final_len:',len(m_final), type(K1))
	prev_out = b'\x00'

	for i in range (0, len(m_final)//128):
		AES_cipher_object = AES_ECB(k)
		m_block = m_final[i*128 : (i+1)*128]
		# print('m_block=', m_block)
		ciphertext = AES_cipher_object.encrypt((int(m_block,2)^int(prev_out.hex(),16)).to_bytes(16,'big'))
		prev_out = ciphertext

	if tlen < 128:
		ret_val = (bin(int.from_bytes(prev_out, "big"))[2:].zfill(128))[:tlen]
	else:
		ret_val = (bin(int.from_bytes(prev_out, "big"))[2:].zfill(128))
	return ret_val
	# print('prevout:',prev_out.hex())