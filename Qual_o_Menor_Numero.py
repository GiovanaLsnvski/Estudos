print('Digite três números diferentes: ')
num1=float(input())
num2=float(input())
num3=float(input())
if num1<num2:     #V,V,F,F
    if num1<num3: #V,F,V,F
        print('O primeiro número é menor! ') #V / V
    else:
        print('O terceiro número é menor! ') # V / F
else:
    if num2<num3:
        print('O segundo número é menor! ') # F / V
    #else:
        #print('O terceiro número é menor! ') #V / F

'''
#Uma segunda forma de resolver o mesmo problema

print('Digite três números diferentes: ')
num1=float(input())
num2=float(input())
num3=float(input())
if num1<num3 and num1<num2:
    print('O primeiro número é o menor! ')
elif num2<num1 and num2<num3:
    print('O segundo número é menor! ')
else:
    print('O terceiro número é o menor! ')
'''