'''
1  2  3  4
5  6  7  8
9 10 11 12
13 14 15 16
traversal the matrix in a spiral order and print the path 1 2 3 4 8 12 16 15 14 13 5 6 7 11 10'''

n=int(input("Enter the size: "))
r=int(input("Enter no.of rows: "))
c=int(input("Enter no.of columns: "))
a=[]
print("Enter matrix elements: ")
for i in range(r):
    row=[]
    for j in range(c):
        row.append(int(input()))
    a.append(row)
top=0
bottom=r-1
left=0
right=c-1
num=1
while top<=bottom and left<=right:
    #traverse at top from left to right
    for i in range(left,right+1):
        print(a[top][i],end=' ')
    top+=1
    #traverse at right from top to bottom
    for i in range(top,bottom+1):
        print(a[i][right], end=' ')
    right-=1
    #traverse at bottom from right to left
    for i in range(right,left-1,-1):
        print(a[bottom][i],end=' ')
    bottom-=1
    #traverse at left from bottom to top
    for i in range(bottom,top-1,-1):
        print(a[i][left],end=' ')
    left+=1


    



