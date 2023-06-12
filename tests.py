import unittest

import utils
from main import run


class TestValues(unittest.TestCase):
    
    def test_check_chars_bad0(self):
        with self.assertRaises(ValueError):
            utils.check_chars('LXCyX')

    def test_check_chars_bad1(self):
        with self.assertRaises(ValueError):
            utils.check_chars('LXCZM')

    def test_check_chars_ok(self):
        self.assertIsInstance(utils.check_chars('LXCX'), list)
            
    def test_run_ok0(self):
        self.assertEqual(run('CII'), 102)

    def test_run_ok1(self):
        self.assertEqual(run('XIX'), 19)

    def test_run_ok2(self):
        self.assertEqual(run('CMXCIX'), 999)
    
    def test_run_ok3(self):
        self.assertEqual(run('MCCXXXIV'), 1234)

if __name__ == '__main__':
    unittest.main()