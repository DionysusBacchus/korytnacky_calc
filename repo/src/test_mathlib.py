##
#

import mathlib
mathlib.set_set_expr(lambda x : x == 2)

import unittest

class TestFactorial(unittest.TestCase):

    #factorial is defined for non-negative ints only
    def test_forbidden(self):
        res = mathlib.submit('-4!')
        self.assertEqual(res,'Neplatný vstup')
        res = mathlib.submit('(-4)!')
        self.assertEqual(res,'Neplatný vstup')
        res = mathlib.submit('0.1!')
        self.assertEqual(res,'Neplatný vstup')
        res = mathlib.submit('-0.68!')
        self.assertEqual(res,'Neplatný vstup')
    
    def test_unit(self):
        res = mathlib.submit('1!')
        self.assertEqual(res,1)
        res = mathlib.submit('5!')
        self.assertEqual(res,120)
        res = mathlib.submit('-(5!)')
        self.assertEqual(res,-120)
        res = mathlib.submit('10!')
        self.assertEqual(res,3628800)

#Noncompulsory natural logarithm function
class TestLog(unittest.TestCase):
    def test_props(self):
        res = mathlib.submit('ln(1)')
        self.assertEqual(res,0)
        res = mathlib.submit('ln(e)')
        self.assertEqual(res,1)
        xy = mathlib.submit('ln(15)')
        x = mathlib.submit('ln(3)')
        y = mathlib.submit('ln(5)')
        self.assertEqual(xy,x+y)
        x = mathlib.submit('ln(3^(2))')
        y = mathlib.submit('2*ln(3)')
        self.assertEqual(x,y)

    def test_forbidden(self):
        res = mathlib.submit('ln(-1)')
        self.assertEqual(res,'Neplatný vstup')
        res = mathlib.submit('ln(0)')
        self.assertEqual(res,'Neplatný vstup')

#Noncompulsory absotule (|x|) function
class TestAbsolute(unittest.TestCase):
    
    def test_ints(self):
        res = mathlib.submit('|0|')
        self.assertEqual(res,0)
        res = mathlib.submit('|-8|')
        self.assertEqual(res,8)
        res = mathlib.submit('|55|')
        self.assertEqual(res,55)

    def test_doubles(self):
        res = mathlib.submit('|1.6|')
        self.assertAlmostEqual(res,1.6,8)
        res = mathlib.submit('|-0.00000001|')
        self.assertAlmostEqual(res,0.00000001,8)
        res = mathlib.submit('|-56.9|')
        self.assertAlmostEqual(res,56.9,8)

#Noncompulsory modulo (%) function
class TestModulo(unittest.TestCase):

    def test_forbidden(self):
        res = mathlib.submit('4%0')
        self.assertEqual(res,'Nulou se nedá dělit')

    def test_pos(self):
        res = mathlib.submit('5%4')
        self.assertEqual(res,1)
        res = mathlib.submit('5%5')
        self.assertEqual(res,0)
        res = mathlib.submit('1%5')
        self.assertEqual(res,1)

    def test_neg(self):
        res = mathlib.submit('-114%-5')
        self.assertEqual(res,-4)
        res = mathlib.submit('-14%7')
        self.assertEqual(res,0)
        res = mathlib.submit('-7%-10')
        self.assertEqual(res,-7)

    def test_mixed(self):
        res = mathlib.submit('-114%5')
        self.assertEqual(res,1)
        res = mathlib.submit('114%-5')
        self.assertEqual(res,-1) 

class TestSquareRoot(unittest.TestCase):

    def test_forbidden(self):
        with self.assertRaises(ValueError):
            mathlib.sqrt(-4)
    
    def test_unit(self):
        self.assertAlmostEqual(mathlib.sqrt(5),2.23606798,8)
        self.assertAlmostEqual(mathlib.sqrt(0.25),0.5,8)
        self.assertEqual(mathlib.sqrt(4),2)

    def test_through_submit(self):
        res = mathlib.submit('√(16)')
        self.assertEqual(res,4)
        res = mathlib.submit('√(0.00001764)')
        self.assertAlmostEqual(res,0.0042,8)

