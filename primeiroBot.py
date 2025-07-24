'''Bot de prompt para treinar Input'''

name = input("Olá! Como você se chama? ")
print(f"É bom ter você por aqui, {name}!")
age_input= input(("Quantos anos você tem, " + name + "? "))
age = int(age_input)
bot_age = 2
age_difference = (age - bot_age)
print(f"Nossa! Você é {age_difference} anos mais velho que eu :) Eu tenho {bot_age} anos!")
color = input("Qual a sua cor favorita? ")
bot_fav_color = "preto"
print(f"Eu acho {color} uma cor muito bonita. Mas, a minha favorita é {bot_fav_color} embora muitos considere apenas uma ausência de cor.")

# print(type()) -> tipo do parâmetro 
# print(str()) -> número vira string
# print(int()) -> float vira inteiro sem arredondar
# print(float()) -> inteiro vira float
# print(bool()) -> string vira bool, se tiver vazio ou 0 será false
# input() -> coleta entradas