'''
Problem Statement
Design and implement an LRU (Least Recently Used) Cache using Python.
Implement the class LRUCache with the following methods:
get(key): Return the value of the key if it exists, otherwise return -1.
put(key, value): Insert or update the key-value pair. If the cache reaches capacity, evict the least recently used key.
'''

class LRUCache:
    def __init__(self):
        self.data = {}
        self.capacity = 0
    
    def get(self,key):
        if self.data.get(key):
            self.data[key]['count'] +=1
            return self.data[key]['val']
        else:
            return -1

    def put(self,key,val):
        if self.data.get(key):
            self.data[key]={
                "val":val,
                "count":self.data[key]['count']
            }
        else:
            if self.capacity >= 2:
                pass
                # remove least use
                c1 = 0
                d1= None
                c2 = 0
                d2 = None
                counter = 0
                for k,v in self.data.items():
                    if counter == 0: 
                        c1 =self.data[k]['count'] 
                        d1 =k
                    else:
                        c2  =self.data[k]['count'] 
                        d2 =k
                if c1<=c2:
                    self.data.pop(d1)
                else:
                    self.data.pop(d2)

                self.capacity -=1

            self.data[key]={
                "val":val,
                "count":0
            }
            self.capacity +=1

c = LRUCache()
print(c.data)
print(c.get('a'))
c.put('a','vipul')
print(c.get('a'))

print(c.data)
c.put('b','vaishnavi')
print(c.data)
print(c.capacity)
c.put('c','lahe')
print(c.data)
c.put('c','pune')
print(c.data)





