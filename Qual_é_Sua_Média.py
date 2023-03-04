matter=input('Qual o nome de sua disciplina? ')
print('Digite suas 4 notas do bimestre: ')
nota1=int(input())
nota2=int(input())
nota3=int(input())
nota4=int(input())
matter_media=(nota1+nota2+nota3+nota4)/4
print('A sua média da matéria de {} é de {} ' .format(matter, matter_media))
