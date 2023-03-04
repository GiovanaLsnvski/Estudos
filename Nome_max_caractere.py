nome = input('Digite seu nome, com no máximo 20 carateres:')
if len(nome) <= 20:
    print('Obrigado, está tudo certo.')
else:
    print('Por favor digite novamente os carateres excedem o limite.')
    nome = input('Digite seu nome novamente, com no máximo 20 caracteres:')
