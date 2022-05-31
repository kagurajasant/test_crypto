from aes_module import AES_CBC
import unittest

class TestAESCBC(unittest.TestCase):
	def test_CBC_enc_success(self):
		expected =   '7649abac8119b246cee98e9b12e9197d5086cb9b507219ee95db113a917678b273bed6b8e3c1743b7116e69e222295163ff1caa1681fac09120eca307586e1a7'
		
		key = 0x2b7e151628aed2a6abf7158809cf4f3c
		iv = 0x000102030405060708090a0b0c0d0e0f

		plaintext = 0x6bc1bee22e409f96e93d7e117393172aae2d8a571e03ac9c9eb76fac45af8e5130c81c46a35ce411e5fbc1191a0a52eff69f2445df4f9b17ad2b417be66c3710
		
		o = AES_CBC(key.to_bytes(16, 'big'), iv.to_bytes(16, 'big'))
		ciphertext = o.encrypt(plaintext.to_bytes(64, 'big'))
		
		actual = ciphertext.hex()

		self.assertEqual(actual, expected)

	def test_CBC_dec_success(self):
		expected = '6bc1bee22e409f96e93d7e117393172aae2d8a571e03ac9c9eb76fac45af8e5130c81c46a35ce411e5fbc1191a0a52eff69f2445df4f9b17ad2b417be66c3710'
		
		key = 0x2b7e151628aed2a6abf7158809cf4f3c
		iv = 0x000102030405060708090a0b0c0d0e0f

		plaintext = 0x6bc1bee22e409f96e93d7e117393172aae2d8a571e03ac9c9eb76fac45af8e5130c81c46a35ce411e5fbc1191a0a52eff69f2445df4f9b17ad2b417be66c3710
		
		o = AES_CBC(key.to_bytes(16, 'big'), iv.to_bytes(16, 'big'))
		dec_plaintext = o.decrypt(o.encrypt(plaintext.to_bytes(64, 'big')))
		
		actual = dec_plaintext.hex()

		self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()