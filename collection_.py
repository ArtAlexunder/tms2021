# List

k = [1, 2.0, 4, 'b']
print(len(k))
k[0] = 3
print(3 in k)
print(k[1::2])
k.append(4)
print(k)
k.pop(0)
print(k)
k.remove(4)
print(k)
k.remove(4)
print(k)
coll_2 = ['hello', 'world', 'my', 'name']
k.extend(coll_2)
k.insert(5, 123)
print(k)
