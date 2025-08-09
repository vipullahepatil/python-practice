# 


from functools import reduce


avg = lambda x,y : (x+y)/2 
print(avg(3,5))

avg_from_list = reduce(lambda x,y : (x+y),range(11))/10
print(avg_from_list)