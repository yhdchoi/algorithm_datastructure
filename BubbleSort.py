def bubble_sort(elements):
    size = len(elements)
    for i in range(size - 1):
        swapped = False
        for j in range(size - 1):
            if elements[j] > elements[j + 1]:
                tmp = elements[j]
                elements[j] = elements[j + 1]
                elements[j+1] = tmp
                swapped = True

        if not swapped:
            break


elements = [5, 34, 2, 36, 89, 15, 36]

bubble_sort(elements)
print(elements)
