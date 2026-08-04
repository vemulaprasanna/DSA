#4. find the largest /smallest element in an array

arr=list(map(int,input("Enter elements: ").split()))
#largest value
largest=arr[0]
for i in range(len(arr)):
    if arr[i]>largest:
        largest=arr[i]
print("Largest: ",largest)

#smallest value 
small=arr[0]
for i in range(len(arr)):
    if arr[i]<small:
        small=arr[i]
print("smallest: ",small)