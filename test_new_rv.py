from aes_module import AES_ECB
import unittest

class TestNewRV(unittest.TestCase):
	def test_newRV(self):

		PRNG_STATE = '41f21213bca0434b3eb3bafcb0a19d74'
		PRNG_KEY = 'a1be019264992b2b725a4dd4c7767002'

		o = AES_ECB(int(PRNG_KEY, 16).to_bytes(16, 'big'))

		PRNG_STATE_new = o.encrypt(int(PRNG_STATE, 16).to_bytes(16, 'big'))

		self.assertEqual(PRNG_STATE_new.hex(), '614aae8a7bb8fff31ac3230e6240506b')

if __name__ == '__main__':
    unittest.main() 
