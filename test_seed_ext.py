from MP_module import Miyaguchi_Preneel
import unittest 

class TestSeedExt(unittest.TestCase):
	def test_SeedExt(self):
		ENTROPY = 'ae2d8a571e03ac9c9eb76fac45af8e51'
		PRNG_STATE = '614aae8a7bb8fff31ac3230e6240506b'
		PRNG_EXTENSION_C = '80000000000000000000000000000100'
		PRNG_SEED = '41f21213bca0434b3eb3bafcb0a19d74'

		i = int(PRNG_STATE+ENTROPY+PRNG_EXTENSION_C, 16).to_bytes(48, 'big')
		PRNG_STATE_EXT = Miyaguchi_Preneel(i, 0)
		i = int(PRNG_SEED+ENTROPY+PRNG_EXTENSION_C, 16).to_bytes(48, 'big')
		PRNG_SEED_EXT = Miyaguchi_Preneel(i, 0)

		expected_PRNG_SEED_EXT = '7c92bea252d03015e4f5c2bca69a6f8a'
		expected_PRNG_STATE_EXT = 'cf475ceb98f8ba6be1f55f97fdda9634'

		self.assertEqual((PRNG_SEED_EXT, PRNG_STATE_EXT), (expected_PRNG_SEED_EXT, expected_PRNG_STATE_EXT))

if __name__ == '__main__':
    unittest.main()
