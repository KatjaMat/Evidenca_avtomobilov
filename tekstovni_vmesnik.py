import modeli
def izberi_moznost(moznosti):
    """
    Funkcija, ki izpiše seznam možnosti in vrne indeks izbrane možnosti
    Če na voljo ni nobene možnosti, izpiše opozorilo in vrne None
    Če je na voljo samo ena možnost, vrne 0
    >>> izberi_moznost(['A','B,'C'])
    1)A
    2)B
    3)C
    Vnesite izbiro: 2
    1 #indeks
    """

    if len(moznosti) == 0:
        return None
    elif len(moznosti) == 1:
        return 0
    else:
        for i, moznost in enumerate(moznosti, 1):
            print('{}){}'.format(i,moznost))
        st_moznosti = len(moznosti)
        while True:
            izbira = input("Vnesite izbiro: ")
            if not izbira.isdigit():
                print("NAPAKA: vnesti morate število")
            else:
                n = int(izbira)
                if 1 <= n <= st_moznosti:
                    return n-1
                else:
                    print("NAPAKA: vnesti morate število med 1 in {}!".format(st_moznosti))

def prikazi_podatke_vozilih():
    """
    Prikaže podatke o določenih vozilih. Če podatka ni v bazi, izpiše napako.
    """
    ime = input("Vnesi številko šasije vozila: ")
    while not modeli.podatki_vozil(ime):
        ime = input("Vozilo s to stevilko sasije ne obstaja. Vnesi veljavno stevilko:")
    else:
        podatki = list(modeli.podatki_vozil(ime))
    print(podatki)
    print("\nLetnik: {0}, Barva: {1}, Gorivo: {2}, Oseba: {3}, Model: {4}\n".format(*podatki))

def pokazi_moznosti(moznosti):
    print(50 * '-')
    izbira = izberi_moznost([
        'prikaži podatke o določenih vozilih',
        'vozila na zalogi',
        'dano podjetje dobavlja ta vozila',
        'izhod',
    ])
    if izbira == 0:
        prikazi_podatke_vozilih()
        nazaj()
    elif izbira == 1:
        prikazi_vozila_na_zalogi()
        nazaj()
    elif izbira == 2:
        podjetje()
        nazaj()
    else:
        print('Do naslednjič!')
        exit()


def podjetje():
    """
    Prikaže znamke vozil, ki jih neko podjetje dobavlja.
    """
    ime_podjetja = input("Vnesi ime podjetja: ")

    podatki = modeli.znamke_podjetja(ime_podjetja)    
    for podatek in podatki:
        print("Podjetje dobavlja znamko: {}".format(list(podatek)[0]))




def prikazi_vozila_na_zalogi():
    """
    Funkcija prešteje vozila
    """
    return modeli.koliko_avtov()



def nazaj():
    """
    Funkcija naredi, da se po uporabnikovi uspešni poizvedbi ne vrnemo takoj na poizvedovanje
    """
    st = False
    while not st:
        st = input('Za nazaj napisi "True":')

def main():
    print('Pozdravljeni v bazi vozil!')
    moznosti = "" #########nekaj napisi
    while True:
        pokazi_moznosti(moznosti)

main()