import random
from typing import Tuple

# Naimportujeme knihovny
'''
    main.py: druhý projekt do Engeto Online Python Akademie
    author: Ivo Dolezal
    email: ivousd@seznam.cz

    Hra: Bulls and Cows (Býci a Krávy) - česká verze
    Hra, kde hráč hádá čtyřciferné unikátní číslo (PIN).
    Býci jsou správné tipy ne správném místě, krávy jsou správné tipy na špatném místě.
    Hráč zadává tipy, program vyhodnocuje počet správných číslic na správném a špatném místě.
    Hra končí, když hráč uhodne všechna čtyři čísla.
'''

# Konstanty
VERSION = "1.0.5"
AUTOR = "IVO DOLEZAL"
EMAIL = "MAILITO:IVOUSD@GMAIL.COM"
# Separátor pro oddělení částí výstupu
ODDELOVAC = "-" * 47

# Vygeneruje čtyřciferné unikátní číslo, první cifra není nula. Tzv. PIN - fce
def generuj_tajne_cislo() -> str:
    prvni = random.choice("123456789")
    ostatni = random.sample("0123456789".replace(prvni, ""), 3)
    return prvni + "".join(ostatni)

# Kontrola tipu playera (Správný formát)
def je_spravne_cislo(tip: str) -> bool:
     return (
          len(tip) == 4
          and tip.isdigit()
          and tip[0] != '0'
          and len(set(tip)) == 4
     )  #True, pokud je formát správný, jinak False.

# Zpráva: Co za chybu? Vysvětlí co nesedí
def ziskej_chybovou_zpravu(tip: str) -> str:
    if len(tip) != 4:
        return "Musíš zadat přesně čtyři číslice!"
    if not tip.isdigit():
        return "Zadej pouze číslice 0-9!"
    if tip[0] == "0":
        return "První cifra nesmí být nula!"
    if len(set(tip)) != 4:
        return "Číslice se nesmí opakovat!"
    return "Neplatný vstup!"

# Počítání tipu
def spocitej_bulls_cows(tip: str, tajne_cislo: str) -> Tuple[int, int]:
    bulls = sum(t == s for t, s in zip(tip, tajne_cislo))
    cows = sum(c in tajne_cislo for c in tip) - bulls
    return bulls, cows

# Výsledek počítání - deklinace (český jazyk)
def formatuj_vysledek(bulls: int, cows: int) -> str:
    # Správný formát býka
    if bulls == 1:
        byk_txt = "býk"
    elif 1 < bulls < 5:
        byk_txt = "býci"
    else:
        byk_txt = "býků"

    # Správný formát krávy
    if cows == 1:
        krava_txt = "kráva"
    elif 1 < cows < 5:
        krava_txt = "krávy"
    else:
        krava_txt = "krav"
    return f"{bulls} {byk_txt}, {cows} {krava_txt}"

# Hra - Úvod do hry a pravidla
def vypis_uvod() -> None:
    print(
       f"Ahoj.\n{ODDELOVAC}\n"
        "👋 Vítej v programu na hádání tajného čísla.\n"
        "Možná to znáš jako hru Bulls & Cows. Tady je CZ verze.\n"
        "'Býk' → správná číslice na správném místě.\n"
        "'Kráva' → správná číslice na špatném místě.\n"
        "Hádej čtyřciferné číslo (0–9),\nčíslice se neopakují\na první není nula.\n"
        f"{ODDELOVAC}\n"
        "Tajné číslo je vygenerováno, začni hádat!\n"
        f"{ODDELOVAC}"
    )

# Hlavní hra
def hraj_hru() -> None:
    vypis_uvod()
    tajne_cislo = generuj_tajne_cislo() 
    pokus = 0

    # Dokud neuhádne všechy čtyři, jede smyčka
    while True:
        tip = input("Zadej svůj tip (nebo napiš 'exit' pro ukončení): ").strip()
        if tip.lower() == 'exit':
            print(f"{ODDELOVAC}\nDěkujeme za hru, ahoj! 👋\n{ODDELOVAC}")
            break
        
        if not je_spravne_cislo(tip):
            print(f"Chyba: {ziskej_chybovou_zpravu(tip)}\n{ODDELOVAC}")
            continue

        pokus += 1
        bulls, cows = spocitej_bulls_cows(tip, tajne_cislo)
        print(f"{ODDELOVAC}\n{formatuj_vysledek(bulls, cows)}\n{ODDELOVAC}")
        
        if bulls == 4:
            print(
                f"✅ Správně! Tajný PIN neboli číslo -> jsi právě uhádl. 'Gratulky 🎉'\n"
                f"Je to: {tajne_cislo} (🐂🐂🐂🐂)"
            )
            print(f"Počet pokusů: {pokus}")
            break

            print(f"{ODDELOVAC}\nDěkujeme za hru, ahoj! 👋\n{ODDELOVAC}")

if __name__ == "__main__":
    hraj_hru()
