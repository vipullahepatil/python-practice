chai ="Masala Chai"

slice_chai = chai[0:6]  
print(slice_chai)  # Output: Masala


num_list = "0123456789"
slice_num_list = num_list[0:6]
print(slice_num_list)  # Output: 012345

slice_num_list = num_list[0:6:2]
print(slice_num_list)  # Output: 024

slice_num_list = num_list[::2]
print(slice_num_list)  # Output: 02468  

slice_num_list = num_list[::-1]
print(slice_num_list)  # Output: 9876543210

slice_num_list = num_list[:7]
print(slice_num_list)  # Output: 0123456

slice_num_list = num_list[7:]
print(slice_num_list)  # Output: 789


>>> chai = "absda"
>>> aa = chai.replace("a","v")
>>> aa
'vbsdv'

chai ="Masala Chai"
>>> chai.find("Chai")
7
>>> chai.find("chai")
-1
>>> chai.find("a")
1
>>> 

>>> chai_type ="Masala"
>>> quantity = 2
>>> order = "i ordered {} cups of {} chai"
>>> order
'i ordered {} cups of {} chai'
>>> order.format(quantity,chai_type)
'i ordered 2 cups of Masala chai'
>>> 

>>> chai_veriety = ["Lemon","Masala","Ginger"]
>>> "".join(chai_veriety)
'LemonMasalaGinger'
>>> " ".join(chai_veriety)
'Lemon Masala Ginger'