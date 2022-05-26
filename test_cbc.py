from aes_module import AES_CBC


key = 0x2b7e151628aed2a6abf7158809cf4f3c
# plaintext = 0x6bc1bee22e409f96e93d7e117393172a
plaintext = bytes.fromhex("6bc1bee22e409f96e93d7e117393172aae2d8a571e03ac9c9eb76fac45af8e5130c81c46a35ce411e5fbc1191a0a52eff69f2445df4f9b17ad2b417be66c3710")
iv = 0x000102030405060708090a0b0c0d0e0f
o = AES_CBC(key.to_bytes(16, 'big'), iv.to_bytes(16, 'big'))
ciphertext = o.encrypt(plaintext)
print("ciphertext = {}".format(ciphertext.hex()))
dec_plaintext = o.decrypt(ciphertext)

if dec_plaintext == plaintext:
	print("dec_ok")