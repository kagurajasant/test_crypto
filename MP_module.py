from aes_module import AES_ECB
from math import floor


def Miyaguchi_Preneel(message:bytes, pad:int):
	# print('lmessage',len(message))
	m = bin(int(message.hex(),16))[2:].zfill(len(message)*8)
	#m = bin(int(message.hex(),16))[2:]
	# print('lmessage: {0},,,{1}'.format(len(m), m))
	l = len(m)
	if pad:
		# print("l = {0}, {1}".format(l, bin(l)[2:]))
		k = '0'*((88 - l - 1) % 128)
		# print("k = ",len(k))
		l_pad = bin(l)[2:].zfill(40)
		# print("l_pad=",l_pad)
		m_fin = m + '1' + k + l_pad
	# print("m_fin=",m_fin, len(m_fin))
	else:
		m_fin = m
	out = 0x0.to_bytes(16, "big")
	AES_cipher_object = []
	AES_cipher_object.append(AES_ECB(out))
	for i in range (0, len(m_fin)//128):
		m_block = m_fin[i*128 : (i+1)*128]
		output = AES_cipher_object[i].encrypt(int(m_block,2).to_bytes(16,'big'))
		out = (int(out.hex(), 16) ^ int(output.hex(), 16) ^ int(m_block, 2)).to_bytes(16, 'big')
		AES_cipher_object.append(AES_ECB(out))
	# print(out.hex())

	return out.hex()

		

	

