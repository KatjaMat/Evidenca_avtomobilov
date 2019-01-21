
import sqlite3
import baza


conn = sqlite3.connect('Evidenca_avtomobilov.db')
baza.ustvari_bazo_ce_ne_obstaja(conn)
conn.execute("PRAGMA foreign_keys = ON")

def koliko_avtov(vnos):
    """
    Vrne stevilo avtov.
    >>> koliko_avtov('plin')
    35
    """
    poizvedba = """
        SELECT COUNT(*)
        FROM vozilo
        WHERE gorivo = vnos
    """
    return conn.execute(poizvedba, [vnos]).fetchall()
#
def podatki_vozil(vnos):
    """
    Vrne podatke o vozilih.
    """
    poizvedba = """
        SELECT letnik, barva, gorivo, oseba, model
        FROM vozilo
        WHERE stevilka_sasije = ?
    """
    return conn.execute(poizvedba).fetchone()
#
def poisci_vozilo(ime_vnos):
    """
    Poišče vsa vozila iste znamke.
    """
    poizvedba = """
        SELECT stevilka_sasije, letnik, barva, gorivo, oseba, model
        FROM vozilo
        WHERE stevilka_sasije = (SELECT ID FROM model WHERE znamka = ime_vnos)
    """
    return conn.execute(poizvedba, ['%' + ime_vnos + '%']).fetchall()

def znamke_podjetja(ime_podjetja):
    """
    Poišče vse znamke, ki jih določeno podjetje dobavlja
    """
    poizvedba = """SELECT znamka
    FROM dobavlja JOIN podjetje ON dobavlja.idpodjetja = id
    WHERE ime LIKE ?
    """
    #"""
    #   SELECT znamka 
    #   FROM model JOIN dobavlja ON model.id = model
    #   JOIN podjetje ON podjetje = podjetje.id
    #   WHERE ime LIKE ?
    #"""
    return [znamka for znamka, in conn.execute(poizvedba,['%' + ime_podjetja + '%']).fetchall()]