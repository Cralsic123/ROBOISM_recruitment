import random
A=[]
for i in range (1,100):
    A.append(i)
rand=random.randint(1,100)
A.append(rand)

for i in range(0,100):
    for j in range(i+1,100):
        if (A[i]==A[j]):
            print("Duplicate element is :- ",A[j])


