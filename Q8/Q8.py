def func(str):
    sum=0
    for i in str:
        if i.isdigit()==True:
            a=int(i)
            sum+=a

    return sum

str=input("enter the string :-")
print(func(str))