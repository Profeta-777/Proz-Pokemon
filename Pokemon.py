import random
#Pókemons
p1 = "Charmander"
p2 = "Squirtle"
p3 = "Bulbasaur"
#Ações Player
hp = 0
defs = 0
dmg = 0
#Ações Inimigas
hp2 = 0
defs2 = 0
dmg2 = 0
#Boas Vindas & Seleção de Pókemon
pokemon = int(input("Bem vindo a Batalha!!!\nEscolha seu Pókemon!\n1 - Charmander\n  Vida: 350\n  Defesa: 55\n  Ataque: 150\n\n2 - Squirtle\n  Vida: 400\n  Defesa: 75\n  Ataque: 125\n\n3 - Bulbasaur\n  Vida: 450\n  Defesa: 60\n  Ataque: 100\n>> "))

if pokemon == 1:
    print(f"Você escolheu o {p1}")
    hp = 350
    defs = 55
    dmg = 150

elif pokemon == 2:
    print(f"Você escolheu o {p2}")
    hp = 400
    defs = 75
    dmg = 125

elif pokemon == 3:
    print(f"Você escolheu o {p3}")
    hp = 450
    defs = 60
    dmg = 100
else:
    while pokemon < 0 or pokemon > 3:
        pokemon = int(input("Escolha dentre as opções!!!\nEscolha seu Pókemon!\n1 - Charmander\n2 - Squirtle\n3 - Bulbasaur\n>> "))
        if pokemon == 1:
            print(f"Você escolheu o {p1}")
            hp = 350
            defs = 55
            dmg = 150

        elif pokemon == 2:
            print(f"Você escolheu o {p2}")
            hp = 400
            defs = 75
            dmg = 125

        elif pokemon == 3:
            print(f"Você escolheu o {p3}")
            hp = 450
            defs = 60
            dmg = 100
            
#Seleção do Oponente
lista = (p1, p2, p3)
inimigo = random.choice(lista)
print(f"\n Seu inimigo será {inimigo}!")
if inimigo == p1:
    hp2 = 350
    defs2 = 55
    dmg2 = 150
elif inimigo == p2:
    hp2 = 400
    defs2 = 75
    dmg = 125
else:
    hp2 = 450
    defs2 = 60
    dmg2 = 100
    
#Ínicio da Batalha
print("\n ---- Batalha Iniciada ---- ")
while hp > 0 and hp2 > 0:
    print(f"\n Sua Vida: {hp} | Vida do Inimigo: {hp2}")
    act = int(input("1 - Atacar\n2 - Defender\n3 - Fugir\n>>"))
    act2 = random.randint(1,2)
    if act == 1:
        if act2 == 1:
            hp = hp - dmg2
            hp2 = hp2 - dmg
            print("Ambos atacaram e perderam vida!\n========================================")
        else:
            hp2 = hp2 - (dmg - defs2)
            print("O inimigo defendeu seu ataque!!\n========================================")
    elif act == 2:
        if act2 == 1:
            hp = hp - (dmg2 - defs)
            print("Você defendeu o ataque inimgo!!\n========================================")
        else:
            print("Ambos defenderam... Ninguém perdeu vida\n========================================")
    elif act == 3:
        break
    else:
        print("Selecione uma ação valida!!\n========================================")
if 0 == hp2:
    print(f"\nMeus parabéns! Você venceu a batalha!!\n Sua Vida {hp} | Vida do Inimgo {hp2}")
elif hp == 0:
    print(f"\nQue pena... Você perdeu a batalha!\n Sua Vida {hp} | Vida do Inimgo {hp2}")
elif hp < 0 and hp2 < 0:
    print(f"Incrivel!! Ambos empataram a Batalha!!!\n Sua Vida {hp} | Vida do Inimigo {hp2}")
else:
    print(f"\nVocê fugiu da batalha. Ninguém venceu!\n Sua Vida {hp} | Vida do Inimgo {hp2}")