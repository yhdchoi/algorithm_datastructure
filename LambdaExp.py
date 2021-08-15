# Add
print((lambda a, b: a + b)(3, 7))

# With tuple and function
arr = [('Daniel', 80), ('Linda', 90), ('Mike', 70)]


def my_key(x):
    return x[1]


print(sorted(arr, key=my_key))

# Simplified with lambda
print(sorted(arr, key=lambda x: x[1]))

# With map
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a + b, list1, list2)
print(list(result))
