
n=int(input("Enter elements: ")) 
arr=[]
for i in range(n):
    val = int(input("Enter a value: ")) 
    arr.append(val)          
print("Original array: ")
for i in arr:
    print(i, end=" ")        
print()
#delete
pos=int(input("Enter position: "))
arr.pop(pos)
print("Latest array after delete an element: ")
for i in arr:
    print(i,end=" ")
print()



