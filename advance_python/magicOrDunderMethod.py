

class Vector:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x+other.x,self.y+other.y)

    def __call__(self):
        return "Call is called"
    
    # def __del__(self):
    #     print("Dell get calll", self)

    def __eq__(self, other): #== call this method internalll
        print("__eq__ called")
        return  self.x == other.x and self.y == other.y
    

    # perferance giving to __str__ over __repr__
    
    # def __str__(self):
    #     return f'X = {self.x} , Y = {self.y} in str'
    
    def __repr__(self):
        return f'X = {self.x} , Y = {self.y} in repr'
    
    # def __str__(self):
    #     return f'X = {self.x} , Y = {self.y} in str'



v1 = Vector(1,2)
v2 = Vector(5,7)

v3 = v1+v2


print(v1.x , v1.y)
print(v2.x , v2.y)
print(v3.x , v3.y)

print(v1())
print(v1)
print("checking equality",v1==v2)
# print("checking equality by is",v1 is v2)
# print("checking equality by __eq__",v1 is v2)
