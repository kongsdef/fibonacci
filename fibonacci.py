def fib(n):
    a,b=0,1
    for i in range(n):
        if i %2==0:
            print(a,b,end=" ")
        a,b=b,a+b
    print()
fib(20)    
