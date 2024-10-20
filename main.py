n=int(input())
lst1=[]
lst2=[]
updated_list=[]

for i in range(n):
    a=int(input())
    lst1.append(a)
for i in range(n):
    b=int(input())
    lst2.append(b)

def summation():
    for i in range(n):
        sum=lst1[i]+lst2[i]
        updated_list.append(sum)
        sum=0
    return updated_list

def find_min_max():
    updated_list.sort
    min=updated_list[0]
    max=updated_list[-1]
    if min>max: 
        result=(max, min)
    else:
        result=(min, max)
    return result
print(summation())
print(find_min_max())
