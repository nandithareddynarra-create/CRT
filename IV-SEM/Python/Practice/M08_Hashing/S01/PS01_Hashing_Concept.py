'''
Hashing
Definition
Advantages'''
'''h(key) = key mod m
k = key value
m = size table
h(k) = k%2'''
a = 10
b = "Nandu"
c = 34.88
print(hash(a))
print(hash(b))
print(hash(c))
a = [10,20,30]
size = 7
table = [None]*size
for key in a:
    index = key % size
    table[index] = key
print(table)