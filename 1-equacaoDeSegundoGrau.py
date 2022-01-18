'''
Solicitar valores de a,b e c e calcaular a equação de segundo Grau.
Se o usuário informar o valor de A igual a zero, a equação não é de segundo grau
e o programa não deve pedir os demais valores, sendo encerrado.
Se o delta calculado for negativo a equação não possui valores reais. Informe ao usuário e encerre o programa
Se o delta calculado for igual a zero a equação possui apenas uma raiz. Informe-a ao usuário
Se o delta for positivo, a equação possi duas raizes; Informe-as ao usuário. -> Teste Pull
'''
print('\t\t *-* Programa Calculo de equação de segundo Grau *-*')
a = float(input('Por favor, informe o valor para a'))

if(a == 0):
    print('Que chato! Infelizmente a equação não é de segundo grau')

else:
    b = float(input('Por favor, informe o valor para b'))
    c= float(input('Por favor, informe o valor para c'))
    delta = pow(b,2)-4* a*c
    print('Delta é: ' + str(delta))
   
    if(delta < 0):
        print('O delta possui um valor negativo, portanto não possui valores reais')

    elif(delta == 0):
        x = (-b + (delta** (1/2))) / (2*a)
        #or x = -b /(2*a)
        print('O delta possui valor igual a zero, portanto possui apenas uma raiz')
        print('\t\t O X é igual:'+ str(x))
        
    else:
        x1 = (-b + (delta** (1/2))) / (2*a)
        x2 = (-b - (delta** (1/2))) / (2*a)
        print('O delta possui um valor positivo maior que zero, portanto possui duas raizes')
        print('\t\t X1 é igual:'+ str(x1)+'\n \t\t e X2 é igual a:' + str(x2))   

