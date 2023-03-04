salario = float(input(print('Digite quanto você ganha mensalmente: ')))

if salario <= 5000:
    abono = (salario * 15) / 100
    print('O seu abono é de R${} '.format(abono))
else:
    abono = (salario * 10) / 100
    print('O seu abono é de R${} '.format(abono))
