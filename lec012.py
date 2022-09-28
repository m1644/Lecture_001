# Функции

'''
import lec010
print(lec010.f(1))
'''

'''
import lec010 as h
print(h.f(1))
'''

'''
def new_string(symbol, count):
    return symbol * count

print(new_string('!', 5))  # !!!!!
print(new_string('!'))     # Ошибка!
'''

'''
def new_string(symbol, count = 3):
    return symbol * count

print(new_string('!', 5))  # !!!!!
print(new_string('!'))     # !!!
print(new_string(4))       # 12
'''

'''
def concatenatio(*params):
    res: str = ""
    for item in params:
        res += item
    return res

print(concatenatio('a', 's', 'd', 'w'))  # asdw
print(concatenatio('a', '1'))            # a1
'''

# Кортеж

'''
a = (3, 4)
print(a)      # (3, 4)
print(a[0])   # 3
print(a[-1])  # 4

for item in a:
    print(item)
'''

# Словари

'''
dictionary = {}
dictionary = \
    {
        'up': '^',
        'left': '<',
        'down': 'v',
        'rigte': '>'
    }
print(dictionary)          # {'up': '^', 'left': '<', 'down': 'v', 'rigte': '>'}
print(dictionary['left'])  # <

for k in dictionary.keys():
    print(k)                 # Вывод всех ключей

for k in dictionary.values():
    print(k)                 # Вывод значений ключей
'''

# Множества

'''
colors = {'red', 'green', 'blue'}
print(colors)  # {'blue', 'red', 'green'}
colors.add('gray')
print(colors)  # {'gray', 'red', 'green', 'blue'}
colors.remove('red')
print(colors)  # {'green', 'gray', 'blue'}
#colors.remove('red')  # KeyError: 'red
colors.discard('red')  # ok
print(colors)  # {'green', 'gray', 'blue'}
colors.clear()
print(colors)  # set()
'''

'''
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()             # c = {1, 2, 3, 5, 8}
u = a.union(b)           # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b)    # i = {8, 2, 5}
dl = a.difference(b)     # dl = {1, 3}
dr = a.difference(a)     # dr = {13, 21}

q = a\
    .union(b) \
    .difference(a.intersection(b))
# {1, 21, 3, 13}

s = frozenset(a)
'''

# Списки

'''
list1 = [1, 2, 3, 4, 5]
list2 = list1

for e in list1:
    print(e)

print()

for e in list2:
    print(e)

list1[0] = 123

for e in list1:
    print(e)

print()

for e in list2:
    print(e)
'''

list1 = [1, 2, 3, 4, 5]
print(len(list1))
print(list1.pop())  # Удаляет последний элемент
print(list1)
print(list1.pop(2)) # Удаляет заданный элемент
print(list1)
print(list1.insert(2, 11)) # Добавляет элемент вместо заданного
print(list1)
print(list1.append(16))  # Добавляет элемент в конец списка
print(list1)
