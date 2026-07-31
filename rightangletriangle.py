'''j==0 or i==j or i==n-1
(i+j)==n-1 or j==n or i=n-1 or j==n-1
i==0 or i==j or j==n-1
i==0 or j==0 or i+j==n-1
i==0 or j==0 or (i+j)==n-1
i==n or j==2*i+1'''


n=int(input("\nEnter a value: "))
for i in range(n):
    for j in range(n):
        if j==0 or i==j or i==n-1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()