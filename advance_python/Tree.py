class Tree:
    def __init__(self,name,designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent =None
    
    def add_cheldren(self, children):
        children.parent = self
        self.children.append(children)

    def print_name(self):
        space = ' '*self.get_level()*3
        prefix = '|__' + self.name

        print(space+prefix)
        for c in self.children:
            c.print_name()

    def print_desi(self):
        space = ' '*self.get_level()*3
        prefix = '|__' + self.designation

        print(space+prefix)
        for c in self.children:
            c.print_desi()
    
    def print_both(self):
        space = ' '*self.get_level()*3
        prefix = '|__' + f'{self.name} ({self.designation})'

        print(space+prefix)
        for c in self.children:
            c.print_both()

    def get_level(self):
        level =0
        while self.parent:
            level+=1
            self = self.parent
        return level


root = Tree("Nilupul",'CEO')

a1 = Tree("Chinmay",'CTO')
a2 = Tree("Gels",'HR Head')
root.add_cheldren(a1)
root.add_cheldren(a2)

a11 = Tree("Vishva",'Infrastucture Head')
a1.add_cheldren(a11)
a111 = Tree("Dhaval",'Cloud Manager')
a112 = Tree("Abhijit",'App Manager')
a11.add_cheldren(a111)
a11.add_cheldren(a112)

a21 =Tree("Peter",'Recruitment Manager')
a22 =Tree("Waqas",'Policy Manager')
a2.add_cheldren(a21)
a2.add_cheldren(a22)



# root.print_name()
# root.print_desi()
root.print_both()
# print(a11.get_level())



