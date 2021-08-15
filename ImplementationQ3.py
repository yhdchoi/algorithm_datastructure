# Chess -> find the knight location.
location = input()
row = int(location[1])
col = int(ord(location[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row + step[1]
    next_col = col + step[0]
    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        result += 1

print(result)
