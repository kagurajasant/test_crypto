from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding



class AES_ECB:
	def __init__(self, key):
		cipher_enc = Cipher(algorithms.AES(key), modes.ECB()).encryptor()
		cipher_dec = Cipher(algorithms.AES(key), modes.ECB()).decryptor()
		padder = padding.PKCS7(algorithms.AES(key).block_size).padder()

	def aes_ecb_encrypt(self, plaintext):
		