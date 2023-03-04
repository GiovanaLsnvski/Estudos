nome = input(print('Olá, senhor(a)?'))
print('Bom oi, senhor  {} '.format(nome))
turno = input(
    print('Diga nos em que turno trabalha. (use M-Manhã, T-tarde, N-Noite)'))

if turno == 'M':
    print('Bom dia!')
elif turno == 'T':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
