# Time -> How many numbers that contain the num-input.
num = int(input())
count = 0

for h in range(num + 1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                count += 1
print(count)
