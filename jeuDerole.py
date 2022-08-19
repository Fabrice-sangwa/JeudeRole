from random import randint

symbolYou = '\U0001F603'
SymbolEnnemi= '\U0001F47A'

print("Jeu de Role\nVous: ", symbolYou, " \nL'ennemi: ", SymbolEnnemi)
vieEnnemi = VieYou = 50
nbPotion = 3 
while True:
    print("-"*40)
    reponse = input("Souhaitez-vous attaquer \U00002694 (1) ou utiliser une potion \U0001F34E (2) ?\n>")
    while reponse != "1" and reponse != "2":
        reponse = input("Souhaitez-vous attaquer \U00002694 (1) ou utiliser une potion \U0001F34E (2) ?\n>")
    if reponse == "1": 
        degatYou = randint(5,10)
        degatEnnemi = randint(5,15)
        vieEnnemi = vieEnnemi - degatYou
        VieYou = VieYou - degatEnnemi
        print(f"\U0001F603 Vous avez infligé à votre ennemi {degatYou} points de degat")
        print(f"\U0001F47A L'ennemi vous a infligé {degatEnnemi} points de degat")
        if VieYou <= 0 or vieEnnemi <=0:
            if VieYou <= 0:
                print("\U0001F47A L'ennemi vous avez mis chaos\nVous avez perdu!\n\U0001F62D Game over")
                break
            elif vieEnnemi <= 0 : 
                print("\U0001F603 Vous avez mis l'ennemi Chaos\n\U0001F973 Vous avez gagné")
                break
        elif vieEnnemi>0 and VieYou > 0: 
            print(f"\U0001F603 Il vous reste {VieYou} points de vie")
            print(f"\U0001F47A Il reste {vieEnnemi} points de vie à votre ennemi")
    elif reponse == "2" and VieYou > 0 and vieEnnemi > 0:
        if nbPotion > 0:
            potion = randint(15,50)
            nbPotion -=1
            print(f"\U0001F603 Vous avez recupéré {potion} points de vie")
            VieYou = VieYou + potion
            print(f"\U0001F603 Vous avez maintenant {VieYou} points de vie")
            print(f"\U0001F34E {nbPotion} Restantes")
            degatEnnemi = randint(5,15)
            VieYou = VieYou - degatEnnemi
            print(f"\U0001F47A L'ennemi vous a infligé {degatEnnemi} points de degat")
            print(f"\U0001F603 Il vous reste {VieYou} points de vie")
            print("\U0001F603 Vous passez votre tour.....")
            degatEnnemi = randint(5,15)
            VieYou = VieYou - degatEnnemi
            print(f"\U0001F47A L'ennemi vous a infligé {degatEnnemi} points de degat")
            print(f"\U0001F47A Il vous reste {VieYou} points de vie")
        else:
            print("Vous n'avez plus de potion")
