def A(str):
    num=len(str)
    for i in range(0,num):
        print(2*str[i],end="")

str=input("Enter the string :- ")    
print(A(str))    