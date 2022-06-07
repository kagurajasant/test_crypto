from kdf_module import KDF
from aes_module import AES_ECB
import unittest

class TestPRNG(unittest.TestCase):
	def test_PRNG(self):
		SECRET_KEY = '2b7e151628aed2a6abf7158809cf4f3c'
		PRNG_SEED_KEY_C = '010553484500800000000000000000B0'
		expected_PRNG_SEED_KEY = '8abc8f6e2a8264fd38088be622ca0416'
		PRNG_SEED_KEY = KDF(int(SECRET_KEY,16).to_bytes(16, 'big'), int(PRNG_SEED_KEY_C,16).to_bytes(16, 'big'))

		self.assertEqual(expected_PRNG_SEED_KEY, PRNG_SEED_KEY)
		
		PRNG_SEED = '6bc1bee22e409f96e93d7e117393172a'

		o = AES_ECB(int(PRNG_SEED_KEY,16).to_bytes(16, 'big'))

		PRNG_SEED_new = o.encrypt(int(PRNG_SEED, 16).to_bytes(16, 'big'))

		# print(PRNG_SEED_new.hex())

		self.assertEqual(PRNG_SEED_new.hex(), '41f21213bca0434b3eb3bafcb0a19d74')

		# PRNG_SEEDi = ENCECB,PRNG_SEED_KEY(PRNG_SEEDi-1)

if __name__ == '__main__':
    unittest.main()
