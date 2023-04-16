# create hash table
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
# test hash table
t = HashTable()
t['march 6'] = 310
t['march 7'] = 420
t['march 8'] = 280
# print(t.arr)
print(t['march 6'])
# output: