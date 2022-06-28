#!/usr/bin/env python3
"""! @brief  Documentation for test_crypto, a utility for cross-checking the outputs of 
the cryptographic operations for the Secure Hardware Extenstion (SHE)."""
##
# @mainpage test_crypto
#
# @section description_main Description
# Documentation for test_crypto, a utility for cross-checking the outputs of 
# the cryptographic operations for the Secure Hardware Extenstion (SHE).
# 
# 
##
# @file aes_module.py
#
# @brief The base module for creating an AES object for encryption/decryption in the chosen mode of operation.
#
#
# @section libraries_aes_mod Libraries/Modules
# - cryptography (https://cryptography.io/en/latest/)
#   - Access to the cryptography.hazmat.primitives.ciphers, which gives us the 
# 	AES primitive and modes of operation.
# 
#
# 
#
# @section author_aes_mod Author(s)
# - Created by Satyam Sachan on 06/23/2022.
# - Modified by Satyam Sachan on 06/23/2022.
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes




class AES_ECB:
	'''! The base class for AES-ECB.'''
	def __init__(self, key:bytes): 
		'''! Initialize AES-ECB object with \p key (in bytes). 
		@param[in] key The key to be used. Needs to be 16 bytes long. 
 		@param[out] cipher_enc The encrypting instance initialized with the \p key
		@param[out] cipher_dec The decrypting instance initialized with the \p key
		'''
		## The CipherContext used to encrypt.
		self.cipher_enc = Cipher(algorithms.AES(key), modes.ECB()).encryptor() 
		## The CipherContext used to decrypt.
		self.cipher_dec = Cipher(algorithms.AES(key), modes.ECB()).decryptor()
		# print("blocksize = ", algorithms.AES(key).block_size)

	def encrypt(self, plaintext:bytes):
		'''! Uses \p cipher_enc to encrypt \p plaintext (in bytes) in AES-ECB with \p key as defined in #__init__().
		@param[in] plaintext The bytes to be encrypted
		@param[out] ciphertext The encrypted plaintext
		'''
		ciphertext = self.cipher_enc.update(plaintext) + self.cipher_enc.finalize()

		return ciphertext

	def decrypt(self, ciphertext:bytes):
		'''! Uses \p cipher_dec to decrypt \p ciphertext (in bytes) in AES-ECB with \p key as defined in #__init__().
		@param[in] ciphertext The encrypted plaintext
		@param[out] plaintext The decrypted ciphertext
		'''
		plaintext = self.cipher_dec.update(ciphertext) + self.cipher_dec.finalize()

		return plaintext



class AES_CBC:
	'''! The base class for AES-CBC.'''
	def __init__(self, key:bytes, iv:bytes): 
		'''! Initialize AES-CBC object with \p key and \p iv (in bytes). 
		@param[in] key The key to be used. Needs to be 16 bytes long.
		@param[in] iv The initialization vector used as input to the AES-CBC   
 		@param[out] cipher_enc The encrypting instance initialized with the \p key and \p iv
		@param[out] cipher_dec The decrypting instance initialized with the \p key and \p iv
		'''
		## The CipherContext used to encrypt.
		self.cipher_enc = Cipher(algorithms.AES(key), modes.CBC(iv)).encryptor()
		## The CipherContext used to decrypt.
		self.cipher_dec = Cipher(algorithms.AES(key), modes.CBC(iv)).decryptor()
		# print("blocksize = ", algorithms.AES(key).block_size)

	def encrypt(self, plaintext:bytes):
		'''! Uses \p cipher_enc to encrypt \p plaintext (in bytes) in AES-CBC with \p key and \p iv as defined in #__init__().
		@param[in] plaintext The bytes to be encrypted
		@param[out] ciphertext The encrypted plaintext
		'''
		ciphertext = self.cipher_enc.update(plaintext) + self.cipher_enc.finalize()

		return ciphertext

	def decrypt(self, ciphertext:bytes):
		'''! Uses \p cipher_dec to decrypt \p ciphertext (in bytes) in AES-CBC with \p key and \p iv as defined in #__init__().
		@param[in] ciphertext The encrypted plaintext
		@param[out] plaintext The decrypted ciphertext
		'''
		plaintext = self.cipher_dec.update(ciphertext) + self.cipher_dec.finalize()

		return plaintext



	