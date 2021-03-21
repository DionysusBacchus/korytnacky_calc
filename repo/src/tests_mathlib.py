##
#

import unittest
import mathlib

#Tests for the add (+) function 
class TestAdd(unittest.TestCase):

    #integer inputs
    def test_ints_pos(self):
        self.assertEqual(mathlib.add(4,5),9)
        self.assertEqual(mathlib.add(189,561),750)
        self.assertEqual(mathlib.add(1000000,0),1000000)
    def test_ints_neg(self):
        self.assertEqual(mathlib.add(-8,-7),-15)
        self.assertEqual(mathlib.add(-89,-61),-150)
        self.assertEqual(mathlib.add(0,-400),-400)
    def test_ints_mixed(self):
        self.assertEqual(mathlib.add(0,0),0)
        self.assertEqual(mathlib.add(-1,6),5)
        self.assertEqual(mathlib.add(70,-8),62)
        self.assertEqual(mathlib.add(-155,5),-150)

    #double inputs
    def test_doubles_pos(self):
        self.assertAlmostEqual(mathlib.add(0.1,0.05),0.15,9)
        self.assertAlmostEqual(mathlib.add(12.34567,0.0000089),12.3456789,9)
        self.assertAlmostEqual(mathlib.add(1.5,2.5),4,9)
        self.assertAlmostEqual(mathlib.add(1000.9,0.2),1001.1,9)
    def test_doubles_neg(self):
        self.assertAlmostEqual(mathlib.add(-0.1,-0.8),-0.9,9)
        self.assertAlmostEqual(mathlib.add(-98.1,-1.9),-100,9)
        self.assertAlmostEqual(mathlib.add(-0.0006,-0.00000007),-0.00060007,9)
        self.assertEqual(mathlib.add(-15.3,-18.8),-34.1,9)
    def test_doubles_mixed(self):
        self.assertAlmostEqual(mathlib.add(0.1,-0.1),0,9)
        self.assertAlmostEqual(mathlib.add(-5.55,5.00000000),-0.55,9)
        self.assertAlmostEqual(mathlib.add(-12.43,0.43),-12,9)
        self.assertAlmostEqual(mathlib.add(4.3, -2.009),2.291,9)
    

class TestSub(unittest.TestCase):
    pass

class TestDiv(unittest.TestCase):
    pass

class TestMul(unittest.TestCase):
    pass

class TestModulo(unittest.TestCase):
    pass

class TestFactorial(unittest.TestCase):
    pass

class TestPow(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
