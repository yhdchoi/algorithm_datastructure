def add(a, b):
    return a + b


def subt(c, d):
    print("The result is ", c - d)


print(add(3, 7))
subt(8, 3)

# Global
f = 0


def func():
    global f
    f += 1


for i in range(10):
    func()

print(f)


# Packing
def operator(h, g):
    addi = h + g
    subtr = h - g
    multi = h * g
    div = h / g
    return addi, subtr, multi, div


r, t, y, u = operator(7, 3)
print(r, t, y, u)
