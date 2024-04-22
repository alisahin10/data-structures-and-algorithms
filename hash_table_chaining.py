class HashTable:
    def __init__(self):
        self.MAX = 100
        self.array = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.array[h]):
            if len(element) == 2 and element[0] == key:
                self.array[h][idx] = (key, val)
                found = True
        if not found:
            self.array[h].append((key, val))

    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.array[arr_index]:
            if kv[0] == key:
                return kv[1]
        return None

    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.array[arr_index]:
            if kv[0] == key:
                self.array[arr_index].remove(kv)


t = HashTable()
t['March 6'] = 130
t['March 14'] = 200
t['March 21'] = 450

# Displays the data assigned to Hash Table
print(t['March 6'])
print(t['March 14'])
print(t['March 21'])

# Delete the assigned data.
del t['March 6']
print("---------------After Delete Process---------------")

# It should return None.
print(t['March 6'])
