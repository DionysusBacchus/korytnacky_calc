##
#

import mathlib
import unittest

class TestFactorial(unittest.TestCase):

    #factorial is defined for non-negative ints only
    def test_forbidden(self):
        with self.assertRaises(ValueError):
            mathlib.factorial(-4)
        with self.assertRaises(ValueError):
            mathlib.factorial(0.1)
        with self.assertRaises(ValueError):
            mathlib.factorial(-0.68)
    
    def test_unit(self):
        self.assertEqual(mathlib.factorial(1),1)
        self.assertEqual(mathlib.factorial(5),120)
        self.assertEqual(mathlib.factorial(10),3628800)

    def test_through_submit(self):
        res = mathlib.submit('5!')
        self.assertEqual(res,120)
        res = mathlib.submit('0!')
        self.assertEqual(res,1)

#Noncompulsory absotule (|x|) function
class TestAbsolute(unittest.TestCase):
    
    def test_ints(self):
        self.assertEqual(mathlib.absolute(0),0)
        self.assertEqual(mathlib.absolute(-8),8)
        self.assertEqual(mathlib.absolute(55),55)

    def test_doubles(self):
        self.assertAlmostEqual(mathlib.absolute(1.6),1.6,8) #? Proc tady 2 hodnoty s carkou? 
        self.assertAlmostEqual(mathlib.absolute(-0.00000001),0.00000001,8)
        self.assertAlmostEqual(mathlib.absolute(-56.9),56.9,8)
    
    def test_through_submit(self):
        res = mathlib.submit('|-4|')
        self.assertEqual(res,4)
        res = mathlib.submit('|18|')
        self.assertEqual(res,18)
        res = mathlib.submit('|-0.00016574|')
        self.assertAlmostEqual(res,0.00016574,8)
        res = mathlib.submit('|0.74|')
        self.assertAlmostEqual(res,0.74,8)

#Noncompulsory modulo (%) function
class TestModulo(unittest.TestCase):

    def test_forbidden(self):
        with self.assertRaises(ZeroDivisionError):
            mathlib.modulo(8,0)

    def test_pos(self):
        self.assertEqual(mathlib.modulo(5,4),1)
        self.assertEqual(mathlib.modulo(5,5),0)
        self.assertEqual(mathlib.modulo(1,5),1)

    def test_neg(self):
        self.assertEqual(mathlib.modulo(-114,-5),-4)
        self.assertEqual(mathlib.modulo(-14,-7),0)
        self.assertEqual(mathlib.modulo(-7,-10),-7)

    def test_mixed(self):
        self.assertEqual(mathlib.modulo(-114,5),-4)
        self.assertEqual(mathlib.modulo(114,-5),4)
    
    def test_through_submit(self):
        res = mathlib.submit('14%6')
        self.assertEqual(res,2)

class TestSquareRoot(unittest.TestCase):

    def test_forbidden(self):
        with self.assertRaises(ValueError):
            mathlib.nroot(-4)
    
    def test_unit(self):
        self.assertAlmostEqual(math.nroot(5),sqrt(5),8)
        self.assertAlmostEqual(math.nroot(0.25),0.5,8)
        self.assertEqual(mathlib.nroot(4),2)

    def test_through_submit(self):
        res = mathlib.submit('√(16)')
        self.assertEqual(res,4)
        res = mathlib.submit('√(0.00001764)')
        self.assertAlmostEqual(res,0.0042,8)

class TestNRoot(unittest.TestCase):

    def test_forbidden(self):
        with self.assertRaises(ValueError):
            mathlib.nroot(-4,4)
        with self.assertRaises(ValueError):
            mathlib.nroot(4,0)
        with self.assertRaises(ValueError):
            mathlib.nroot(4,0.4)

    def test_unit(self):
        self.assertEqual(mathlib.nroot(4,2),2)
        self.assertEqual(mathlib.nroot(-8,3),-2)
        self.assertAlmostEqual(mathlib.nroot(0.22667121,4),0.69,8)

    def test_through_submit(self):
        res=mathlib.submit('√(-8,3)')
        self.assertEqual(res,-2)
        res = mathlib.submit('√(0.0065536,4)')
        self.assertAlmostEqual(res,0.16,8)

