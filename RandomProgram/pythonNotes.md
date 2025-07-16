

Pythons Notes

Data types types
1 Mutable / 2 Immutable

1 Mutable
List
Set
Dictionary
Bytearray
array


2. Immutable
Integers
Floating-points number
Boolean
Strings
Tuples
Frozer Set
Bytes

Number: 1234 , 3.14 , 3+4j ,0b11,Decimal(),
        Fraction()
String : 'spam' , "Bob's",b'a\x01c', u'sp\xc4m'

List : [1,[2,'three'],4.5] , List(range(10))

Tuple : (1,'spam',4,'U'), tuple('spam'),namedtuple

Dictionary : {'foof':'span'}  , dict

Set : set('abc') , {'a','b','c'}

File : open('abc.txt'),open(r'C:\hsm.bin','wb')

Boolean : True , False
None : None
Bytes : b'spam', bytes(range(10))
Bytearray : bytearray(b'spam'), bytearray(range(10))
Array : array.array('i', [1, 2, 3, 4])
Complex : 3+4j , complex(3,4)
Decimal : Decimal('3.14'), Decimal(3.14)
Fraction : Fraction(3, 4), Fraction('3/4')

Function : def spam(): pass , lambda x: x+1
Module : import math , from math import sqrt
Class : class Spam: pass , type('Spam', (), {})     

Advanced types
Decorator : @staticmethod, @classmethod, @property
Generator : (x*x for x in range(10)), yield from
Iterator : iter([1, 2, 3]), next(iter([1, 2, 3]))
MetaProgramming : type, isinstance, issubclass
ContextManager : with open('file.txt') as f: pass



m == n check value ref
m is n check memory ref
means both objects are same as value but not same as memory ref