# Преобразование 8-битного двоичного числа в десятичное.
# • Создайте комбинированный список из 8 элементов со значениями, являющимися степенями двойки - [128 64 32
# 16 8 4 2 1]
import numpy as np

tab =  [2 ** i for i in range(7,-1, -1)]
print(tab)

wagi = np.array([tab])
print(wagi)

liczba_bin = np.random.randint(low = 0,high = 2, size=(8))
print(liczba_bin)