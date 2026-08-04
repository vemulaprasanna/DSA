#find the index of an element

arr=[]
n=int(input("enter the size of an array: "))
print("Enter elements: ")
for i in range(n):
    arr.append(int(input()))
target=int(input("Enter the element you want to find: "))
found = False
for i in range(n):   
    if arr[i]==target:
        print(target," found at index ", i)
        found=True
        break
if found==False:
    print(target,"not found ")