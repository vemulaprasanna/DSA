#5. count the even and odd numbers /prime

n=int(input("Enter size of array: "))
arr=[]
even=0
odd=0
for i in range(n):
    num=int(input("Enter the values: "))
    arr.append(num)

for i in range(n):
    if arr[i]%2==0:
        even+=1
    else:
        odd+=1
print("Even count: ",even)
print("Odd count: ",odd)
    
