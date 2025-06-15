"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Ivo Dolezal
email: ivousd@seznam.cz
"""
# --
# naimportujeme knihovnu
import random

oddelovac = "-" * 47
# --
# generování PIN - fce
def generuj_tajne_cislo():
    cifry = random.sample("123456789", 1) + random.sample("0123456789", 3)
    while len(set(cifry)) != 4:
        cifry = random.sample("123456789", 1) + random.sample("0123456789", 3)
    return ''.join(cifry)
# --
# kontrola tipu playera
def je_spravne_cislo(tip):
     return (
          len(tip) == 4 and
          tip.isdigit() and
          len(set(tip)) ==  len(tip) and
          tip [0] != '0'
     )


print("Ahoj.")
print(oddelovac)
print("Vítej v programu hádání tajného čísla.")
print("HÁDEJ ČTYŘ-místné ČÍSLA: JE TO SKORO JAKO HÁDAT PIN OD TELEFONU.")
print("Jsou to čtyři číslice (cifry).A neopakují se." \
"VYBÍREJ Z ČÍSEL 'jedna až děvět' -> jsou to čísla 1, 2, 3, 4, 5, 6, 7, 8, 9." \
"A bacha, nula se tam nepoužije")
print(oddelovac)




print("Právě je vygenerováno číslo, které máš hádat.")

#
print(oddelovac)
# --
# pocitani tipu byku a krav
def spocitat_tip(tip, tajne_cislo):
    bulls = 0
    cows = 0
    for i in range(4):
        if tip[i] == tajne_cislo[i]:
            bulls += 1
        elif tip[i] in tajne_cislo:
            cows += 1
    return bulls, cows

# vysledek pocitani
def vysledek_hrani(bulls, cows):
    return (
        f"{bulls} {'býk' if bulls == 1 else 'býci'} "
        f"{cows} {'kráva' if cows == 1 else 'krávy'}"
    )

# hlavní hra
def hlavni_hra():
    print("Ahoj!")
    print(oddelovac)
    print("Vítej v aplikaci na hádání tajného čísla/PINu. 😉")
    print("HÁDEJ ČTYŘ-místné ČÍSLO: JE TO SKORO JAKO HÁDAT PIN OD TELEFONU.")
    print("Akorát má to pravidla:\
          První cifra není 0 (nula)\
          Další mohou být 0 (nula)\
          Pokuk uhádneš - uloží se ti správný tip. A hádej dál, dokud neuhodneš všechny.")
    print("A jedem. Hra začíná.")
    print(oddelovac)
    tajne_cislo = generuj_tajne_cislo()
    pokus = 0
    while True:
        tip = input("Zadej svůj tip: ").strip()
        # kontrola tipu
        if je_spravne_cislo(tip):

