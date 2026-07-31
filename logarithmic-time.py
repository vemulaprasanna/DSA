#logarithmic time O(log(n))
n= int(input("Enter a number: "))
while n>1:
    print(n)
    n//=2 # n=64 -->64//2=32, n=32 -->32//2=16, n=16 -->16//2=8, n=8 -->8//2=4, n=4 -->4//2=2