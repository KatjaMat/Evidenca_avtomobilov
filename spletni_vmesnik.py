from bottle import get, template, run
import modeli

@get('/')
def glavna_stran():
    return template('glavna_stran',
    stevilo_avtov = modeli.koliko_vseh_avtov()
    )

run(reloader=True,debug=True)