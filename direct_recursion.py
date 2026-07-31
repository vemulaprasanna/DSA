#Direct Recursion
#Code to print n natural numbers using recursion
def numbers(n):
    if n==0: #5==0 f, 4==0 f, 3==0 f, 2==0 f,1==0 f, 0==0 t
        return
    print(n, end=" ")
    numbers(n-1) #5-1=4, 4-1=3, 3-1=2, 2-1=1, 1-1=0
n=int(input("Enter a number: ")) 
numbers(n) #5