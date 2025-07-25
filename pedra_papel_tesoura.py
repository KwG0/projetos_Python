'''Pedra, Papel, Tesoura para controle de fluxos'''
import random

escolhas_bot = ['pedra', 'papel', 'tesoura']

start_input = input("Gostaria de jogar pedra, papel, tesoura comigo? \n Digite: \n 1 - para sim \n 0 - para não \n Minha escolha: ")
start = int(start_input)


if start == 1:
    print("Ok, vamos começar!")
    preparado = input("Preparado? ")
elif start == 0:
    print("Ok, até a próxima!")
else:
    print("Não entendi a sua resposta.")

if start == 1 and preparado == "sim":
     escolha_usuario = input("Qual será sua escolha: pedra, papel ou tesoura? ")
     vez_bot = random.choice(escolhas_bot)
     resultado= str(vez_bot)
     print("Eu escolho " + resultado)
elif start == 1 and preparado == "não":
    print("Ok, eu espero.")

# if ... : -> if padrão
# else : -> else padrão
# elif ...: -> elseif, porém do Python
# and -> &&
# or ->  ||
# for ... in range (): -> Loop
# while True or False: -> loop
# continue -> pula o item
# break = quebra loop
# else : -> Também pode ser usado no for
