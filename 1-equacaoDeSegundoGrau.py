'''
Solicitar valores de a,b e c e calcaular a equação de segundo Grau.
Se o usuário informar o valor de A igual a zero, a equação não é de segundo grau
e o programa não deve pedir os demais valores, sendo encerrado.
Se o delta calculado for negativo a equação não possui valores reais. Informe ao usuário e encerre o programa
Se o delta calculado for igual a zero a equação possui apenas uma raiz. Informe-a ao usuário
Se o delta for positivo, a equação possi duas raizes; Informe-as ao usuário.
'''
from tkinter import *

def equacaoSegundoGrau():
    print('\t\t *-* Programa Calculo de equação de segundo Grau *-*')
    try:
       a = float(textBoxA.get("1.0", "end"))
       b = float(textBoxB.get("1.0", "end"))
       c = float(textBoxC.get("1.0", "end"))
       
       if(a == 0):
            print('Que chato! Infelizmente a equação não é de segundo grau')
            labelMensagemExtra["text"] = "Que chato! Infelizmente a equação não é de segundo gra"
       else:
            delta = pow(b,2)-4* a*c
            print(f'Delta é: {delta}')
            labelDelta["text"] = "Delta: " +str(delta)
        
            if(delta < 0):
                print('O delta possui um valor negativo, portanto não possui valores reais')
                labelMensagemExtra["text"] ="O delta possui um valor negativo, portanto não possui valores reais"

            elif(delta == 0):
                x = (-b + (delta** (1/2))) / (2*a)
                #or x = -b /(2*a)
                print('O delta possui valor igual a zero, portanto possui apenas uma raiz')
                print(f'\t\t O X é igual: {x} ')
                labelMensagemExtra["text"] = "O delta possui valor igual a zero, portanto possui apenas uma raiz" 
                labelResultado["text"] = f"O X é igual: {x}"
                
            else:
                x1 = (-b + (delta** (1/2))) / (2*a)
                x2 = (-b - (delta** (1/2))) / (2*a)
                print('O delta possui um valor positivo maior que zero, portanto possui duas raizes')
                print(f'\t\t X1 é igual: {x1} \n \t\t e X2 é igual a: {x2}') 
                labelMensagemExtra["text"] = "O delta possui um valor positivo maior que zero, portanto possui duas raizes; "
                labelResultado["text"] = f"X1 é igual: {x1} e X2 é igual a: {x2}"

    except ValueError:
        labelMensagemExtra["text"]="Por favor, preencha todos os campos com números válidos"
        
#equacaoSegundoGrau(float(input("Por favor, digite a: ")),float(input("Por favor, digite b: ")), float(input("Por favor, digite c: "))) 

#Criando uma janela
janela = Tk()
janela.title("Equação de segundo grau.")
#linha para a
textoA = Label(janela, text= "Digite A: ")
textoA.grid(column=0, row=0)
textBoxA = Text(janela,height=1, width=10)
textBoxA.grid(column=1,row=0)

#linha para b
textoB = Label(janela, text= "Digite B: ")
textoB.grid(column=0, row=1)
textBoxB = Text(janela,height=1, width=10)
textBoxB.grid(column=1,row=1)

#linha para c
textoC = Label(janela, text= "Digite C: ")
textoC.grid(column=0, row=2)
textBoxC = Text(janela,height=1, width=10)
textBoxC.grid(column=1,row=2)

#Botão para o calculo
botao = Button(janela, text="Calcular", command=equacaoSegundoGrau)
botao.grid(column=0, row=3)

#Label Delta
labelDelta = Label(janela, text=" ")
labelDelta.grid(column=1, row=3)

#Label para  A mensagem extra
labelMensagemExtra = Label(janela, text=" ")
labelMensagemExtra.grid(column=0, row=4)

#Label para o resultado
labelResultado = Label(janela, text=" ")
labelResultado.grid(column=0, row=5)


janela.mainloop() #-> Mantem a janela aberta.