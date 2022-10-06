# Анонимные, lambda функции

'''
В файле хранятся числа, нужно выбрать четные и составить список пар (число; квадрат числа).
Пример:
1 2 3 5 8 15 23 38
Получить:
[(2, 4), (8, 64), (38, 1444)]
'''
# Решение моё
'''
def f(x):
    return x**2

list = [(i, f(i)) for i in (1, 2, 3, 5, 8, 15, 23, 38) if i % 2 == 0]
print(list)
'''
# Решение правильное
'''
def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data)
res = where(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x**2), res))
print(res)
'''
# Функция map
'''
li = [x for x in range(1, 21)]
li = list(map(lambda x: x+10, li))
print(li)
'''
# Функция map
'''
data = list(map(int, '1 2 3 4'.split()))
print(data)

for e in data:
    print(e)

print('--')

for e in data:
    print(e)
'''
# Функция filter
'''
data = '1 2 3 5 8 15 23 38'.split()
res = map(int, data)
res = filter(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x**2), res))
print(res)
'''
# Функция zip
'''
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
data = list(zip(users, ids, salary))
print(data)
'''
# Функция enumerate

users = ['user1', 'user2', 'user3', 'user4', 'user5']
data = list(enumerate(users))
print(data)
