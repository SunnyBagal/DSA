
# #* 0 1 1 2 3 5 8 13 21 34 55 89 144

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

for i in range(10):
    print(fibonacci(i), end=" ")


# def fino(n, a=0, b=1):
#     if n == 0:
#         return
    
#     print(a, end=" ")
#     return fino(n-1, b, a+b)


# fino(9)