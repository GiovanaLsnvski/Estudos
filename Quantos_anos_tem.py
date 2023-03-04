nscmt=int(input('Em que ano nasceu? '))
print('Digite "s" para sim e, "n" para não: ')
nvsr=input('ja fez aniversário esse ano? ')
ano_atual=2023
if nvsr == 'n':
    idade=(ano_atual-nscmt)-1
elif nvsr =='s':
    idade = ano_atual-nscmt
print('Sua idade é: {}' .format(idade))
