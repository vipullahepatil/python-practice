'''
Question 2 – New Topic (Data Structures / Design)

Problem: Design a data structure that supports the following operations in O(1) time:

insert(val) – Inserts an integer val into the data structure.

remove(val) – Removes val if it exists.

getRandom() – Returns a random element from the current set of elements. Each element must have equal probability of being returned.

Example:

ds = RandomizedSet()
ds.insert(10)     # True
ds.insert(20)     # True
ds.insert(10)     # False, already exists
ds.getRandom()    # Could return 10 or 20
ds.remove(10)     # True
ds.getRandom()    # Returns 20


Constraints / Notes:

All operations must be O(1).

You can assume the inputs are integers.

Think carefully about what data structures to use to achieve O(1) for all operations.

'''

class RandomizedSet:
    def __init__(self):
        self.set = set()

    def insert(self,ele):
        return self.set.add(ele)
    
    def remove(self,ele):
        return self.set.remove(ele)
    
    def getRandom(self):
        for i in self.set:
            print("randon",i)
    

ds = RandomizedSet()
ds.insert(10)     # True
ds.insert(20)     # True
ds.insert(10)     # False, already exists
ds.getRandom()    # Could return 10 or 20
print(ds.set)
ds.remove(10)     # True
print(ds.set)
ds.getRandom()    # Returns 20
ds.insert(30) 
ds.getRandom()    # Returns 20
ds.insert(40) 
ds.getRandom()    # Returns 20
ds.getRandom()    # Returns 20
ds.getRandom()    # Returns 20
ds.getRandom()    # Returns 20

