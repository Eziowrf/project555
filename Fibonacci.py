# Yunfan Ye 10423172
def Fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
