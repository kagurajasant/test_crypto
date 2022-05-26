from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding



class AES_ECB:
	def __init__(self, key):
		self.cipher_enc = Cipher(algorithms.AES(key), modes.ECB()).encryptor()
		self.cipher_dec = Cipher(algorithms.AES(key), modes.ECB()).decryptor()
		print("blocksize = ", algorithms.AES(key).block_size)

	def encrypt(self, plaintext):
		# padded_data = self.padder.update(plaintext) + self.padder.finalize()
		ciphertext = self.cipher_enc.update(plaintext) + self.cipher_enc.finalize()

		return ciphertext

	def decrypt(self, ciphertext):
		plaintext = self.cipher_dec.update(ciphertext) + self.cipher_dec.finalize()

		return plaintext


class AES_CBC:
	def __init__(self, key, iv):
		self.cipher_enc = Cipher(algorithms.AES(key), modes.CBC(iv)).encryptor()
		self.cipher_dec = Cipher(algorithms.AES(key), modes.CBC(iv)).decryptor()
		print("blocksize = ", algorithms.AES(key).block_size)

	def encrypt(self, plaintext):
		ciphertext = self.cipher_enc.update(plaintext) + self.cipher_enc.finalize()

		return ciphertext

	def decrypt(self, ciphertext):
		plaintext = self.cipher_dec.update(ciphertext) + self.cipher_dec.finalize()

		return plaintext

