import unittest

class UnitTest(unittest.TestCase):

  def setUp(self):
    self.base_url = '5.253.25.209'

  def test_upper(self):
    self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
  unittest.main()