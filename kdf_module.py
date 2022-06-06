from MP_module import Miyaguchi_Preneel

def KDF(K:bytes, C:bytes):
	i = bytearray(K) + bytearray(C)
	return Miyaguchi_Preneel(i, 0)