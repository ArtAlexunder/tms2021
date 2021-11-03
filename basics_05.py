# Atomarnie and Ssilocnie

a, b, c, d = 'spam'

print(a)
print(b)
print(c)
print(d)

a = b = c = d = 'mah'
print(a)
print(b)
print(c)
print(d)

string = 'Hello Alex'
list_string = string.split()
list_string.insert(0, '!')
list_string.append('!')
string = ' '.join(list_string)
print(string)
