# tree recursion - fibonacci number
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

n=int(input("Enter a nimber: "))
print("Fibonacci", fib(n))

#4 4<=1->f fib(4-1)+fib(4-2)  =>fib(3)+fib(2) =>=>2+1=3 ==>fib(4) -->o/p
#fib(3) 3<=1->f fib(3-1)+fib(3-2) =>fib(2)+fib(1) =>=>1+1=2
#fib(2) 2<=1->f fib(2-1)+fib(2-2) =>fib(1)+fib(0) =>=>1+0=1
#fib(1) 1<=1->T  return n-> 1
#fib(0) ->0
