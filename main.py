def number(number):
    try:
        return 50 / number
    except ZeroDivisionError:
        print('Error : you try to divide by zero')

print(number(2))
print(number(5))
print(number(0))