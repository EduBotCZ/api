from fastapi import FastAPI
# Importujeme naše vyřešené funkce z vedlejšího souboru
from maturita_lib import analyzuj_rc, validuj_heslo, vlastni_max

app = FastAPI()

# 1. Endpoint pro validaci a analýzu rodného čísla (Maturitní okruh 20)
@app.get("/tools/validator-rc/{rc}")
def validator_rc(rc: str):
    """
    Přijme rodné číslo, ověří jeho základní délku a 
    vrátí extrahované datum narození a pohlaví.
    """
    if len(rc) != 10:
        return {"chyba": "Neplatný formát, očekáváno YYMMDDXXXX"}
    
    # Využití logiky z naší knihovny
    analyza = analyzuj_rc(rc)
    
    return {
        "rc": rc,
        "validni_delka": True,
        "datum_narozeni": analyza["datum_narozeni"],
        "pohlavi": analyza["pohlavi"]
    }

# 2. Endpoint pro ověření síly hesla (Maturitní okruh 12)
@app.get("/tools/validator-hesla/{heslo}")
def zkontroluj_heslo(heslo: str):
    """
    Vrátí JSON s informací, zda heslo splňuje naše bezpečnostní požadavky.
    """
    je_bezpecne = validuj_heslo(heslo)
    return {
        "heslo": heslo,
        "je_bezpecne": je_bezpecne
    }

# 3. Endpoint pro hledání maxima v poli čísel (Maturitní okruh 6 a 7)
@app.post("/tools/najdi-maximum")
def najdi_maximum(cisla: list[int]):
    """
    Přijme JSON pole s čísly (POST metoda) a vrátí největší z nich 
    pomocí naší vlastní implementace vyhledávání.
    """
    maximum = vlastni_max(cisla)
    return {
        "zadana_cisla": cisla,
        "nejvetsi_cislo": maximum
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
