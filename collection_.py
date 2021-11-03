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

# Set

my_set = {1, 1, 1, 2, 3, 4, 5}
print(my_set)
my_set.add(6)
print(my_set)
my_set.remove(1)
print(my_set)

set_a = {1, 2, 3, 4}
set_b = {8, 7, 6, 5, 4, 3}
print()
print('set_a: ', set_a)
print('set_b: ', set_b)
print('| for set: ', set_a | set_b)
print('& for set: ', set_a & set_b)
print('^ for set: ', set_a ^ set_b)
print('- for set: ', set_a - set_b)

# Dictionary

my_dict = {1: 'one', 2: 'two', 3: 'three'}
print(my_dict)
my_dict[4] = 'four'
print(my_dict)
my_dict[1] = 1
print(my_dict)
my_dict.pop(4)
print(my_dict)

