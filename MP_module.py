from aes_module import AES_ECB
from math import floor


def Miyaguchi_Preneel(key:bytes, message:bytes):
	m = bin(int(message.hex(),16))[2:]
	l = len(m)
	print("l = ", bin(l)[2:])
	if l % 128 != 0:
		k = '0'*((88 - l - 1) % 128)
		print("k = ",len(k))
		n = bin(l).zfill(40)
		print("n=",n)
	

