# find all of the positions of occurances

arr=[]
n=int(input("enter the size of an array: "))
print("Enter elements: ")
for i in range(n):
    arr.append(int(input()))
target=int(input("Enter target you want to count: "))
found = False
for i in range(n):   
    if arr[i]==target:
        print(target," found at index ", i)
        found=True
if found==False:
    print(target,"not found ")