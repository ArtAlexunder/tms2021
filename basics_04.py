# Identification

def print_list(list_1, list_2, list_3):
    print(f'Content - 1: {list_1}, 2: {list_2}, 3: {list_3}')
    print(f'Content - 1: {id(list_1)}, 2: {id(list_2)}, 3: {id(list_3)}')
    print(f'Content - 1 & 2: {id(list_1) == id(list_2)}')
    print(f'Content - 2 & 3: {id(list_2) == id(list_3)}')
    print(f'Content - 1 & 3: {id(list_1) == id(list_3)}')

print(id(1))
a = 1
print(id(a))
print(id(a) == id(1))
a += 1
print(id(a) == id(1))

first_list = [1, 2, 3]
second_list = [1, 2, 3]
third_list = first_list
# Result
print_list(first_list, second_list, third_list)
# Change 3 list
third_list.append(4)
print_list(first_list, second_list, third_list)
# Change 1 list
first_list.pop(1)
print_list(first_list, second_list, third_list)
# Change 1 list
first_list.remove(4)
print_list(first_list, second_list, third_list)
# 3 list is copy of 1
third_list = first_list.copy()
print_list(first_list, second_list, third_list)
# Change 3 list
third_list.append(4)
print_list(first_list, second_list, third_list)

