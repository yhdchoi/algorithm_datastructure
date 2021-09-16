class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hs = 0
        for char in key:
            hs += ord(char)
        return hs % self.MAX

    # def add(self, key, val):
    #     h = self.get_hash(key)
    #     self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False

        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break

        if not found:
            self.arr[h].append((key, value))

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]



t = HashTable()

#t.add("march 8", 67)

t["march 6"] = 120
t["march 17"] = 15
t["march 8"] = 34
t["march 3"] = 2
t["march 19"] = 59

print(t.arr)
del t["march 17"]
print(t.arr)