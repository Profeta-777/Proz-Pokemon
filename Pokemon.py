import random
#Chamander
p1 = "Charmander"
vida1 = 39
defesa1 = 43
dano1 = 52
#Squirtle
p2 = "Squirtle"
vida2 = 44
defesa2 = 65
dano2 = 48
#Bulbasaur
p3 = "Bulbasaur"
vida3 = 45
defesa3 = 49
dano3 = 49


#APRESENTAÇÃO E MENU INCIAL
pokemon = int(input("Bem vindo ao JOGO!!!\nEscolha seu Pókemon!\n1 - Charmander\n2 - Squirtle\n3 - Bulbasaur\n>> "))

if pokemon == 1:
    print(f"Você escolheu o {p1}")

elif pokemon == 2:
    print(f"Você escolheu o {p2}")

elif pokemon == 3:
    print(f"Você escolheu o {p3}")
else:
    while pokemon < 0 or pokemon > 3:
        pokemon = int(input("Escolha dentre as opções!!!\nEscolha seu Pókemon!\n1 - Charmander\n2 - Squirtle\n3 - Bulbasaur\n>> "))
        if pokemon == 1:
            print(f"Você escolheu o {p1}")

        elif pokemon == 2:
            print(f"Você escolheu o {p2}")

        elif pokemon == 3:
            print(f"Você escolheu o {p3}")
       
lista = (p1, p2, p3)
inimigo = random.choice(lista)
print(f"Seu inimigo será {inimigo}!")

#ESCOLHA DO OPONENTE