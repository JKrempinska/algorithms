class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return (3 * key + 5) % self.size

    def add_key(self, key):
        index = self.hash_function(key)
        print(key,index)
        while self.table[index] is not None:
            index = (index + 1) % self.size
        self.table[index] = key

    def __str__(self):
        table=[]
        for i in range(self.size):
            table.append([self.table[i]])
        return(str(table))

keys = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]

hash_table = HashTable(len(keys))

for key in keys:
    hash_table.add_key(key)

print(hash_table)
