#2. Binary search
arr=list(map(int,input("Enter Elements: ").split()))
target=int(input("Enter target value: "))
l=0
r= len(arr)-1
found = False
while l<=r:
    m=(l+r)//2
    if arr[m]==target:
        print(target, " found at ", m)
        found=True
        break
    elif arr[m]>target:
        r=m-1
    else:
        l=m+1
if not found:
    print("Element does not exists")