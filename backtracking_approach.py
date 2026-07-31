def genrate(s, n):
    if len(s)==n:
        print(s)
        return
    genrate(s+'0',n)
    genrate(s+'1',n)
n=int(input("Enter length: "))
genrate("",n)