class HashTable:
    def __init__(self):
        self.MAX = 100
        self.array = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.array[h] = value

    def __getitem__(self, item):
        h = self.get_hash(item)
        return self.array[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.array[h] = None


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

# It should return null.
print(t['March 6'])

