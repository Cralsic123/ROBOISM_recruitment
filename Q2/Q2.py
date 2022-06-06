list=[]
num=int(input("Enter the number of digits in the card number :-"))
for i in range(0,num):
    A=input()
    list.append(A)

for i in range(0,num-4):
    list[i]="*"    

for i in range(0,num):    
    print(list[i],end="")


    
    