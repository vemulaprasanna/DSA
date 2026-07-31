#arg pass return value --->value taken from global
def summate(a,b): #calle #4,5
    return a+b #4+5 #9
n1=int(input("Enter a first value: ")) #4
n2=int(input("Enter a second value: ")) #5
result=summate(n1,n2) #caller #4,5 
print("Sum:",result) #9


#arg pass no return value --->value taken from global
def summate(n1,n2): #4,5
    print("Sum:",n1+n2) #4+5 #9
n1=int(input("Enter n1: ")) #4
n2=int(input("Enter n2: ")) #5
summate(n1,n2) #4,5


#no arg return value --->value taken from local
def summate(): #9
    n1=int(input("Enter n1: ")) #4
    n2=int(input("Enter n2: ")) #5
    return n1+n2 #4+5 #9
result=summate() #9
print("Sum:",result)#9


#no arg no return value
def summate():
    n1=int(input("Enter n1: ")) #4
    n2=int(input("Enter n2: ")) #5
    print("Sum: ",n1+n2) #4+5 #9
summate()
