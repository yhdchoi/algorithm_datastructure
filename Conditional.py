# Conditional
a = 5
if a <= 0:
    print("a<=0")
elif a < 10:
    print("0 < a < 10")
else:
    print("a >= 10")
# NOTE: x in list, x not in list, or, and

# pass
b = 85
if b >= 80:
    pass
else:
    print("b < 80")

# Conditional Expression
result = "Success" if b >= 80 else "Fail"
print(result)

# Loop
i = 1
total = 0

while i <= 9:
    total += i
    i += 1
print(total)

while i <= 9:
    if i % 2 == 1:
        total += i
    i += 1
print(total)

# break
i = 0
while True:
    if i == 5:
        break
    i += 1

# for -> can use with list, tuple
arr = [7, 3, 5, 2]
for x in arr:
    print(x)

fin = 0
for i in range(1, 10):
    fin += i
print(fin)

# continue -> doesn't continue to next but goes back to the start
for i in range(1, 10):
    if i % 2 == 0:
        continue
    fin += i
print(fin)

