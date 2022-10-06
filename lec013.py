# Анонимные функции

'''
def calc1(x):
    return x+10

print(calc1(4))

def calc2(x):
    return x*10

print(calc2(4))

def math(op, x):
    print(op(x))

math(calc1, 10)
math(calc2, 10)
'''

# lambda функции

#def sum(x, y):
#    return x+y

sum = lambda x, y: x+y

#def mylt(x, y):
#    return x*y

mylt = lambda x, y: x*y

def calc(op, a, b):
    print(op(a, b))
    # return op(a, b)

#calc(sum, 4, 5)

calc(lambda x, y: x*y, 4, 5)
