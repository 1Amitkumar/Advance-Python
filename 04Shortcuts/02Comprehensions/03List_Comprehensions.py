from random import randint


num = [randint(1, 50) for i in range(50)]
print(num, end='\n\n')


seven_multi = [x for x in num if not x % 7]
print(seven_multi)

