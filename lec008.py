# Текст

text = 'съешь еще этих мягких французских булок'
print(len(text)) # 39
print('еще' in text) # True
print(text.isdigit()) # False
print(text.islower()) # True
print(text.replace('еще', 'ЕЩЕ')) # замена
print(text[:]) # весь текст
print(text[2:14]) # ешь еще этих
print(text[6:-18]) # еще этих мягких
print(text[len(text)-2:]) # ок
