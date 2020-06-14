import requests
import unittest

r=requests.get('http://www.tut.by')
class TestStringMethods(unittest.TestCase):
	def test_tut_by(self):
		self.assertTrue(r.status_code == 200)
		self.assertFalse(r.status_code ==404)
	def test_tut_by(self):
		self.assertTrue(r.encoding == 'utf-8')
	def test_tut_by(self):
		self.assertTrue(r.text != 0)	





#r = requests.get('http://www.tut.by')
#if r.status_code == 200:
#    print('al1 ok')
#	print("it's a trap")


if __name__ == '__main__':
    unittest.main()
