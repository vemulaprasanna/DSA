#searching and manipulations in array
# checking if an element is present in the array or not
arr=[]
n=int(input("enter the size of an array: "))
print("Enter elements: ")
for i in range(n):
    arr.append(int(input()))
target=int(input("Enter the element you want to find: "))
if target in arr:
    print(target,"Found ")
else:
    print(target,"not found ")





