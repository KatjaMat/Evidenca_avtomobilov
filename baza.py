import csv
from modeli import conn, commit


def pobrisi_tabele(conn):
    """
    Pobriše tabele iz baze.
    """
    conn.execute("DROP TABLE IF EXISTS dobavlja;")
    conn.execute("DROP TABLE IF EXISTS kupi;")
    conn.execute("DROP TABLE IF EXISTS oseba;")
    conn.execute("DROP TABLE IF EXISTS vozilo;")
    conn.execute("DROP TABLE IF EXISTS model;")
    conn.execute("DROP TABLE IF EXISTS podjetje;")



def ustvari_tabele(conn):
    """
    Ustvari tabele v bazi.
    """
    conn.execute("""
        CREATE TABLE oseba (
            id        INTEGER PRIMARY KEY,
            ime       TEXT,
            priimek   TEXT,
            naslov    TEXT,
            telefon   INTEGER,
            emšo      INTEGER,

        );
    """)

    conn.execute("""
        CREATE TABLE model (
            id    INTEGER PRIMARY KEY ,
            oblika TEXT,
            znamka TEXT
        );
    """)
    conn.execute("""
        CREATE TABLE vozilo (
            stevilka_sasije  INTEGER PRIMARY KEY,
            letnik TEXT,
            barva TEXT,
            gorivo TEXT,
            oseba INTEGER REFERENCES oseba(id),
            model INTEGER REFERENCES model(id) NOT NULL

        );
    """)

    conn.execute("""
        CREATE TABLE podjetje (
            id    INTEGER PRIMARY KEY ,
            ime TEXT,
            telefon INTEGER,
            naslov TEXT,
            email TEXT
        );
    """)
    conn.execute("""
        CREATE TABLE dobavlja (
            podjetje  INTEGER REFERENCES podjetje(id),
            model INTEGER REFERENCES model(id),
            PRIMARY KEY (podjetje, model)
        );
    """)

#    conn.execute("""
#        CREATE TABLE kupi (
#           oseba INTEGER REFERENCES oseba(id),
#          vozilo INTEGER REFERENCES vozilo(stevilka_sasije),
#         PRIMARY KEY (oseba, vozilo)
#    );
#""")

def uvozi_podjetja(conn):
    """
    Uvozi podatke o podjetjih.
    """
    conn.execute("DELETE FROM podjetje;")
    with open('podatki/podjetje.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO podjetje VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)


def uvozi_osebe(conn):
    """
    Uvozi podatke o osebah.
    """
    conn.execute("DELETE FROM oseba;")
    with open('podatki/oseba.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO oseba VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)


def uvozi_vozila(conn):
    """
    Uvozi podatke o vozilih.
    """
    conn.execute("DELETE FROM kupi;")
    conn.execute("DELETE FROM vozila;")
    vozila = {}
    with open('podatki/vozila.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        v = stolpci.index('vozila')
        poizvedba = """
            INSERT INTO nastopa VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        poizvedba_vozila = "INSERT INTO vozila (naziv) VALUES (?);"
        for vrstica in podatki:
            vozila = vrstica[v]
            if vozila not in vozila:
                conn.execute(poizvedba_vozila, [vozila])
                vozila[vozila] = conn.lastrowid
            vrstica[v] = vozila[vozila]
            conn.execute(poizvedba, vrstica)


def uvozi_modele(conn):
    """
    Uvozi podatke o žanrih.
    """
    conn.execute("DELETE FROM dobavlja;")
    conn.execute("DELETE FROM model;")
    modeli = {}
    with open('podatki/model.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        z = stolpci.index('model')
        poizvedba = """
            INSERT INTO pripada VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        poizvedba_model = "INSERT INTO model (naziv) VALUES (?);"
        for vrstica in podatki:
            model = vrstica[z]
            if model not in modeli:
                conn.execute(poizvedba_model, [model])
                model[model] = conn.lastrowid
            vrstica[z] = model[model]
            conn.execute(poizvedba, vrstica)


def ustvari_bazo(conn):
    """
    Opravi celoten postopek postavitve baze.
    """
    pobrisi_tabele(conn)
    ustvari_tabele(conn)
    uvozi_osebe(conn)
    uvozi_podjetja(conn)
    uvozi_vozila(conn)
    uvozi_modele(conn)

def ustvari_bazo_ce_ne_obstaja(conn):
    """
    Ustvari bazo, če ta še ne obstaja.
    """
    with conn:
        cur = conn.execute("SELECT COUNT(*) FROM sqlite_master")
        if cur.fetchone() == (0, ):
            ustvari_bazo(conn)