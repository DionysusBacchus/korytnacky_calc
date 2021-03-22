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
    
#Tests for the sub (-) function
class TestSub(unittest.TestCase):
    #integer inputs
    def test_ints_pos(self):
        self.assertEqual(mathlib.add(5,1),4)
        self.assertEqual(mathlib.add(1,5),-4)
        self.assertEqual(mathlib.add(6,6),0)
        self.assertEqual(mathlib.add(0,55687),-55687)
        self.assertEqual(mathlib.add(167,0),167)
    def test_ints_neg(self):
        self.assertEqual(mathlib.add(-2,-7),5)
        self.assertEqual(mathlib.add(-7,-2),-5)
        self.assertEqual(mathlib.add(-4,-4),0)
        self.assertEqual(mathlib.add(0,-18),18)
        self.assertEqual(mathlib.add(-42,0),-42)
    def test_ints_mixed(self):
        self.assertEqual(mathlib.add(-4,6),-10)
        self.assertEqual(mathlib.add(7,-2),9)
        self.assertEqual(mathlib.add(0,0),0))
        self.assertEqual(mathlib.add(1,-179),-180)
        self.assertEqual(mathlib.add(87,-3),90)
    
    #double inputs
    def test_doubles_pos(self):
        self.assertAlmostEqual(mathlib.add(0.1,0.1),0,9)
        self.assertAlmostEqual(mathlib.add(0.00000001,0.1),-0.09999999,9)
        self.assertAlmostEqual(mathlib.add(1.234,0.234),1,9)
        self.assertAlmostEqual(mathlib.add(0.234,1.234),-1,9)
    def test_doubles_neg(self):
        self.assertAlmostEqual(mathlib.add(-0.1,-0.1),0,9)
        self.assertAlmostEqual(mathlib.add(-40.1,-3.21),-36.89,9)
        self.assertAlmostEqual(mathlib.add(-80.77,-0.77),-80,9)
        self.assertAlmostEqual(mathlib.add(-0.77000001,-80.77000001),80,9)
    def test_doubles_mixed(self):
        self.assertAlmostEqual(mathlib.add(0.1,-0.1),0.2,9)
        self.assertAlmostEqual(mathlib.add(-0.0001,0.00000001),-0.00010001,9)
        self.assertAlmostEqual(mathlib.add(449.5,0.001),449.499,9)
        self.assertAlmostEqual(mathlib.add(-120.876,0.876),-120,9)

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
