import sys

# IO
n = int(input())
data = list(map(int, input().split()))
data.sort(reverse=True)
print(data)

a, b, c = map(int, input().split())
print(a, b, c)

# system
data2 = sys.stdin.readline().rstrip()
print(data2)

print(a, end=" ")
print("The answer is " + str(7))

answer = 7
print(f"The answer is {answer}.")
