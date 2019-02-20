from bottle import get,run,template
import modeli

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


run(reloader=True,debug=True)