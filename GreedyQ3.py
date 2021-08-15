n = int(input())  # ?
data = list(map(int, input().split()))
data.sort()

# Total num of groups
result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)
