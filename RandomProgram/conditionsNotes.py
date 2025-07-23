

'''
1. Age groupcategorization
2. Movie ticket pricing
3. Greade calculator
4. Fruit Ripeeness checker
5. weather Activity suggestion
6. Transportation mode Selection
7. Coffee Customization
8. Password Strength Checker
9. Leap Year Checker
10. Pet Food Recommendation
'''

# age = int(input("Enter your age: "))
# if age < 13:
#     print("You are a Child.")
# elif 13 <= age < 20:
#     print("You are a Teenager.")
# elif 20 <= age < 60:
#     print("You are an Adult.")
# else:
#     print("You are a Senior.")

# movie_prices = {
#     "metro in dino":500,
#     "son of serdar": 200,
# }

# movie_name = input("Enter movie name:")
# if movie_name in movie_prices:
#     print(f'Movie {movie_name} price is {movie_prices.get(movie_name)}')
# else:
#     print(f"Movie {movie_name} not found in the database.")

'''
Problem: Calculate movie ticket price based on age group: 
Child(<13): $5, Teenager(13-19): $8, 
Adult(20-59): $12, Senior(60+): $6.
Everyone gets a discount of 10% 
if they book online.
'''
# price = 0
# discount = 10
# booking_mode= input("Enter booking mode (online/offline): ").strip().lower()    

# if age < 13:
#     price = 5
#     print("You are a Child.")
# elif 13 <= age < 20:
#     price = 8
#     print("You are a Teenager.")
# elif 20 <= age < 60:
#     price = 12
#     print("You are an Adult.")
# else:
#     price = 6
#     print("You are a Senior.")

# if booking_mode == "online":
#     after_discount_price = price - (price * (discount / 100))
#     print(f"Your offer price was: ${price} \n final ticket price after discount is: ${after_discount_price}")
# else:
#     print(f"Your Movies price is ${price}")
'''
greade calculator
(90-100)A
(80-89)B
(70-79)C
(60-69)D
(below-60)F
'''

# marks = int(input("Enter marks:"))
# grade = ""
# if marks >= 90 and marks <=100 :
#     grade = "A"
# elif marks >= 80 and marks <=89 :
#     grade = "B"
# elif marks >= 70 and marks <=79 :
#     grade = "C"
# elif marks >= 60 and marks <=69 :
#     grade = "D"
# else:
#     grade ="F"
# print(f"Your marks is {marks} and your grade is {grade}")

# input_string = "Python"
# reversed_string =""
# count = 0
# len_str = len(input_string)
# for char in input_string:
#     reversed_string = char + reversed_string

# print(reversed_string)

# i = "teerter"
# no_count ={}
# for ip in i:
#     if ip not in no_count:
#         no_count.update({ip:1})  
#     else:
#         no_count[ip] += 1

# for key, value in no_count.items():
#     if value == 1:
#         print(key)
#         break

# for chr in i:
#     if i.count(chr) == 1:
#         print("first rep no",chr)
#         break


# cube = lambda x : x ** 3

# print(cube(10))


# def sum_all(*args):
#     return sum(args)

# print(sum_all(1,2,3))
# print(sum_all(1,2,3,4,5))

# def print_kwargs(**kwargs):
#     for key , value in kwargs.items():
#         print(key,value)

# # # def print_kwargs(name = "shaktiman",power ="lazer"):
# # def print_kwargs(name ,power):
# #     # return f'Name = {name} ,Power ={power}'
# #     print('Name = ',name,'Power =',power)

# print(print_kwargs(power ="lazer",name = "shaktiman"))
# print(print_kwargs(name = "shaktiman",power ="lazer"))
# print(print_kwargs(name = "shaktiman"))
# print(print_kwargs(name = "shaktiman",power ="lazer",emeny = "Dr. Jackaal"))

def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i
    
for i in even_generator(10):
    print(i)