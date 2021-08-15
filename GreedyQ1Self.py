n, k = map(int, input().split())

result = 0
count = 0

while True:
    result = n % k

    if result == 0:
        n = n // k
    else:
        n = (n - 1)
        
    count += 1
    if n == 1:
        break

print(count)
