from bottle import get,run,template
import modeli

@get('/letniki-vozil/')
@get('/letniki-vozil/<leto:int>/')
def letniki_vozil(leto=2000):
    leto, avtomobili_z_letnicami = modeli.letnice_avtomobilov(leto)
    return template('letniki_vozil',
                     leto = leto, avti = avtomobili_z_letnicami,)

@get('/')
def osnovna_stran():
    leta = modeli.mozna_leta()
    nova = []
    for i in range(len(leta)):
        leta[i] = leta[i][0]
    return template('osnovna_stran',
                     leta = leta,)
run(reloader=True,debug=True)