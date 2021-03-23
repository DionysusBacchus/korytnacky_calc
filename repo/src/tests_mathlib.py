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
        self.assertEqual(mathlib.sub(5,1),4)
        self.assertEqual(mathlib.sub(1,5),-4)
        self.assertEqual(mathlib.sub(6,6),0)
        self.assertEqual(mathlib.sub(0,55687),-55687)
        self.assertEqual(mathlib.sub(167,0),167)
    def test_ints_neg(self):
        self.assertEqual(mathlib.sub(-2,-7),5)
        self.assertEqual(mathlib.sub(-7,-2),-5)
        self.assertEqual(mathlib.sub(-4,-4),0)
        self.assertEqual(mathlib.sub(0,-18),18)
        self.assertEqual(mathlib.sub(-42,0),-42)
    def test_ints_mixed(self):
        self.assertEqual(mathlib.sub(-4,6),-10)
        self.assertEqual(mathlib.sub(7,-2),9)
        self.assertEqual(mathlib.sub(0,0),0)
        self.assertEqual(mathlib.sub(1,-179),-180)
        self.assertEqual(mathlib.sub(87,-3),90)
    
    #double inputs
    def test_doubles_pos(self):
        self.assertAlmostEqual(mathlib.sub(0.1,0.1),0,9)
        self.assertAlmostEqual(mathlib.sub(0.00000001,0.1),-0.09999999,9)
        self.assertAlmostEqual(mathlib.sub(1.234,0.234),1,9)
        self.assertAlmostEqual(mathlib.sub(0.234,1.234),-1,9)
    def test_doubles_neg(self):
        self.assertAlmostEqual(mathlib.sub(-0.1,-0.1),0,9)
        self.assertAlmostEqual(mathlib.sub(-40.1,-3.21),-36.89,9)
        self.assertAlmostEqual(mathlib.sub(-80.77,-0.77),-80,9)
        self.assertAlmostEqual(mathlib.sub(-0.77000001,-80.77000001),80,9)
    def test_doubles_mixed(self):
        self.assertAlmostEqual(mathlib.sub(0.1,-0.1),0.2,9)
        self.assertAlmostEqual(mathlib.sub(-0.0001,0.00000001),-0.00010001,9)
        self.assertAlmostEqual(mathlib.sub(449.5,0.001),449.499,9)
        self.assertAlmostEqual(mathlib.sub(-120.876,0.876),-120,9)

class TestDiv(unittest.TestCase):
    pass

#Tests for the mul (*) function
class TestMul(unittest.TestCase):
    #integer inputs
    def test_ints_pos(self):
        self.assertEqual(mathlib.mul(1,9),9)
        self.assertEqual(mathlib.mul(7,1),7)
        self.assertEqual(mathlib.mul(567,0),0)
        self.assertEqual(mathlib.mul(0,985),0)
        self.assertEqual(mathlib.mul(5,9),45)
        self.assertEqual(mathlib.mul(20,80),1600)
    def test_ints_neg(self):
        self.assertEqual(mathlib.mul(-1,-5),5)
        self.assertEqual(mathlib.mul(-16,-1),16)
        self.assertEqual(mathlib.mul(-8,0),0)
        self.assertEqual(mathlib.mul(0,-198765),0)
        self.assertEqual(mathlib.mul(-6,-8),48)
        self.assertEqual(mathlib.mul(-500,-20),10000)
    def test_ints_mixed(self):
        self.assertEqual(mathlib.mul(0,0),0)
        self.assertEqual(mathlib.mul(1,-1),-1)
        self.assertEqual(mathlib.mul(-12,10),-120)
        self.assertEqual(mathlib.mul(-1,30),-30)
        self.assertEqual(mathlib.mul(5,-6),-30)

    #double inputs
    def test_doubles_pos(self):
        self.assertAlmostEqual(mathlib.mul(0.1,0.1),0.01,9)
        self.assertAlmostEqual(mathlib.mul(0.0029,0.0001),0.00000029,9)
        self.assertAlmostEqual(mathlib.mul(1.6,0.1),0.16,9)
        self.assertAlmostEqual(mathlib.mul(1.6,1.6),2.56,9)
    def test_doubles_neg(self):
        self.assertAlmostEqual(mathlib.mul(-0.1,-0.1),0.01,9)
        self.assertAlmostEqual(mathlib.mul(-0.0029,-0.0001),0.00000029,9)
        self.assertAlmostEqual(mathlib.mul(-1.6,-0.1),0.16,9)
        self.assertAlmostEqual(mathlib.mul(-1.6,-1.6),2.56,9)
    def test_doubles_mixed(self):
        self.assertAlmostEqual(mathlib.mul(0.1,-0.1),-0.01,9)
        self.assertAlmostEqual(mathlib.mul(-0.0029,0.0001),-0.00000029,9)
        self.assertAlmostEqual(mathlib.mul(1.6,-0.1),-0.16,9)
        self.assertAlmostEqual(mathlib.mul(-1.6,1.6),-2.56,9)

#Tests for the modulo (|x|) function
class TestModulo(unittest.TestCase):
    #integer inputs
    def test_ints(self):
        self.assertEqual(mathlib.modulo(0),0)
        self.assertEqual(mathlib.modulo(-8),8)
        self.assertEqual(mathlib.modulo(55),55)
    def test_doubles(self):
        self.assertAlmostEqual(mathlib.modulo(1.6),1.6)
        self.assertAlmostEqual(mathlib.modulo(-0.00000001),0.00000001)
        self.assertAlmostEqual(mathlib.modulo(-56.9),56.9)

class TestFactorial(unittest.TestCase):
    pass

class TestPow(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
