# Yunfan Ye 10423172
def Fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

# arr = [1,2,3,4,5,6,7,8,9,10]
# for i in arr:
#     print(Fibonacci(i))  
