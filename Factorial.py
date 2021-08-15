# n! = 1 x 2 x 3 x ... x (n - 1) x n
# 0! & 1! = 1

def factorial_iterative(n):
    result = 1
    # multiplying 1 to n
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    # if n is lower than 1, return 1
    if n <= 1:
        return 1
    # n! = n * (n - 1)! in code
    return n * factorial_recursive(n - 1)


print('Implementing iterative: ', factorial_iterative(5))
print('Implementing recursive: ', factorial_recursive(5))
