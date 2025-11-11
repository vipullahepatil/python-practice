n= int(input())
li= input()
lii = li.split()
di = {}
for i in lii:
    di[i] = di.get(i,0)+1
max_no = 0
for k, v in di.items():
    if v >max_no:
        max_no = v
print(max_no)
