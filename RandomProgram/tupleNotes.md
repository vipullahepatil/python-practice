list = mutable
set = immutable
dict = mutable
tuple = immutable

tea_type =("Black", "Green", "White", "Oolong", "Herbal")

tea_type[0] = "Black"

tea_type[-1] = "Herbal"

tea_type[1:3] = ("Green", "White")  

tea_type[0]= "Elaichi"

>>> tea_type =("Black", "Green", "White", "Oolong", "Herbal")
>>> tea_type[0]
'Black'
>>> tea_type[0] = "Elaychi"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment

more_tea = ("Chamomile", "Peppermint")

all_tea = tea_type + more_tea
>>> all_tea
('Black', 'Green', 'White', 'Oolong', 'Herbal', 'Chamomile', 'Peppermint')

if "green" in tea_type:
    print("Green tea is available")
else:
    print("Green tea is not available")
Green tea is not available  

>>> tea_list = list(tea_type)
>>> print(tea_list)
['Black', 'Green', 'White', 'Oolong', 'Herbal']
>>> tea_type
('Black', 'Green', 'White', 'Oolong', 'Herbal')

>>> tea_tup = tuple(tea_list)
>>> tea_tup
('Black', 'Green', 'White', 'Oolong', 'Herbal')

tea_list.append("Chamomile")


>>> more_tea_tup = ("black","black","white")
>>> more_tea_tup
('black', 'black', 'white')

more_tea_tup.count("black")
2
>>> 


value assignment by tuple

(black, green, white) = tea_type[0:3]
>>> black
'Black'
>>> green
'Green'
>>> white
'White' 

type(tea_type)
<class 'tuple'>


nested_tuple = (("Black", "Green"), ("White", "Oolong"), ("Herbal",))
>>> nested_tuple
(('Black', 'Green'), ('White', 'Oolong'), ('Herbal',))  
