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