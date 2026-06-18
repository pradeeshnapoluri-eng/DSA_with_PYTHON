class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][i] = (key, value)
                    return
            self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None
obj = HashTable()
obj.insert('mom', 2)    
obj.insert('dad', 1)
obj.insert('bro', 3)
print('mom appears:', obj.get('mom'), 'times')
print('dad appears:', obj.get('dad'), 'times')
print('bro appears:', obj.get('bro'), 'times')
print('------------------------------------------------------------------')
### VScode has a built in function to count the frequency of an element in a list
# from collections import defaultdict
# arr=[2,2,3,4,5,1,2,2]
# my=3
# freq=defaultdict(int)
# for i in arr:
#     freq[i] += 1
# print(my, 'appears:', freq[my], 'times')
print('-------------------------------')
### Using a dictionary to count frequency
# freq={}
# arr=[2,2,3,4,5,1,2,2]
# for i in arr:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1
# print('Frequency of each element in the array:')
# for key, value in freq.items():
#     print(key, 'appears:', value, 'times')
print('------------------------------')
# arr = [7,7,3]
# freq = {}
# for num in arr:
#     if num in freq:
#         freq[num] += 1
#         print("if")
#     else:
#         freq[num] = 1
#         print("else")
# print('Frequency of each element in the array:')
# print(freq)
# print(7, 'appears:', freq[7], 'times')
# print(3, 'appears:', freq[3], 'times')