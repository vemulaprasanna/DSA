#Exponential time O(2^n)
def abc(n):
    if n==0:
        return
    print(n) #3
    abc(n-1)# 3-1=2 --> 1 -->1
    abc(n-1)# 3-1=2 --> 1 -->1
n= int(input("Enter a number: "))
abc(n) #n=3