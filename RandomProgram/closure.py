def f1(x):
    def f2(y):
        return x ** y
    return f2

xyz= f1(2)
print(xyz(3))