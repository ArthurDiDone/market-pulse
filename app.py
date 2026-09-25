from flask import Flask, render_template
from market_data import obter_dados
from score import calcular_scores
from diagnostico import gerar_diagnostico
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():

    resultado = obter_dados()
    dados = resultado["dados"]
    score = calcular_scores(dados)
    diagnostico = gerar_diagnostico(score)
    
    return render_template(
        "score.html",
        score=score,
        diagnostico=diagnostico,
        ultima_atualizacao=resultado["ultima_atualizacao"]
    )
        
@app.route("/mercados")
def mercados():
    resultado = obter_dados()

    return render_template(
        "index.html",
        resultado=resultado["dados"],
        ultima_atualizacao=resultado["ultima_atualizacao"]
        )

@app.route("/score")
def score():
    resultado = obter_dados()
    dados = resultado["dados"]
    score = calcular_scores(dados)
    diagnostico = gerar_diagnostico(score)
    
    return render_template(
        "score.html",
        score=score,
        diagnostico=diagnostico,
        ultima_atualizacao=resultado["ultima_atualizacao"]
    )    

@app.route("/metodologia")
def metodologia():
    return render_template("metodologia.html")

if __name__ == "__main__":
    app.run(debug=True)