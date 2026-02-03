from fastapi import FastAPI
import uvicorn

app = FastAPI()

# Endpoint 1: Základní ověření funkčnosti
@app.get("/")
def home():
    return {"status": "Server běží", "lokace": "Codespaces"}

# Endpoint 2: Maturitní úloha - Faktoriál (Algoritmy)
@app.get("/faktorial/{cislo}")
def vypocet_faktorialu(cislo: int):
    vysledek = 1
    for i in range(1, cislo + 1):
        vysledek *= i
    return {"vstup": cislo, "faktorial": vysledek}

# Endpoint 3: Ukázka práce s daty
@app.post("/scitani")
def secti(a: int, b: int):
    return {"vysledek": a + b}

# Toto umožní spuštění přímo přes Python (volitelné)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)