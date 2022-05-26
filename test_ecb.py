from aes_module import AES_ECB


key = 0x000102030405060708090a0b0c0d0e0f
plaintext = 0x00112233445566778899aabbccddeeff
o = AES_ECB(key.to_bytes(16, 'big'))
ciphertext = o.encrypt(plaintext.to_bytes(16, 'big'))
# print(type(ciphertext), ciphertext, len(ciphertext))
# if ciphertext == "69c4e0d86a7b0430d8cdb78070b4c55a":
# 	print("ok")
dec_plaintext = o.decrypt(ciphertext)

if int(dec_plaintext.hex(), 16) == plaintext:
	print("dec_ok")