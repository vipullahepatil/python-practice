# palindrone
# s = input()
# print('yes' if s== s[::-1] else 'no')

# Count vowels
# name = "pp"
# count = 0
# for i in name:
#     if i in 'aAIiOoUuEe':
#         count+=1
# print(count)

# c = sum(1 for i in name if i in 'aAIiOoUuEe')
# print(c)

# Reverse string
# s = 'vaishnavi'
# print(s[::-1])


# Find frequency of characters (use dict)

# 1. Print numbers from 1 to N (Using Recursion)
# Q: Print numbers from 1 to n without using loops.

# def p(n):
#     print(n)
#     if n>=10:
#         return
#     return p(n+1)

# p(1)

# 2. Factorial of N
# Q: Calculate factorial(n) using recursion.

# def fact(n):
#     if n ==1:
#         return 1
#     return  n * fact(n-1) 

# print(fact(3))

# Fibonacci Number

# def fib(n):
#     if n <=1:
#         return n
#     return fib(n-1) + fib(n-2)

# print(fib(10))

# def perm(s, ans=""):
#     if len(s) == 0:
#         print(ans)
#         return
#     for i in range(len(s)):
#         perm(s[:i] + s[i+1:], ans + s[i])

# perm("abc")

# def perm(s, ans=''):
#     if len(s)==0:
#         print(ans)
#         return
#     for i in range(len(s)):
#         perm(s[:i]+s[i+1:],ans+s[i])

# perm('abc')


# def perm(s,ans=''):
#     if len(s)==0:
#         print(ans)
#         return
#     for i in range(len(s)):
#         perm(s[:i]+s[i+1:],ans+s[i])
# perm("abc")

# Check anagram (sorted(s1)==sorted(s2))

# s1 = 'abc'
# s2 = 'bba'

# print(sorted(s1)==sorted(s2))

# Remove duplicate characters
# s ='aasd'
# # print(''.join(set(s)))
# result = ""
# seen = set()
# for c in s:
#     if c not in seen:
#         seen.add(c)
#         result += c
# print(result)
    

# arr = [1, 2, 2, 3, 1, 4]
# result_l= []
# seen = set()
# for a in arr:
#     if a not in seen:
#         seen.add(a)
#         result_l.append(a)
# print(result_l)

# arr =[0, 1, 0, 3, 12]

# non_zero = [x for x in arr if x > 0]
# zero = [x for x in arr if x == 0]
# print(non_zero.extend(zero))
# print(non_zero)



# a = [1, 3, 5]
# b = [2, 4, 6]

# i = 0
# j = 0
# res = []
# while i < len(a) and j < len(b):
#     if a[i]< b[j]:
#         res.append(a[i])
#         i+=1
#     else:
#         res.append(b[j])
#         j+=1
# res.extend(a[i:])
# res.extend(b[j:])
# print(res)

# arr = [1, 2, 4, 5]
# n = len(arr) +1

# expected = (n*(n+1))//2
# print(expected-sum(arr))

def suuuu(num):
    num_arr = []
    def perm(s,ans=''):
        if len(s) == 0:
            num_arr.append(int(ans))
            return
        for i in range(len(s)):
            perm(s[i:]+s[:i+1],ans+s[i])
            perm(s[:i]+s[i+1:],ans+s[i])
    str_new = str(num)
    perm(str_new)
    return str(min(num_arr))
print(suuuu(912))