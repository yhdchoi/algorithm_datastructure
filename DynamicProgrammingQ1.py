# The storage
# The total number of storage
n = int(input())
# The value for each storage
array = list(map(int, input().split()))
# DP table
d = [0] * 100

# Assign max value
d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])
