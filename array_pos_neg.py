#6. count pos/ne
n=int(input("Enter size of array: "))
arr=[]
pos=0
neg=0
for i in range(n):
    num=int(input("Enter the values: "))
    arr.append(num)

for i in range(n):
    if arr[i]>0:
        pos+=1
    else:
        neg+=1
print("Positive count: ",pos)
print("Negative count: ",neg)