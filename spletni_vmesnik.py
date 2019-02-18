from bottle import get,run,template
import modeli

@get('/')
def glavna_stran():
    return template('glavna_stran')

run(reloader=True,debug=True)