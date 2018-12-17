
import sqlite3

conn = sqlite3.connect('Evidenca_avtomobilov.db')
conn.execute("PRAGMA foreign_keys = ON")

def commit(fun):
    """
    Dekorator, ki ustvari kurzor, ga poda dekorirani funkciji,
    in nato zapiše spremembe v bazo.
    Originalna funkcija je na voljo pod atributom nocommit.
    """
    def funkcija(*largs, **kwargs):
        ret = fun(conn.cursor(), *largs, **kwargs)
        conn.commit()
        return ret
    funkcija.__doc__ = fun.__doc__
    funkcija.__name__ = fun.__name__
    funkcija.__qualname__ = fun.__qualname__
    fun.__qualname__ += '.nocommit'
    funkcija.nocommit = fun
    return funkcija

def koliko_avtov():
    """
    Vrne stevilo avtov.
    >>> koliko_avtov()
    35
    """
    poizvedba = """
        SELECT COUNT(*)
        FROM vozilo
    """
    st, = conn.execute(poizvedba).fetchone()
    return st

def podatki_vozil(vnos):
    """
    Vrne podatke o vozilih.
    """
    poizvedba = """
        SELECT stevilka_sasije, letnik, barva, gorivo
        FROM vozilo
        WHERE stevilka_sasije = vnos
    """
    return conn.execute(poizvedba).fetchall()

def poisci_vozilo(ime_vnos):
    """
    Poišče vsa vozila iste znamke.
    """
    poizvedba = """
        SELECT stevilka_sasije, letnik, barva, gorivo
        FROM vozilo
        WHERE stevilka_sasije = (SELECT ID FROM model WHERE znamka = ime_vnos)
    """
    return conn.execute(poizvedba, ['%' + ime_vnos + '%']).fetchall()

def znamke_podjetja(ime_podjetja):
    """
    Poišče vse znamke, ki jih določeno podjetje dobavlja
    """
    poizvedba = """
       SELECT znamka 
       FROM model 
       WHERE ime_podjetja = (SELECT ime FROM podjetje)
       """
    return conn.execute(poizvedba).fetchall()