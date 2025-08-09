# def cube(f):
#     return f * f * f

# print(cube(5))


# l = [ 1,2,4,6,4,3]
# new_list =[]
# for i in l:
#     new_list.append(cube(i))

# print(new_list)

# new_ls = list(map(cube, l))
# print(new_ls)

# # return even value
# even_no= []
# def filter1(a):
#     if a%2 == 0:
#         even_no.append(a)
# def new_filter(a):
#     return a%2 ==0

# for i in l:
#     filter1(i)

# print(even_no)

# new_filter1 = list(filter(new_filter,l))
# print(new_filter1)


# by_lambada_cube  =  list(map(lambda x : x * x * x , l))
# print(by_lambada_cube)

# by_lambada_filter =list(filter(lambda x : x%2 == 0 , l))
# print(by_lambada_filter)

from functools import reduce


l = [ 1,2,4,6,4,3]

def mysum(x,y):
    return x+y

my_reduce = reduce(mysum,l)
print(my_reduce)

print(reduce(lambda x,y : x + y ,range(11)))