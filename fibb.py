def fibonacci(n):
    fib_sequence=[]
    a,b=0,1

    for _ in range(n):
        fib_sequence.append(a)
        a, b=b,a+b
    return fib_sequence
n=int(input("enter the fib sequence to generate:"))
fib_numbers=fibonacci(n)
print("fibonacci:",fib_numbers)