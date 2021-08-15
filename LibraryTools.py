from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement
from collections import Counter
import math

# itertools
data = ['A', 'B', 'C']

result = list(permutations(data, 3))
print(result)

result2 = list(combinations(data, 2))
print(result2)

result3 = list(product(data, repeat=2))
print(result3)

result4 = list(combinations_with_replacement(data, 2))
print(result4)

# collections -> counting
counter = Counter(['red', 'blue', 'green', 'blue', 'blue'])
print(counter['blue'])
print(counter['green'])
print(dict(counter))


# math
def lcm(a, b):
    return a * b


print(math.gcd(21, 14))  # 최대 공약수
print(lcm(21, 14))  # 최소 공배수
