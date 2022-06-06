def func(A,str):
    if (str=="asce"):
     A.sort()
     return A
    elif (str=="desc"):
     A.sort(reverse=True)
     return A
    elif(str=="none"):
        return A 


num=int(input("Enter the number of elements :- "))
list=[]

for i in range(num):

    A=int(input())

    list.append(A)

str=input("Enter the string i.e desc for descending, asce for ascending and none for nothing ")

ans_list=func(list,str)

print(ans_list)