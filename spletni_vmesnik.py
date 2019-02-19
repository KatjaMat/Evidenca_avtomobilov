from bottle import get,run,template
import modeli

@get('/')
def glavna_stran():
    stevilo_avtov = modeli.koliko_vseh_avtov()
    return template('glavna_stran',
                     avti = stevilo_avtov)

run(reloader=True,debug=True)