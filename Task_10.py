# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной
# и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

n=int(input("Введи количество монет, лежащих на столе: "))
r=int(input("Сколько монет лежат решкой вверх?: "))
o=n-r
print("Минимальное количество монет, которые нужно перевернуть = ")
if(r > o):
   print(o)
else:
   print(r)