class TestPow(unittest.TestCase):

    #Assigment defined natural exponents
    def test_forbidden(self):
        with self.assertRaises(ValueError):
            mathlib.pow(1,-1)
        with self.assertRaises(ValueError):
            mathlib.pow(2,0.1)
        with self.assertRaises(ValueError):
            mathlib.pow(3,-1.5)
    
    def test_pos_int(self):
        self.assertEqual(mathlib.pow(2,3),8)
        self.assertEqual(mathlib.pow(3,2),9)
        self.assertEqual(mathlib.pow(4,0),1)
    
    def test_neg_int(self):
        self.assertEqual(mathlib.pow(-2,3),-8)
        self.assertEqual(mathlib.pow(-2,2),4)
        self.assertEqual(mathlib.pow(-5,0),1)
    
    def test_pos_double(self):
        self.assertAlmostEqual(mathlib.pow(0.2,3),0.008,8)
        self.assertAlmostEqual(mathlib.pow(0.01,4),float(1e-8),8)
        self.assertAlmostEqual(mathlib.pow(0.2,0),1)

    def test_neg_double(self):
        self.assertAlmostEqual(mathlib.pow(-0.2,3),-0.008,8)
        self.assertAlmostEqual(mathlib.pow(-0.01,4),float(1e-8),8)
        self.assertAlmostEqual(mathlib.pow(-0.2,0),1,8)

    def test_through_submit(self):
        res = mathlib.submit('(-11.1)^2')
        self.assertAlmostEqual(res,123.21,8)
        res = mathlib.submit('(-2.5)^3')
        self.assertAlmostEqual(res,-15.625,8)
        res = mathlib.submit('(2.5)^3')
        self.assertAlmostEqual(res,15.625,8)
        res = mathlib.submit('(-2)^3')
        self.assertEqual(res,-8)
        res = mathlib.submit('(-2)^2')
        self.assertEqual(res,4)
        res = mathlib.submit('(4)^2')
        self.assertEqual(res,16)

class TestSubmitComplex(unittest.TestCase):

    #Each bracket has to have a complementary one
    def test_brackets(self):
        with self.assertRaises(SyntaxError):
            mathlib.submit('(4+5*2')
        with self.assertRaises(SyntaxError):
            mathlib.submit('4+5)*2')
        with self.assertRaises(SyntaxError):
            mathlib.submit('(4+5)*2)')
        with self.assertRaises(SyntaxError):
            mathlib.submit('((4+5)*2')
        with self.assertRaises(SyntaxError):
            mathlib.submit('|4+5)*2)')
        with self.assertRaises(SyntaxError):
            mathlib.submit('|(4+5)|*2|')
    
    def test_basics_int(self):
        res = mathlib.submit('(4+5)*2')
        self.assertEqual(res,18)
        res = mathlib.submit('-8+12/2')
        self.assertEqual(res,-2)
        res = mathlib.submit('8/-4+2')
        self.assertEqual(res,0)
        res = mathlib.submit('8/(-4+2)')
        self.assertEqual(res,-4)
        res = mathlib.submit('-1*5-15')
        self.assertEqual(res,-20)
    
    def test_pro_int(self):
        res = mathlib.submit('2!+5*√(-8,3)')
        self.assertEqual(res,-8)
        res = mathlib.submit('(-4)^2/1!')
        self.assertEqual(res,16)
    
    def test_basics_double(self):
        res = mathlib.submit('(4.091+0.009)*1.5')
        self.assertAlmostEqual(res,6.15,8)
        res = mathlib.submit('14.2/2-7.1')
        self.assertAlmostEqual(res,0,8)
        res = mathlib.submit('-8.16*4/3+9')
        self.assertAlmostEqual(res,-1.88,8)
        res = mathlib.submit('-8.16+4/(3+1)')
        self.assertAlmostEqual(res,-7.16,8)

    def test_pro_double(self):
        res = mathlib.submit('(4.091+0.009)^2-1.5*4')
        self.assertAlmostEqual(res,10.81,8)
        res = mathlib.submit('(4.091+0.009)^2-√(1.44)*5+0.12345678')
        self.assertAlmostEqual(res,10.933456789,8)

    def test_forbidden(self):
        with self.assertRaises(ZeroDivisionError):
            mathlib.submit('12/0')
        with self.assertRaises(ZeroDivisionError):
            mathlib.submit('1.15/0')
        with self.assertRaises(ValueError):
            mathlib.submit('(14-28)!')
        with self.assertRaises(ValueError):
            mathlib.submit('(0.18724)!')
        with self.assertRaises(ValueError):
            mathlib.submit('√(10-28)')
        with self.assertRaises(ValueError):
            mathlib.submit('√(0.5-28)')
        with self.assertRaises(ValueError):
            mathlib.submit('√(10-28,6)')
        with self.assertRaises(ValueError):
            mathlib.submit('(10-28,6)^-4') #negative power is forbiden
        with self.assertRaises(ValueError):
            mathlib.submit('(10-28,6)^0.5') #rational power is forbiden


if __name__ == '__main__':
    unittest.main()


