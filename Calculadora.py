num1 = float(input(print('Digite um número: ')))
num2 = float(input(print('Digite outro número: ')))

op = input(print('Qual operação deseja realizar? (use +, -, /, *)'))

if op == '+':
    soma = num1 + num2
    print(num1, op, num2, '=', soma)

if op == '-':
    subt = num1 - num2
    print(num1, op, num2, '=', subt)

if op == '/':
    divi = num1 / num2
    print(num1, op, num2, '=', divi)

if op == '*':
    mult = num1 * num2
    print(num1, op, num2, '=', mult)
