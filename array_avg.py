#3. find th avg

n=int(input("Enter size of array: "))
arr=[]
sum=0
for i in range(n):
    num = int(input("Enter a value: "))
    arr.append(num)   
print("Array elements: ")
for i in range(n):
    sum = sum+arr[i]
print('Avg: ', float(sum/n))