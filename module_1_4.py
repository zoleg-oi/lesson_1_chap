# Организация программ и методы строк.
my_string = input('Введите любую строку: ')
len_str = len(my_string)
print('Количество символов введенного текста: ' + str(len_str))

#Методы строк
print('Строка в верхнем регистре: ' + my_string.upper())
print('Строка в нижнем регистре: ' + my_string.lower())
print('Строка без пробелов: ' + my_string.replace(' ',''))
print('Первый символ : "' + my_string[0] + '"' )
print('Последний символ : "' + my_string[len_str-1] + '"' )
