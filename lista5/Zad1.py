class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return (3 * key + 5) % self.size

    def add_key(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)

    def __str__(self):
        table=[]
        for i in range(self.size):
            table.append(self.table[i])
        return str(table)

keys = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]

hash_table = HashTable(11)

for key in keys:
    hash_table.add_key(key)

print(hash_table)
