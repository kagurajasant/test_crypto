from MP_module import Miyaguchi_Preneel
import unittest
# key = 0xdfa66747de9ae63030ca32611497c827.to_bytes(16, "big")
# message = b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe'
# message = 0x6bc1bee22e409f96e93d7e117393172aae2d8a571e03ac9c9eb76fac45af8e51
# Miyaguchi_Preneel(message.to_bytes(32, "big"))

class TestMP(unittest.TestCase):
	def test_MP(self):
		expected = 'c7277a0dc1fb853b5f4d9cbd26be40c6'
		message = 0x6bc1bee22e409f96e93d7e117393172aae2d8a571e03ac9c9eb76fac45af8e51
		actual = Miyaguchi_Preneel(message.to_bytes(32, "big"))
		self.assertEqual(actual, expected)

