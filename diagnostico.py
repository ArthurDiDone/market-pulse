def gerar_diagnostico(score):

    if score["bolsas"] <= 2:
        regime = "Forte Risk-off"

    elif score["bolsas"] <= 5:
        regime = "Moderado Risk-off"

    elif score["bolsas"] <= 8:
        regime = "Neutro"

    elif score["bolsas"] <= 10:
        regime = "Moderado Risk-on"

    else:
        regime = "Forte Risk-on"

    divergencias = 0

    if "Risk-on" in regime:
        if score["vix"]["direcao"] == "Crescente":
            divergencias += 1

    elif "Risk-off" in regime:
        if score["vix"]["direcao"] == "Decrescente":
            divergencias += 1

    if "Risk-on" in regime:
        if score["dxy"]["direcao"] == "Crescente":
            divergencias += 1

    elif "Risk-off" in regime:
        if score["dxy"]["direcao"] == "Decrescente":
            divergencias += 1

    if "Risk-on" in regime:
        if score["ouro"]["direcao"] == "Crescente":
            divergencias += 1

    elif "Risk-off" in regime:
        if score["ouro"]["direcao"] == "Decrescente":
            divergencias += 1

    if "Risk-on" in regime:
        if score["cobre"]["direcao"] == "Decrescente":
            divergencias += 1

    elif "Risk-off" in regime:
        if score["cobre"]["direcao"] == "Crescente":
            divergencias += 1

    if "Risk-on" in regime:
        if score["prata"]["direcao"] == "Decrescente":
            divergencias += 1

    elif "Risk-off" in regime:
        if score["prata"]["direcao"] == "Crescente":
            divergencias += 1

    if "Risk-on" in regime:
        if score["wti"]["direcao"] == "Decrescente" or score["brent"]["direcao"] == "Decrescente":
            divergencias += 1

    elif "Risk-off" in regime:
        if score["wti"]["direcao"] == "Crescente" or score["brent"]["direcao"] == "Crescente":
            divergencias += 1

    if "Risk-on" in regime:
        if score["btc"] == 0:
            divergencias += 1

    elif "Risk-off" in regime:
        if score["btc"] == 1:
            divergencias += 1



    if "Risk-on" in regime:
        if divergencias <= 1:
            diagnostico = "Risk-on"
        else:
            diagnostico = "Risk-on com cautela"

    elif "Risk-off" in regime:

        if divergencias <= 1:
            diagnostico = "Risk-off"
        else:
            diagnostico = "Risk-off com sinais de reversão"

    else:
        diagnostico = "Mercado neutro / sinais mistos"

    return {
        "regime": regime,
        "divergencias": divergencias,
        "diagnostico": diagnostico
    }