class TestNRoot(unittest.TestCase):

    def test_forbidden(self):
        res = mathlib.submit('√(-4,4)')
        self.assertEqual(res,'Neplatný vstup')
        res = mathlib.submit('√(4,0)')
        self.assertEqual(res,'Neplatný vstup')
        res = mathlib.submit('√(4,0.4)')
        self.assertEqual(res,'Neplatný vstup')

    def test_unit(self):
        res = mathlib.submit('√(4,2)')
        self.assertEqual(res,2)
        res = mathlib.submit('√(-8,3)')
        self.assertEqual(res,-2)
        res = mathlib.submit('√(0.22667121,4)')
        self.assertAlmostEqual(res,0.69,8)
        res = mathlib.submit('√(-0.32768,5)')
        self.assertAlmostEqual(res,-0.8,8)
        
class TestPow(unittest.TestCase):

    def test_pos_int(self):
        res = mathlib.submit('2^3')
        self.assertEqual(res,8)
        res = mathlib.submit('3^2')
        self.assertEqual(res,9)
        res = mathlib.submit('4^0')
        self.assertEqual(res,1)
    
    def test_neg_int(self):
        res = mathlib.submit('(-2)^3')
        self.assertEqual(res,-8)
        res = mathlib.submit('(-2)^2')
        self.assertEqual(res,4)
        res = mathlib.submit('(-5)^0')
        self.assertEqual(res,1)
    
    def test_pos_double(self):
        res = mathlib.submit('0.2^3')
        self.assertAlmostEqual(res,0.008,8)
        res = mathlib.submit('0.01^4')
        self.assertAlmostEqual(res,float(1e-8),8)
        res = mathlib.submit('0.2^0')
        self.assertAlmostEqual(res,1)

    def test_neg_double(self):
        res = mathlib.submit('(-0.2)^3')
        self.assertAlmostEqual(res,-0.008,8)
        res = mathlib.submit('(-0.01)^4')
        self.assertAlmostEqual(res,float(1e-8),8)
        res = mathlib.submit('(-0.2)^0')
        self.assertAlmostEqual(res,1,8)

class TestSubmitComplex(unittest.TestCase):

    #Each bracket has to have a complementary one
    def test_brackets(self):
        res = mathlib.submit('(4+5*2')
        self.assertEqual(res,'Chyba syntaxe')
        res = mathlib.submit('4+5)*2')
        self.assertEqual(res,'Chyba syntaxe')
        res = mathlib.submit('(4+5)*2)')
        self.assertEqual(res,'Chyba syntaxe')
        res = mathlib.submit('((4+5)*2')
        self.assertEqual(res,'Chyba syntaxe')
        res = mathlib.submit('|4+5)*2)')
        self.assertEqual(res,'Chyba syntaxe')
        res = mathlib.submit('|(4+5)|*2|')
        self.assertEqual(res,'Chyba syntaxe')
        res = mathlib.submit('ln(9')
        self.assertEqual(res,'Chyba syntaxe')
        res = mathlib.submit('ln8)')
        self.assertEqual(res,'Chyba syntaxe')
    
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
        self.assertAlmostEqual(res,10.93345678,8)

    def test_forbidden(self):
        res = mathlib.submit('12/0')
        self.assertEqual(res,'Nulou se nedá dělit')
        res = mathlib.submit('1.15/0')
        self.assertEqual(res,'Nulou se nedá dělit')
        res = mathlib.submit('(14-28)!')
        self.assertEqual(res,'Neplatný vstup')
        res = mathlib.submit('(0.18724)!')
        self.assertEqual(res,'Neplatný vstup')
        res = mathlib.submit('√(10-28)')
        self.assertEqual(res,'Neplatný vstup')
        res = mathlib.submit('√(0.5-28)')
        self.assertEqual(res,'Neplatný vstup')
        res = mathlib.submit('√(10-28,6)')
        self.assertEqual(res,'Neplatný vstup')

if __name__ == '__main__':
    unittest.main()


