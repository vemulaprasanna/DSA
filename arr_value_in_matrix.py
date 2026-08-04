#5. find index of given value in matrix
r= int(input("Enter rows: "))
c=int(input("Enter columns: "))
arr=[]
print("Enter elements: ")
for i in range(r):
    row=[]
    for j in range(c):
        row.append(int(input()))
    arr.append(row)
target=int(input("Enter the target want to search: "))
found = False
for i in range(r):
    for j in range(c):
        if arr[i][j]==target:
            print("Target found at: ",i,j)
            found = True
            
if found==False:
    print("Element not found...")