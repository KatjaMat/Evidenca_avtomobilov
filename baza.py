import csv
from modeli import conn, commit

@commit
def pobrisi_tabele(cur):
    """
    Pobriše tabele iz baze.
    """
    cur.execute("DROP TABLE IF EXISTS pripada;")
    cur.execute("DROP TABLE IF EXISTS nastopa;")
    cur.execute("DROP TABLE IF EXISTS zanr;")
    cur.execute("DROP TABLE IF EXISTS vloga;")
    cur.execute("DROP TABLE IF EXISTS oseba;")
    cur.execute("DROP TABLE IF EXISTS film;")

@commit
def ustvari_tabele(cur):
    """
    Ustvari tabele v bazi.
    """
    cur.execute("""
        CREATE TABLE oseba (
            id        INTEGER PRIMARY KEY,
            ime       TEXT,
            priimek   TEXT,
            naslov    TEXT,
            telefon   INTEGER,
            emšo      INTEGER,

        );
    """)
    cur.execute("""
        CREATE TABLE vozilo (
            številka šasije  INTEGER PRIMARY KEY,
            letnik TEXT,
            barva TEXT,
            gorivo TEXT
        );
    """)
    cur.execute("""
        CREATE TABLE model (
            id    INTEGER PRIMARY KEY ,
            oblika TEXT,
            znamka TEXT
        );
    """)
    cur.execute("""
        CREATE TABLE podjetje (
            id    INTEGER PRIMARY KEY ,
            ime TEXT,
            telefon INTEGER,
            naslov TEXT,
            email TEXT
        );
    """)
    cur.execute("""
        CREATE TABLE dobavlja (
            podjetje  INTEGER REFERENCES podjetje(id),
            model INTEGER REFERENCES model(id),
            PRIMARY KEY (podjetje, model)
        );
    """)
    cur.execute("""
        CREATE TABLE kupi (
            oseba INTEGER REFERENCES oseba(id),
            vozilo INTEGER REFERENCES vozilo(številka šasije),
            PRIMARY KEY (oseba, vozilo)
        );
    """)

@commit
def uvozi_filme(cur):
    """
    Uvozi podatke o filmih.
    """
    cur.execute("DELETE FROM film;")
    with open('podatki/film.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO film VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            cur.execute(poizvedba, vrstica)

@commit
def uvozi_osebe(cur):
    """
    Uvozi podatke o osebah.
    """
    cur.execute("DELETE FROM oseba;")
    with open('podatki/oseba.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO oseba VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            cur.execute(poizvedba, vrstica)

@commit
def uvozi_vloge(cur):
    """
    Uvozi podatke o vlogah.
    """
    cur.execute("DELETE FROM nastopa;")
    cur.execute("DELETE FROM vloga;")
    vloge = {}
    with open('podatki/vloge.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        v = stolpci.index('vloga')
        poizvedba = """
            INSERT INTO nastopa VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        poizvedba_vloga = "INSERT INTO vloga (naziv) VALUES (?);"
        for vrstica in podatki:
            vloga = vrstica[v]
            if vloga not in vloge:
                cur.execute(poizvedba_vloga, [vloga])
                vloge[vloga] = cur.lastrowid
            vrstica[v] = vloge[vloga]
            cur.execute(poizvedba, vrstica)

@commit
def uvozi_zanre(cur):
    """
    Uvozi podatke o žanrih.
    """
    cur.execute("DELETE FROM pripada;")
    cur.execute("DELETE FROM zanr;")
    zanri = {}
    with open('podatki/zanri.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        z = stolpci.index('zanr')
        poizvedba = """
            INSERT INTO pripada VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        poizvedba_zanr = "INSERT INTO zanr (naziv) VALUES (?);"
        for vrstica in podatki:
            zanr = vrstica[z]
            if zanr not in zanri:
                cur.execute(poizvedba_zanr, [zanr])
                zanri[zanr] = cur.lastrowid
            vrstica[z] = zanri[zanr]
            cur.execute(poizvedba, vrstica)

@commit
def ustvari_bazo(cur):
    """
    Opravi celoten postopek postavitve baze.
    """
    pobrisi_tabele.nocommit(cur)
    ustvari_tabele.nocommit(cur)
    uvozi_filme.nocommit(cur)
    uvozi_osebe.nocommit(cur)
    uvozi_vloge.nocommit(cur)
    uvozi_zanre.nocommit(cur)

def ustvari_bazo_ce_ne_obstaja():
    """
    Ustvari bazo, če ta še ne obstaja.
    """
    cur = conn.execute("SELECT COUNT(*) FROM sqlite_master")
    if cur.fetchone() == (0, ):
        ustvari_bazo(cur)