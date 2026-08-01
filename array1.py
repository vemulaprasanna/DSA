#Array Data Structure is a linear DS (1D) - [] one data type
#1. read and write an array - code to read n values and traverse those values and print them

n=int(input("Enter size of array: "))
arr=[]
for i in range(n):
    num = int(input("Enter a value: "))
    arr.append(num)
#arr = list(map(int,input("Elements: ").split()))
print("Array elements: ")
for i in range(n):
    print(arr[i],end=" ")
#print(*arr)


#2. find sum of array
#3. find th avg
#4. find the largest /smallest element in an array
#5. count the even and odd numbers /prime
#6. count pos/neg
#7. reverse an array
#8. left rotate
#9. right rotate
#10. array using strings