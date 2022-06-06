def func(a,b,char):
    if (char=="+"):
        return a+b
    elif (char=="-"):
        return a-b 
    elif (char=="*"):
        return a*b 
    elif (char=="/"):
        return a/b     

a=int(input("Enter first number :- "))
b=int(input("Enter the second number :- "))
char=input("Enter the operation to be performed :- ")

ans=func(a,b,char)
print(ans)