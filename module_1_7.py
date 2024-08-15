# Средний балл

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Изменяем тип данных множества students на список
students = list(students)

# В цикле проходим и подсчитываем средний балл и записываем по порядку в новый список
for i in range(0, len(grades)):
    grades[i] = sum(grades[i]) / len(grades[i])
# сортируем спиок с именами студентов по возрастанию
students.sort()
# Организуем новый пустой словарь
students_gr = {}
# В цикле проходим по спику студентов и назначаем им значение из списка со средними баллами.
for ii in range(0, len(students)):
    students_gr.update({students[ii]: grades[ii]})
print('Результат решения с использованием циклов')
print(students_gr)
print()

# можно циклы и не использовать, получиться громозкая конструкция, но аналогично рабочая.

grades_1 = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students_1 = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_1 = list(students_1)

grades_1[0] = sum(grades_1[0]) / len(grades_1[0])
grades_1[1] = sum(grades_1[1]) / len(grades_1[1])
grades_1[2] = sum(grades_1[2]) / len(grades_1[2])
grades_1[3] = sum(grades_1[3]) / len(grades_1[3])
grades_1[4] = sum(grades_1[4]) / len(grades_1[4])

students_1.sort()
students_gr_1 = {}
students_gr_1.update({students_1[0]: grades_1[0], students_1[1]: grades_1[1],
                      students_1[2]: grades_1[2], students_1[3]: grades_1[3],
                      students_1[4]: grades_1[4], })
print('Результат решения без использования циклов')
print(students_gr_1)
