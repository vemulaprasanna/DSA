# count how many times the element  is present in the array

arr=[]
n=int(input("enter the size of an array: "))
print("Enter elements: ")
for i in range(n):
    arr.append(int(input()))
target=int(input("Enter target you want to count: "))
c=0
for i in range(n):   
    if arr[i]==target:
        c+=1
print("Count of", target,"is: ", c)
