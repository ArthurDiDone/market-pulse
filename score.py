def calcular_scores(resultado):
    score_bolsas = 0
    sinal_proteção = 0
    sinal_prata = 0
    sinal_cobre = 0
    sinal_wti = 0
    sinal_brent = 0
    sinal_btc = 0
    vix = 0
    variacao_vix = 0
    dxy = 0
    variacao_dxy = 0
    direcao_ouro = "Estável"
    direcao_cobre = "Estável"
    direcao_prata = "Estável"
    direcao_wti = "Estável"
    direcao_brent = "Estável"

    for ativo in resultado:

        if ativo["grupo"] == "Bolsas":
            if ativo["variacao"] > 0:
                score_bolsas += 1

        elif ativo["grupo"] == "Commodities":
            papel = ativo["papel"]

            if papel == "Proteção":
                if ativo["variacao"] > 0:
                    sinal_proteção = 1 
                    direcao_ouro = "Crescente"
                elif ativo["variacao"] < 0:
                    sinal_protecao = 0
                    direcao_ouro = "Decrescente"
                else:
                    sinal_proteção = 0
                    direcao_ouro = "Estável"

            elif papel == "Crescimento":
                if ativo["nome"] == "Cobre":
                    if ativo["variacao"] > 0:
                        sinal_cobre = 1
                        direcao_cobre = "Crescente"
                    elif ativo["variacao"] < 0:
                        sinal_cobre = 0
                        direcao_cobre = "Decrescente"
                    else:
                        sinal_cobre = 0
                        direcao_cobre = "Estável"

                elif ativo["nome"] == "Prata":
                    if ativo["variacao"] > 0:
                        sinal_prata = 1
                        direcao_prata = "Crescente"
                    elif ativo["variacao"] < 0:
                        sinal_prata = 0
                        direcao_prata = "Decrescente"
                    else:
                        sinal_prata = 0  
                        direcao_prata = "Estável"                   

            elif papel == "Energia":
                if ativo["nome"] == "WTI":
                    if ativo["variacao"] > 0:
                        sinal_wti = 1
                        direcao_wti = "Crescente"
                    elif ativo["variacao"] < 0:
                        sinal_wti = 0
                        direcao_wti = "Decrescente"
                    else:
                        sinal_wti = 0
                        direcao_wti = "Estável"
                                
                elif ativo["nome"] == "Brent":
                    if ativo["variacao"] > 0:
                        sinal_brent = 1
                        direcao_brent = "Crescente"
                    elif ativo["variacao"] < 0:
                        sinal_brent = 0
                        direcao_brent = "Decrescente"
                    else:
                        sinal_brent = 0     
                        direcao_brent = "Estável"

        elif ativo["grupo"] == "Cripto":
            if ativo["variacao"] > 0:
                sinal_btc = 1
            else:
                sinal_btc = 0

        elif ativo["grupo"] == "Risco":
            if ativo["nome"] == "VIX":
                vix = ativo["preco"]
                variacao_vix = ativo["variacao"]
            elif ativo["nome"] == "DXY":
                dxy = ativo["preco"]
                variacao_dxy = ativo["variacao"]

    if sinal_prata > 0 or sinal_cobre > 0:
        sinal_crescimento = 1
    else:
        sinal_crescimento = 0
                
    if sinal_brent > 0 or sinal_wti > 0:
        sinal_energia = 1
    else:
        sinal_energia = 0

    if vix < 15:
        nivel_vix = "Baixa volatilidade"
    elif vix < 20:
        nivel_vix = "Volatilidade normal"
    elif vix < 30:
        nivel_vix = "Atenção"
    elif vix < 40:
        nivel_vix = "Estresse"
    else:
        nivel_vix = "Estresse elevado"

    if variacao_vix > 0:
        direcao_vix = "Crescente"
    elif variacao_vix < 0:
        direcao_vix = "Decrescente"
    else:
        direcao_vix = "Estável"

    if abs(variacao_dxy) < 0.25:
        nivel_dxy = "Estável"
    elif abs(variacao_dxy) < 0.75:
        nivel_dxy = "Movimento moderado"
    elif abs(variacao_dxy) < 1.50:
        nivel_dxy = "Movimento forte"
    else:
        nivel_dxy = "Movimento muito forte"

    if variacao_dxy > 0:
        direcao_dxy = "Crescente"
    elif variacao_dxy < 0:
        direcao_dxy = "Decrescente"
    else:
        direcao_dxy = "Estável"

    return {
        "bolsas": score_bolsas,
        "proteção": sinal_proteção,
        "energia": sinal_energia,
        "crescimento": sinal_crescimento,
        "btc": sinal_btc,
        "vix": {
            "valor": vix,
            "nivel": nivel_vix,
            "direcao": direcao_vix,
            "variacao": variacao_vix
        },
        "dxy": {
            "valor": dxy,
            "nivel": nivel_dxy,
            "direcao": direcao_dxy,
            "variacao": variacao_dxy
        },
        "ouro": {
            "direcao": direcao_ouro
        },
        "cobre": {
            "direcao": direcao_cobre
        },
        "prata": {
            "direcao": direcao_prata
        },
        "wti": {
            "direcao": direcao_wti
        },
        "brent": {
            "direcao": direcao_brent
        }
    }        