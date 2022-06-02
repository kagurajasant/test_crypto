from cmac_module import CMAC, SUBK
import unittest

class TestAESCBC(unittest.TestCase):
	def test_SUBK(self):
		expected = ('fbeed618357133667c85e08f7236a8de', 'f7ddac306ae266ccf90bc11ee46d513b')
		
		k = 0x2b7e151628aed2a6abf7158809cf4f3c.to_bytes(16, 'big')
		(K1, K2) = SUBK(k)
		self.assertEqual((hex(K1)[2:], hex(K2)[2:]), expected)
		



	def test_CMAC(self):
		expected = ('070a16b46b4d4144f79bdd9dd04a287c', 'dfa66747de9ae63030ca32611497c827')			
		key = 0x2b7e151628aed2a6abf7158809cf4f3c.to_bytes(16, "big")
		m1 = 0x6bc1bee22e409f96e93d7e117393172a.to_bytes(16, 'big')
		m2 = 0x6bc1bee22e409f96e93d7e117393172aae2d8a571e03ac9c9eb76fac45af8e5130c81c46a35ce411.to_bytes(40, 'big')
		actual = (hex(int(CMAC(key, m1, 128),2))[2:].zfill(32), hex(int(CMAC(key, m2, 128),2))[2:].zfill(32))
		self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()