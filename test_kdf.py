from kdf_module import KDF
import unittest

class TestKDF(unittest.TestCase):
	def test_KDF(self):
		expected = '118a46447a770d87828a69c222e2d17e'
		K = '000102030405060708090a0b0c0d0e0f'
		C = '010153484500800000000000000000b0'
		i = int(K+C,16).to_bytes(32, 'big')
		actual = KDF(int(K, 16).to_bytes(16, 'big'), int(C, 16).to_bytes(16, 'big'))
		self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()

