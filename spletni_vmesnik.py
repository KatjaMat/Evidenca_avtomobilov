from bottle import get, post, run, template, request, redirect
import modeli
import hashlib

@get('/')
def glavna_stran():
    return template('glavna_stran')

@get('/znamke-vozil/<niz>/')
def znamke_vozil(niz):
    niz, avtomobili_znamk = modeli.znamke_avtomobilov(niz)
    return template('znamka_vozilo', niz = niz, avtomobili_znamk = avtomobili_znamk)

@get('/znamke-vozil/')
def znamke():
    avtomobili_znamk = modeli.znamke()
    for i in range(len(avtomobili_znamk)):
        avtomobili_znamk[i] = avtomobili_znamk[i][0]
    return template('znamke_vozil',
                     znamke = avtomobili_znamk)

@get('/letniki-vozil/')
def letniki():
    leta = modeli.mozna_leta()
    for i in range(len(leta)):
        leta[i] = leta[i][0]
    return template('letniki_vozil',
                     leta = leta,)

@get('/letniki-vozil/<leto:int>/')
def letniki_vozil(leto):
    leto, avtomobili_z_letnicami = modeli.letnice_avtomobilov(leto)
    return template('leto_vozilo',
                     leto = leto, avti = avtomobili_z_letnicami,)

@get('/letniki-vozil/<leto:int>/<podatki:int>/')
def podatki_lastnika(leto,podatki):
    podatki = modeli.podatki_osebe(podatki)
    return template('podatki_oseba',podatki = podatki, leto = leto)

@get('/znamke-vozil/<znamke>/<podatki:int>/')
def podatki_lastnika(znamke,podatki):
    podatki = modeli.podatki_osebe(podatki)
    return template('podatki_oseba',podatki = podatki, znamke = znamke)

# @get('/iskanje/')
# def iskanje():
#     niz = request.query.naslov
#     idji_vozil = modeli.poisci_vozila(niz)
#     vozila = [(stevilka_sasije, letnik, barva, gorivo, model, znamka, '/vozila/{}/'.format(stevilka_sasije)) for (stevilka_sasije, letnik, barva, gorivo, model, znamka) in modeli.podatki_vozil(stevilka_sasije)]
#     return template(
#         'rezultati_iskanja',
#         niz=niz,
#         vozila=vozila,
#     )

@get('/dodaj-vozilo/')
def dodaj_vozilo():
    oblika = modeli.seznam_oblik()
    barve = modeli.seznam_barv()
    gorivo = modeli.seznam_goriv()
    return template('dodaj_vozilo',
                    stevilka_sasije = "",
                    letnik = "",
                    oseba = "",
                    model = "",
                    znamka = "",
                    barva="",
                    gorivo="",
                    oblika="",
                    vse_oblike = oblika,
                    vse_barve = barve,
                    vsa_goriva = gorivo,
                    napaka=False)


@post('/dodaj-vozilo/')
def dodajanje_vozila():
    try:
        id = modeli.dodaj_vozilo(
                    stevilka_sasije = request.forms.stevilka_sasije,
                    letnik = request.forms.letnik,
                    oseba = request.forms.oseba,
                    model = request.forms.model,
                    znamka = request.forms.znamka,
                    barva=request.forms.barva,
                    gorivo=request.forms.gorivo,
                    oblika = request.forms.oblika)
    except:
        oblika = modeli.seznam_oblik()
        barve = modeli.seznam_barv()
        gorivo = modeli.seznam_goriv()
        return template('dodaj_vozilo',
                    stevilka_sasije = request.forms.stevilka_sasije,
                    letnik = request.forms.letnik,
                    oseba = request.forms.oseba,
                    znamka = request.forms.znamka,
                    model = request.forms.model,
                    oblika = request.forms.getall('oblika'),
                    barva=request.forms.getall('barva'),
                    gorivo=request.forms.getall('gorivo'),
                    vse_barve = barve,
                    vse_oblike = oblika,
                    vsa_goriva = gorivo,
                    napaka=True)
    redirect('/vozilo/{}/'.format(id))

@get('/vozilo/<stevilka_sasije:int>/')
def podatki_vozila(stevilka_sasije):
    znamka, letnik, barva, gorivo, oseba, model = modeli.podatki_vozila(stevilka_sasije)
    return template(
        'vozilo',
        znamka = znamka,
        letnik = letnik,
        barva = barva,
        gorivo = gorivo,
        oseba = oseba,
        model = model
    )



run(reloader=True,debug=True)