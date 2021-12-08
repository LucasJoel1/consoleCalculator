import time
import os

os.system('cls')
equation = None
while equation != 'exit':
    print(' ')
    print('Welcome to console calculator, perform simple equations in the calculator')
    print('Type exit to exit the calculator')
    print('Type help to get a list of available operations')
    print('Type clear to clear the console')
    equation = input('Enter equation: ')
    
    if equation == 'exit':
        pass
    elif equation == 'help':
        os.system('cls')
        print('Available operations:')
        print('+ - addition')
        print('- - subtraction')
        print('* - multiplication')
        print('/ - division')
        print('sqrt - square root')
        print('pow - power')
        print('py - pythagorean theorem')
        print('dist - distance between two points')
        print('slp - slope of a line')
        print('mid - midpoint of a line')
        print('clear - clear the console')
    
    elif equation == '+':
        os.system('cls')
        input1 = float(input('Enter first number: '))
        input2 = float(input('Enter second number: '))
        print(f'{input1} + {input2} = {input1 + input2}')
        print(f'Result: {input1 + input2}')
    elif equation == '-':
        os.system('cls')
        input1 = float(input('Enter first number: '))
        input2 = float(input('Enter second number: '))
        print(f'{input1} - {input2} = {input1 - input2}')
        print(f'Result: {input1 - input2}')
    elif equation == '*':
        os.system('cls')
        input1 = float(input('Enter first number: '))
        input2 = float(input('Enter second number: '))
        print(f'{input1} * {input2} = {input1 * input2}')
        print(f'Result: {input1 * input2}')
    elif equation == '/':
        os.system('cls')
        input1 = float(input('Enter first number: '))
        input2 = float(input('Enter second number: '))
        print(f'{input1} / {input2} = {input1 / input2}')
        print(f'Result: {input1 / input2}')
    elif equation == 'sqrt':
        os.system('cls')
        input1 = float(input('Enter number: '))
        print(f'Square root of {input1} is {input1 ** 0.5}')
    elif equation == 'pow':
        os.system('cls')
        input1 = float(input('Enter first number: '))
        input2 = float(input('Enter second number: '))
        print(f'{input1} to the power of {input2} is {input1 ** input2}')
    elif equation == 'py':
        os.system('cls')
        input1 = float(input('Enter first number: '))
        input2 = float(input('Enter second number: '))
        print(f'a²+b²=c²')
        print(f'{input1}²+{input2}²=c²')
        print(f'{input1 ** 2}²+{input2 ** 2}²=c²')
        print(f'{input1 ** 2}+{input2 ** 2}={input1 ** 2 + input2 ** 2}')
        print(f'c=√{input1 ** 2 + input2 ** 2}')
        print(f'{(input1 ** 2 + input2 ** 2) ** 0.5}')
    elif equation == 'clear':
        os.system('cls')
        print('Console cleared')
    elif equation == 'dist':
        x1 = float(input('Enter the first x point: '))
        y1 = float(input('Enter the first y point: '))
        x2 = float(input('Enter the second x point: '))
        y2 = float(input('Enter the second y point: '))
        print(f'd=(x2-x1)²+(y2-y1)²')
        print(f'd=({x2}-{x1})²+({y2}-{y1})²')
        print(f'd={x2 - x1}²+{y2 - y1}²')
        print(f'd=√{(x2 - x1) ** 2 + (y2 - y1) ** 2}')
        print(f'd={((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5}')
        print(f'The distance between the two points is {((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5}')

    elif equation == 'slp':
        x1 = float(input('Enter the first x point: '))
        y1 = float(input('Enter the first y point: '))
        x2 = float(input('Enter the second x point: '))
        y2 = float(input('Enter the second y point: '))
        print(f'y2-y1/x2-x1')
        print(f'{y2}-{y1}/{x2}-{x1}')
        print(f'{y2 - y1}/{x2 - x1}')
        print(f'{(y2 - y1) / (x2 - x1)}')
        print(f'Slope of the line is {(y2 - y1) / (x2 - x1)}')
    elif equation == 'mid':
        x1 = float(input('Enter the first x point: '))
        y1 = float(input('Enter the first y point: '))
        x2 = float(input('Enter the second x point: '))
        y2 = float(input('Enter the second y point: '))
        print(f'(x1+x2)/2,(y1+y2)/2')
        print(f'({x1}+{x2})/2,({y1}+{y2})/2')
        print(f'({x1 + x2})/2,({y1 + y2})/2')
        print(f'({(x1 + x2) / 2},{(y1 + y2) / 2})')
        print(f'Midpoint of the line is {(x1 + x2) / 2},{(y1 + y2) / 2}')
    else:
        os.system('cls')
        print('Invalid input')
        input('Press any key to return to the calculator')
        os.system('cls')
os.system('cls')
print('Thank you for using the calculator')
time.sleep(3)
exit()