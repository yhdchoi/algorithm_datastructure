a = int(1e9)
print(a)

print(round(123.543, 2))

b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(b[2])
print(b[-3])
b[4] = 12
print(b[4])
print(b[2: 6])

n = 10
c = [0] * n
print(c)

# List Comprehension
arr = [i for i in range(10)]
print(arr)

# From 0 to 19, values that are odd nums
arr2 = [i for i in range(20) if i % 2 == 1]
print(arr2)

# List with squared values
arr3 = [i * i for i in range(10)]
print(arr3)

# 2D list
n = 4
m = 3
arr4 = [[0] * m for _ in range(n)]
print(arr4)

# Commonly used methods
arr5 = [4, 3, 2, 1]
arr5.reverse()
print(arr5)
arr5.insert(2, 3)
print(arr5)
print(arr5.count(3))
arr5.remove(1)
print(arr5)

arr6 = [1, 2, 3, 4, 5]
remove_set = {3, 5}
# The only values that are not in remove_set are saved.
result = [i for i in arr6 if i not in remove_set]
print(result)

# String
str1 = "abcdef"
print(str1[2:4])

# Tuple - Cannot replace values
tup = (1, 2, 3, 4, 5)
print(tup[1:4])

# Dictionary
data = dict()
data['Apple'] = 'Red'
data['Banana'] = 'Yellow'
data['Grape'] = 'Purple'
print(data)

if 'Apple' in data:
    print("We have an apple")

key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)
# To print the values in each key
for key in key_list:
    print(data[key])

# Set - no overlapping of values
set1 = set([1, 1, 2, 3, 4, 4, 5])
print(set1)
set2 = {4, 4, 5, 6, 7, 7, 8, 9}
print(set2)
print("-------------")
print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
print("-------------")
set3 = {1, 2, 3}
set3.add(4)
print(set3)
set3.update([5, 6])
print(set3)
set3.remove(2)
print(set3)
print("-------------")
