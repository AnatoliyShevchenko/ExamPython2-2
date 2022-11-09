from operator import (truediv, mul, add, sub)


operators = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv
    }

def calculate(s):
    if s.isdigit():
        return int(s)
    for key in operators.keys():
        left, operator, right = s.partition(key)
        if operator in operators:
            return operators[operator](calculate(left), calculate(right))

s = input("Введите выражение: ")
print(calculate(s))


# # Вариант 2 самый простой
# x = input("введите выражение: ")
# print(eval(x))

