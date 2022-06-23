# # объявление функции import math
#
#
# def get_middle_point(x1, y1, x2, y2):
#     x = (x1 + x2) / 2
#     y = (y1 + y2) / 2
#     return x, y
#
#
# # считываем данные
# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())
#
# # вызываем функцию
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)


# # объявление функции
# def get_circle(radius):
#     c = 2 * math.pi * radius
#     s = math.pi * (radius**2)
#     return c, s
#
#
# # считываем данные
# r = float(input())
#
#
# # вызываем функцию
# length, square = get_circle(r)
# print(length, square)

# объявление функции
# from math import sqrt
#
#
# def solve(a, b, c):
#     d=b**2-4*a*c
#     if d>0:
#         x1=(-b-sqrt(d))/(2*a)
#         x2=(-b+sqrt(d))/(2*a)
#         return min(x1,x2), max(x1, x2)
#     elif d==0:
#         x=-b/(2*a)
#         return x, x
#
# # считываем данные
# a, b, c = int(input()), int(input()), int(input())
#
# # вызываем функцию
# x1, x2 = solve(a, b, c)
# print(x1, x2)


def year_by(year):
    animals = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"]
    i = year % 12
    return animals[i]


#print(year_by(int(input())))

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list2=7000
#
# list1[2][2].append(list2)
#
# print(list1)
# print(list1[2][2])

# list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = -1
# for i in range(len(list1)):
#     if max(list1[i]) > maximum:
#         maximum = max(list1[i])
# print(maximum)

# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# total = 0
# counter = 0
# for i in range(len(list1)):
#     total += sum(list1[i])
#     counter += len(list1[i])
# print(total/counter)

def ind_mt(m,r):
    imt = m/(r**2)
    return imt

if ind_mt(m,r)< 18.5:
    print()

