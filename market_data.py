import yfinance as yf
import pandas as pd
from datetime import datetime

pd.set_option("display.max_columns", None)

ativos = {  
    "^BVSP": {
        "nome": "Ibovespa",
        "grupo": "Bolsas",
    },                                  # Brasil
    "^GSPC": {
        "nome": "S&P 500",
        "grupo": "Bolsas",
    },                                  # EUA
    "^GSPTSE": {
        "nome": "S&P/TSX",
        "grupo": "Bolsas"
    },                                 # Canadá
    "^FTSE": {
        "nome": "FTSE 100",
        "grupo": "Bolsas"
    },                                  # Reino Unido
    "^GDAXI": {
        "nome": "DAX",
        "grupo": "Bolsas"
    },                                  # Alemanha
    "^FCHI": {
        "nome": "CAC 40",
        "grupo": "Bolsas"
    },                                  # França
    "FTSEMIB.MI": {
        "nome": "FTSE MIB",
        "grupo": "Bolsas"
    },                                  # Itália
    "^N225": {
        "nome": "Nikkei 225",
        "grupo": "Bolsas"
    },                                  # Japão
    "000001.SS": {
        "nome": "Shanghai Composite",
        "grupo": "Bolsas"
    },                                  # China
    "^NSEI": {
        "nome": "NIFTY 50",
        "grupo": "Bolsas"
    },                                  # Índia
    "^J203.JO": {
        "nome": "JSE All Shares",
        "grupo": "Bolsas"
    },                                  # África do Sul
    "^KS11": {
        "nome": "KOSPI",
        "grupo": "Bolsas"
    },                                  # Coreia do Sul
    "^AXJO": {
        "nome": "ASX 200",
        "grupo": "Bolsas"
    },                                  # Austrália
    "GC=F": {
        "nome": "Ouro",
        "grupo": "Commodities",
        "papel": "Proteção"
    },                                  # Ouro
    "SI=F": {
        "nome": "Prata",
        "grupo": "Commodities",
        "papel": "Crescimento"
    },                                  # Prata
    "HG=F": {
        "nome": "Cobre",
        "grupo": "Commodities",
        "papel": "Crescimento"
    },                                 # Cobre
    "CL=F": {
        "nome": "WTI",
        "grupo": "Commodities",
        "papel": "Energia"
    },                                  # WTI
    "BZ=F": {
        "nome": "Brent",
        "grupo": "Commodities",
        "papel": "Energia"
    },                                  # Brent
    "BTC-USD": {
        "nome": "Bitcoin",
        "grupo": "Cripto"
    },                                  # Bitcoin
    "^VIX": {
        "nome": "VIX",
        "grupo": "Risco"
    },                                  # VIX
    "DX-Y.NYB": {
        "nome": "DXY",
        "grupo": "Risco"
    },                                  # Dólar Index
}

tickers = list(ativos.keys())

dados = yf.download(
    tickers,
    period="1mo",
    auto_adjust=False
)

fechamentos  = dados["Close"]

variacao = fechamentos.pct_change() * 100

ultimo = fechamentos.ffill().iloc[-1]  #último preço disponível, sem NaN

ultima_variacao = variacao.ffill().iloc[-1]

def obter_dados():
    ultima_atualizacao = datetime.now().strftime("%d/%m/%Y às %H:%M")
    resultado = []

    print("\nMARKET PULSE\n")

    for ticker, info in ativos.items():
        nome = info["nome"]
        grupo = info["grupo"]
        papel = info.get("papel")

        preco = ultimo.get(ticker)
        variacao_dia = ultima_variacao.get(ticker)

        ativo = {
            "ticker": ticker,
            "nome": nome,
            "grupo": grupo,
            "papel": papel,
            "preco": preco,
            "variacao": variacao_dia
        }

        resultado.append(ativo)

    return {
            "dados": resultado,
            "ultima_atualizacao": ultima_atualizacao
    }

resultado = obter_dados()

grupo_atual = ""

for ativo in resultado["dados"]:
    if ativo["grupo"] != grupo_atual:
        grupo_atual = ativo["grupo"]
        print(f"\n{grupo_atual.upper()}")
        print("-" * 45)

    print(
        f"{ativo['nome']:<20}"
        f"{ativo['preco']:>12.2f}" 
        f"{ativo['variacao']:>10.2f}%"
    )