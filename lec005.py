# Управляющие конструкции
# if, if-else

a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)
   
username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это Маша!')
elif username == 'Марина':
    print('Я так ждал Вас, Марина!')
elif username == 'Максим':
    print('Максим - топ)')
else:
    print('Привет, ', username)
