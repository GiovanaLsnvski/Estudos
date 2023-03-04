print('Precisamos de algumas informações suas, antes de verificarmos se você está apto ')
nome = input('Diga-nos seu nome completo: ')
idade = int(input('Diga-nos sua idade: '))
if idade >= 18:
    print('Você pode se inscrever para realizar o teste de motorista, {} procure um atendente para que ele possa te instruir. '.format(nome))
else:
    print('Você não pode se inscrever para realizar oteste de motorista, espere mais um tempo {}! ;) '.format(nome))
