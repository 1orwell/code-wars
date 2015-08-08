def fib(n):
    fib_lst_sum = 1
    perim_sum = 0
    a,b = 1,1
    for i in range(n):
        a,b = b, a+b
        fib_lst_sum += a
    return fib_lst_sum

def perimeter(n):
    return 4*(fib(n))
