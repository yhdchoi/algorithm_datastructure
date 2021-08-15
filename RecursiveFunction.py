# Stack
def recursive_function(i):
    if i == 100:
        return
    print(i, 'th function is calling', i + 1, 'th function.')
    recursive_function(i + 1)
    print(i, 'th function is ending.')


recursive_function(1)
