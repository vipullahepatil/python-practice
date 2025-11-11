

def my_decorator(fun):
    def wrapper():
        fun()
        print("Inside decorator")
    return wrapper

# def hello_world():
#     print("Hello Vipul")

# my_decorator(hello_world)()

@my_decorator
def hello_world():
    print("Hello Vipul")

hello_world()