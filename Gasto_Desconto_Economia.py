nome_prod = input('Digite o nome do produto : ')
valor_prod = float(input('qual o valor do produto ? '))
quant_prod = int(input('Qual a quantidade do produto ? '))
valor_final = (valor_prod * quant_prod)
print('O(a) {}, teve o valor de compra de : R${} '.format(nome_prod, valor_final))

valor_desc_porct = (valor_prod * 15 / 100)
valor_desc_final = (valor_final - valor_desc_porct)
print('Ao pagar a vista você tem 15% de desconto, dando R${} '.format(valor_desc_final))

valor_econom = (valor_final - valor_desc_final)
print('Economizando R${} '.format(valor_econom))
