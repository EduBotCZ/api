# ==========================================
# SADA A: Algoritmy a cykly (Okruhy 6 a 7)
# ==========================================

def vlastni_max(pole: list) -> int:
    """Najde největší číslo v poli bez použití vestavěné funkce max()."""
    if not pole:
        return None
    nejvetsi = pole[0]
    for cislo in pole:
        if cislo > nejvetsi:
            nejvetsi = cislo
    return nejvetsi

def pocet_vyskytu(text: str, znak: str) -> int:
    """Vrátí počet výskytů konkrétního znaku v textu."""
    pocet = 0
    for z in text:
        if z == znak:
            pocet += 1
    return pocet

# ==========================================
# SADA B: Validace řetězců (Okruhy 12 a 20)
# ==========================================

def validuj_heslo(heslo: str) -> bool:
    """
    Ověří, zda má heslo alespoň 8 znaků, obsahuje číslo a velké písmeno.
    """
    if len(heslo) < 8:
        return False
    
    obsahuje_cislo = False
    obsahuje_velke = False
    
    for znak in heslo:
        if znak.isdigit():
            obsahuje_cislo = True
        if znak.isupper():
            obsahuje_velke = True
            
    return obsahuje_cislo and obsahuje_velke

def analyzuj_rc(rc: str) -> dict:
    """Extrahuje datum narození a pohlaví z rodného čísla ve formátu YYMMDD/XXXX."""
    # Poznámka: Konkrétní parsování řetězce (slicing) a konverze je standardní postup v Pythonu.
    rok = rc[0:2]
    mesic = int(rc[2:4])
    den = rc[4:6]
    
    if mesic > 50:
        pohlavi = "Žena"
        mesic_upraveny = mesic - 50
    else:
        pohlavi = "Muž"
        mesic_upraveny = mesic
        
    return {
        "datum_narozeni": f"{den}. {mesic_upraveny:02d}. 19{rok}", 
        "pohlavi": pohlavi
    }

# ==========================================
# SADA C: Objektově orientované programování (Okruhy 3, 11 a 13)
# ==========================================

class Fronta:
    """Simulace fronty (First In, First Out) bez použití pop(0)."""
    def __init__(self):
        self.polozky = []
        
    def push(self, polozka):
        self.polozky.append(polozka)
        
    def pop(self):
        if not self.polozky:
            return None
        prvni = self.polozky
        # Poradíme si s indexy přes tzv. slicing, místo zakázaného pop(0)
        self.polozky = self.polozky[1:] 
        return prvni

class Uzivatel:
    """Rodičovská třída pro ukázku dědičnosti a magických metod."""
    def __init__(self, jmeno: str, email: str):
        self.jmeno = jmeno
        self.email = email
        
    def __str__(self):
        return f"Uživatel {self.jmeno} ({self.email})"

class Admin(Uzivatel):
    """Potomek třídy Uzivatel s přidanými právy."""
    def __init__(self, jmeno: str, email: str, prava: list):
        super().__init__(jmeno, email) # Volání konstruktoru rodiče
        self.prava = prava
        
    def __str__(self):
        return f"Administrátor {self.jmeno} s právy: {', '.join(self.prava)}"

class Ucet:
    """Třída demonstrující zapouzdření (private atributy) a metody."""
    def __init__(self, majitel: str):
        self.majitel = majitel
        self._zustatek = 0 # Protected atribut - nesmí se upravovat zvenčí napřímo
        
    def vklad(self, castka: float):
        if castka > 0:
            self._zustatek += castka
            
    def vyber(self, castka: float) -> bool:
        if castka <= self._zustatek:
            self._zustatek -= castka
            return True
        return False
        
    def generuj_iban(self) -> str:
        """Vygeneruje zjednodušený formát účtu (IBAN)."""
        # Poznámka: Hashování majitele je zvoleno čistě pro generování fixních čísel pro ukázku.
        cislo_uctu = abs(hash(self.majitel)) % 1000000000
        return f"CZ0000000000{cislo_uctu:010d}"
        
    def __str__(self):
        return f"Účet majitele {self.majitel}, stav: {self._zustatek} Kč"