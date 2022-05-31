from aes_module import AES_ECB
import unittest

class TestAESECB(unittest.TestCase):
	def test_ECB_enc_success(self):
		expected = '69c4e0d86a7b0430d8cdb78070b4c55a'
		
		key = 0x000102030405060708090a0b0c0d0e0f
		plaintext = 0x00112233445566778899aabbccddeeff
		
		o = AES_ECB(key.to_bytes(16, 'big'))
		ciphertext = o.encrypt(plaintext.to_bytes(16, 'big'))
		
		actual = ciphertext.hex()

		self.assertEqual(actual, expected)

	def test_ECB_dec_success(self):
		expected = '00112233445566778899aabbccddeeff'
		
		key = 0x000102030405060708090a0b0c0d0e0f
		plaintext = 0x00112233445566778899aabbccddeeff
		
		o = AES_ECB(key.to_bytes(16, 'big'))
		dec_plaintext = o.decrypt(o.encrypt(plaintext.to_bytes(16, 'big')))
		
		actual = dec_plaintext.hex()

		self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()