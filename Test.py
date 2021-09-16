class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX







t = HashTable()

t["march 6"] = 120
t["march 17"] = 15
t["march 8"] = 34
t["march 3"] = 2
t["march 19"] = 59