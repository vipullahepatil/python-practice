class BST:

    def __init__(self,data):
        self.data = data
        self.left=None
        self.right=None

    def add_child(self,data):
        if data == self.data :
            return
        # left side
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST(data)

    

    def in_order_travrsal(self):
        element = []

        if self.left:
            element += self.left.in_order_travrsal()
        
        element.append(self.data)

        if self.right:
            element += self.right.in_order_travrsal()

        return element


bst = BST(50)
no = [39,47,65,55,75,79,23,1,62]
for i in range(1,len(no)):
    bst.add_child(no[i])

print(bst.in_order_travrsal())


a = [1,2]
b = [3,4]
c = a+b
print(c)

