
import sqlite3
import baza


conn = sqlite3.connect('Evidenca_avtomobilov.db')
baza.ustvari_bazo_ce_ne_obstaja(conn)
conn.execute("PRAGMA foreign_keys = ON")

def znamke():
    '''vrne vse znamke avtomobilov'''
    poizvedba = """
    SELECT DISTINCT znamka
    FROM model
    ORDER BY znamka
    """
    znamka = conn.execute(poizvedba).fetchall()
    return znamka

def znamke_avtomobilov(znamka):
    '''vrne vse avtomobile iste znamke'''
    poizvedba = """
        SELECT model, oblika, letnik, barva, gorivo
        FROM vozilo
        JOIN model ON (model.id = vozilo.model)
        WHERE znamka = ?
        ORDER BY letnik DESC"""
    znamke = conn.execute(poizvedba, [znamka]).fetchall()
    return znamka, znamke

def mozna_leta():
    '''vrne vse letnike avtomobilov'''
    poizvedba = """
    SELECT DISTINCT letnik
    FROM vozilo
    ORDER BY letnik ASC
    """
    leta = conn.execute(poizvedba).fetchall()
    return leta
def letnice_avtomobilov(letnik):
    '''vrne vse avtomobile istega letnika'''
    poizvedba = """
        SELECT znamka, model, oblika, letnik, barva, gorivo
        FROM vozilo
        JOIN model ON (model.id = vozilo.model)
        WHERE letnik = ?
        ORDER BY znamka, model DESC"""
    vozila = conn.execute(poizvedba, [letnik]).fetchall()
    return letnik, vozila

def koliko_vseh_avtov():
    poizvedba = """
        SELECT COUNT(*)
        FROM vozilo
    """
    koliko_vseh_avtov, = conn.execute(poizvedba).fetchone()
    return koliko_vseh_avtov

def koliko_avtov(vnos):
    """
    Vrne stevilo avtov.
    >>> koliko_avtov('plin')
    35
    """
    poizvedba = """
        SELECT COUNT(*)
        FROM vozilo
        WHERE gorivo = ?
    """
    return conn.execute(poizvedba, [vnos]).fetchone()[0]
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

def seznam_oblik():
    poizvedba = """
        SELECT DISTINCT oblika FROM model
        ORDER BY oblika
    """
    return conn.execute(poizvedba).fetchall()


def seznam_barv():
    poizvedba = """
        SELECT DISTINCT barva FROM vozilo
        ORDER BY barva
    """
    return conn.execute(poizvedba).fetchall()

def seznam_goriv():
    poizvedba = """
        SELECT DISTINCT gorivo FROM vozilo
        ORDER BY gorivo
    """
    return conn.execute(poizvedba).fetchall()

def dodaj_vozilo(stevilka_sasije, letnik, oseba, model, znamka, barva, gorivo, oblika):
    """
    V bazo doda vozilo ter podatke njegove podatke
    """
    with conn:
        id = conn.execute("""
            INSERT INTO vozilo (stevilka_sasije, letnik, barva, gorivo,
                            oseba, model)
                            VALUES (?, ?, ?, ?, ?, ?)
        """, [stevilka_sasije, letnik, barva, gorivo, oseba, model]).lastrowid
        conn.execute("INSERT INTO model (oblika,znamka) VALUES (?, ?)",
                         [oblika, znamka])
        return id

def podatki_vozila(stevilka_sasije):
    """Vrne vse podatke vozila z dano stevilko sasije"""
    poizvedba = """
    SELECT znamka, letnik, barva, gorivo, oseba, model
    FROM vozilo
    JOIN model on (model.id = vozilo.model)
    WHERE stevilka_sasije = ?                 
    """
    cur = conn.cursor()
    cur.execute(poizvedba, [stevilka_sasije])
    osnovni_podatki = cur.fetchone()
    if osnovni_podatki is None:
        return None
    else:
        znamka, letnik, barva, gorivo, oseba, model = osnovni_podatki
        return znamka, letnik, barva, gorivo, oseba, model
    