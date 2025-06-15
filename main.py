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
          tip [0] != '0' and
          all(cif in '0123456789' for cif in tip)
     )
# --
# zprava co za chybu
def ziskej_chybovou_zpravu(tip):
    if len(tip) != 4:
        return "Musíš zadat přesně čtyři číslice!"
    if not tip.isdigit():
        return "Zadej pouze číslice 0-9!"
    if tip[0] == '0':
        return "První cifra nesmí být nula!"
    if len(set(tip)) != 4:
        return "Číslice se nesmí opakovat!"
    return "Neplatný vstup!"
# --
# pocitani tipu
def spocitat_tip(tip, tajne_cislo):
    bulls = 0
    cows = 0
    bulls = sum(tip_cislo == tajne_cislo_cifra for tip_cislo, tajne_cislo_cifra in zip(tip, tajne_cislo))
    cows = sum(tip_cislo in tajne_cislo for tip_cislo in tip) - bulls
    return bulls, cows
# --
# vysledek pocitani
def vysledek_hrani(bulls, cows):
    return (
        f"{bulls} {'býk' if bulls == 1 else 'býci' if bulls != 0 else 'býků'}, " 
        f"{cows} {'kráva' if cows == 1 else 'krávy' if cows !=0 else 'krav'}"
    )
# --
# hra
def hlavni_hra():
    print("Ahoj.")
    print(oddelovac)
    print("👋 Vítej v programu na hádání tajného čísla.")
    print("Možná to znáš jako hru Bulls & Cows. ale tady je česká verze. 🐂 & 🐄 .cz ")
    print("'Bejk' -> Správná číslice na správném místě.\n'Kravička' -> Správná číslice na špatném místě.")
    print("HÁDÁŠ ČÍSLO,...\nJE TO SKORO JAKO HÁDAT PIN NA TELEFONU.😉 ")
    print("Jsou to čtyři číslice ('cifry').A neopakují se.\nVYBÍRÁŠ Z ČÍSEL 'JEDNA' až 'DEVĚT'")
    print("Jsou to čísla 1, 2, 3, 4, 5, 6, 7, 8, 9.")
    print("A bacha, nula se tam nesmí použít jako první cifra, jinak druhá až čtvrtá cifra ano.")
    print(oddelovac)
    print("Právě se vygenerováno číslo, které máš hádat.")
    print(oddelovac)

    tajne_cislo = generuj_tajne_cislo()
    pokus = 0

    while True:
        tip = input("Zadej svůj tip: ").strip()
        pokus += 1

        # kontrola tipu   
        if not je_spravne_cislo(tip):
            print(f"Chyba: {ziskej_chybovou_zpravu(tip)}")
            print(oddelovac)
            continue


        bulls, cows = spocitat_tip(tip, tajne_cislo)
        print(f"{oddelovac}\n{vysledek_hrani(bulls, cows)}\n{oddelovac}")

        if bulls == 4:
            print(f"✅ Správně! Tajný PIN jsi právě uhádl.\nJe to: {tajne_cislo}")
            print(f"Počet pokusů: {pokus}")
            break

if __name__ == "__main__":
    hlavni_hra()
