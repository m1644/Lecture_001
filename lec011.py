# Работа с файлами

'''
colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
#data.writelines(colors) # разделителей не будет
data.write('\nLINE 2\n')
data.write('LINE 3\n')
data.close()
'''

'''
with open('file.txt', 'a') as data:
    data.write('Line 1\n')
    data.write('Line 2\n')
'''


path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()
