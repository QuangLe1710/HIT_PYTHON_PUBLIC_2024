def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    while len(fib_sequence) < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

n = int(input('Nhập vào giá trị của n : '))
fib_numbers = fibonacci(n)
print(f' Giá trị của số fibonanci thứ {n} là : {fib_numbers}')
