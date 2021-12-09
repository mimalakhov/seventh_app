#Fourth_______________________________________________________________
''' Подключить библиотеку os. 
С её помощью вывести: 
     имя операционной системы; 
     имя пользователя, вошедшего в терминал; 
     список файлов и директорий в папке.
'''
import os
print(f'Operation system: {os.name}')
print(f'User name: {os.getlogin()}')
print(f'Dir List: {os.listdir()}')
print()

#Fifth_______________________________________________________________________
''' Установить через pip библиотеку numpy. 
    С помощью этой библиотеки Создать массив 3x3 со случайными значениями, вывести его. 
    Транспонировать его и вывести'''
import numpy as np
two_dimensions = np.array([[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]])
print("Matrix:")
print(two_dimensions)
print("New matrix:")
print(two_dimensions.transpose())
print()

#Sixth_________________________________________________________________
import helper

helper.func()
print("Enter the numbers")
try:
     a = int(input())
     b = int(input())
     c = int(input())
except ValueError:
     print("Wrong number!")
     helper.func()

helper.numpy_features(a, b, c)



