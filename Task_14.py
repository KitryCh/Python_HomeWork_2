# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n=int(input("Введите число: "))
i=2
while i<=n:
    print(i,end=' ')
    i=i*2