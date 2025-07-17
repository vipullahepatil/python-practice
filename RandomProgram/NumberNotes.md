>>> "chai" *3
'chaichaichai'

>>> "chai" + "code"
'chaicode'

>>> x,y,z
(2, 3, 4)

multiple assignment
get result in tuple

>>> x + 1, y*2
(3, 6)

can do multiple assignment in expression in single line


repr('spam')
'\'spam\''
>>> str('spam')
'spam'
print('spam')
spam


x < y <z
>>> x < y and y < z
True


1 == 2 < 3
False

1 ==2 and 2 < 3
False and True
False

import math

math.floor(3.14)
3
math.floor(3.99)
3
math.floor(-3.14)
-4
math.floor(-3.99)
-4

floor always gives the largest integer less than or equal to the number

math.trunc(3.14)
3
math.trunc(3.99)
3
math.trunc(-3.14)
-3
math.trunc(-3.99)
-3

trunc always gives the integer part of the number, removing the decimal part


0.1 + 0.1 +0.1 - 0.3
5.551115123125783e-17

from decimal import Decimal
Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
Decimal('0.0')  

set = {1, 2, 3}
intersection 
set & {2, 3, 4}
{2, 3}  
union
set | {2, 3, 4}
{1, 2, 3, 4}

 
 catch 
>>> setone = {1,2,3}
>>> setone - {1,2,3}
set()
it didnt return {} cause {} is empty dictionary not empty set

to write empty set use set() not {}


True + 4
5
