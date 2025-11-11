# import decimal
# integer = 10
# deci = decimal.Decimal(integer)
# print(deci)
# print(type(deci))
# print("{:.3f}".format(9.000000))
# print(round(10.878,2))

# string_v = "vippul"
# reverse_s = string_v[::-1]
# print(reverse_s)
# d = ""
# for i in string_v:
#     d = i+d
# print(d)

# v =  "Vipul lahe patil"

# vo = ['a','i','e','o','u']
# count = 0
# for i in v:
#     if i in vo or i.lower() in vo:
#         count+=1
# print(count)


# v =  "Vipul lahe patil"

# vo = ['a','i','e','o','u']
# count = 0
# for i in v:
#     if i in [" "]:
#         continue
#     if i not in vo or i.lower() not in vo:
#         count+=1
# print(count)

# v =  "Vipul lahe patil"
# char= "l"

# count = 0
# for i in v:
#     if i == char:
#         count += 1

# print(count)

# fib = [0,1]
# for i in range(5):
#     fib.append(fib[-1]+fib[-2])

# print(' '.join(str(i) for i in fib ))

# numberList = [15, 85, 35, 89, 125]
# max_no = numberList[0]
# # for i in numberList :
# #     if i > max_no:
# #         max_no = i
# numberList = [15, 85, 35, 89, 125, 2]
# print(max_no)
# for i in numberList:
#     print(i)
#     if i< max_no:
#         max_no =i

# print(max_no)

# numList = [1, 2, 3, 4, 5]
# print(len(numList)//2)
# midle_element = numList[len(numList)//2]
# print(midle_element)

# lst = ["P", "Y", "T", "H", "O", "N"]
# print("".join(lst))

# lst1 = [1, 2, 3]
# lst2 = [4, 5, 6] 
# res = []
# for a , b in zip(lst1,lst2):
#     res.append(a+b)
# print(res)

# str1 = "Listen"
# str2 = "Silent"

# di1= {}
# di2= {}

# for a , b in zip(str1,str2):
#     di1[a.lower()] = di1.get(a,0)+1
#     di2[b.lower()] = di2.get(b,0)+1

# for i in di1:
#     if di1.get(a) != di2.get(a):
#         print("False")
#         break

# print("True")

# str1 = list(str1.lower()).sort()
# str2 = list(str2.lower()).sort()
# if str2 == str1:
#     print("True")
# else:
#     print("False")


# st1 ="vipyiv"

# for i in range(len(st1)):
#     print("ind",0-i-1,"o-",i)
#     print(st1[i].lower())
#     print(st1[0-i-1].lower())
#     if st1[i].lower() != st1[0-i-1].lower():
#         print(False)
#         break

#     if i == (len(st1)//2)+1:
#         break
# print("True")

# str1 = "Kayak".lower()
# str2 = "kayak".lower()

# if str1  == str1[::-1]:
#     print("True")
# else:
#     print("False")

# string = "P r ogramm in g "
# print(string.count('r'))

# import re

# name = 'Python is 1'

# digCount = re.sub("[^0-9]","",name)
# latCount = re.sub("[^a-zA-Z]","",name)
# spaceCount = re.findall("[ \n]",name)
# print(digCount,latCount,spaceCount)

# spChar = "!@#$%^&*()"

# count = re.sub('[\w]',"",spChar)
# print(len(count))
# def remove_duplicates(l):
#     return list(set(l))

# print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))

# def fact(n):
#     if n <=1:
#         return 1
#     return n * fact(n-1)

# print(fact(3))

# l1= [1, 3, 5]
# l2=[2, 4, 6]

# l3 = []
# a=0
# b =0
# while True:
#     if a == len(l1) or  b == len(l2):
#         break
#     if l1[a]<=l2[b]:
#         l3.append(l1[a])
#         print("l3 add",)
#         a+=1
#     else:
#         l3.append(l2[b])
#         b+=1
# print("l3",l3,"a=",a,"b=",b)
# if a != len(l1):
#     l3 = l3+l1[a:]
# else:
#     print("s",l2[b:])
#     l3 = l3+l2[b:]
# print(l3)


# l1 = [1,2,4,6,5,3]
# l2 = l1.sort()
# print(l2)

# numbers = [5, 2, 9, 1]
# # numbers.sort()
# # print(numbers)  # [1, 2, 5, 9]
# numbers.sort(reverse=True)
# print(numbers)

# sq = [a*a for a in range(5)]
# print(sq)
# sq = lambda x : x*x
# print(sq(5))

l1= [1, 2,3, 4,5,6]

sq = list(map(lambda x : x*x , l1))
print(sq)
ev = list(filter(lambda x : x%2 == 0,l1))
print(ev)