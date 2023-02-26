import unittest

from singelton import Borg, Singelton

class TestSingelton(unittest.TestCase):
	def test_two_singeltons_have_different_identity(self):
		x = Singelton(HTTP="Hyper Text Transfer Protocol")
		y = Singelton(SNMP="Simple Network Management Protocol")
		self.assertIsNot(x, y)

	def test_two_singeltons_share_common_state(self):
		x = Singelton(HTTP="Hyper Text Transfer Protocol")
		y = Singelton(SNMP="Simple Network Management Protocol")
		self.assertEqual(str(x), str(y))

if __name__ == "__main__":
	unittest.main()
