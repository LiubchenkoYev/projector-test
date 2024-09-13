x = float(input('Enter first number: '))
op = input('Enter operator (+,-,*): ')
y = float(input('Enter second number: '))
print(x, op, y)


def calculate(x, y, op):
    if op == '+':
        result = x+y
    elif op == '-':
        result = x-y
    elif op == '*':
        result = x*y
    return result


result = calculate(x, y, op)
print('=', result)
