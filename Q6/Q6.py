L_value=int(input("Enter the lower value of range :- "))
U_value=int(input("Enter the upper value of range :- "))

for i in range(L_value, U_value+1):
    if i>1:
        for i in range(2,i):
            if(i%i)==0:
                break
        else:
            print(i)

           