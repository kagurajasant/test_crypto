import re
from aes_module import AES_ECB

def left_shift_128(i:int):
	return (i << 1) & 0xffffffffffffffffffffffffffffffff

def SUBK(k:bytes):
	aes_cipher_object = AES_ECB(k)
	L = aes_cipher_object.encrypt(0x0.to_bytes(16, 'big'))
	#print(bin(int(L.hex(), 16)))
	print(L.hex())	
	if(int(L.hex(), 16) >> 127 == 0):
		K1 = left_shift_128(int(L.hex(), 16))
	else:
		K1 = (left_shift_128(int(L.hex(), 16))) ^ 135
	
	print('K1 : {0}'.format(hex(K1)[2:]))

	if(K1 >> 127 == 0):
		K2 = left_shift_128(K1)
	else:
		K2 = left_shift_128(K1) ^ 135
	
	print('K2 : {0}'.format(hex(K2)[2:]))

	return K1, K2

def CMAC(k:bytes, m:bytes, tlen:int):
	K1, K2 = SUBK(k)
	b = 128
	mlen = len(bin(int(m.hex(),16))[2:].zfill(len(m)*8))
	# print('m_len:', mlen)
	m_bit = bin(int(m.hex(),16))[2:].zfill(len(m)*8)
	# print('m_bit:', m_bit)
	if int(m.hex(), 16) == 0:
		n = 1
	else:
		n = -1 * (-mlen//b)

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

	ret_val = bin(int.from_bytes(prev_out, "big"))[2:tlen+2]
	return ret_val
	# print('prevout:',prev_out.hex())