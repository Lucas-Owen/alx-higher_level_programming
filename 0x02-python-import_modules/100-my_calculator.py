#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    argc = len(argv)
    if argc != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    a = int(argv[0])
    operator = argv[1]
    a = int(argv[2])
    res = '{} {} {} = {}'
    match(operator):
        case '+':
            print(res.format(a, operator, b, add(a, b)))
        case '-':
            print(res.format(a, operator, b, sub(a, b)))
        case '/':
            print(res.format(a, operator, b, mul(a, b)))
        case '*':
            print(res.format(a, operator, b, div(a, b)))
        case _:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
