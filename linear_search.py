#Searching types
#1. Linear search (time complexity = O(n), space compleity=O(1))
#2. Binary search
#3. jump search

#1. Linear search
arr=list(map(int,input("Enter Elementa: ").split()))
target=int(input("Enter target value: "))
for i in range(len(arr)):
    if arr[i]==target:
        print(target,"Found at index: ",i)
        break