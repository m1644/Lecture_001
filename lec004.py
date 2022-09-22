# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, not in
# gen

a = 1 < 4 and 5 > 2
print(a)

a = 1 == 2 # сравнение
print(a)

a = 1 != 2 # неравенство
print(a)

a = 'qwe'
b = 'qwe'
print(a == b)

f = 1 > 2 or 4 < 6
print(f)

f = [1, 2, 3, 4]
print(f)
print(not 2 in f)

is_odd = not f[0] % 2
print(is_odd)
