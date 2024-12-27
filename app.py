from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Aplicação de Análise de Dados Financeiros</h1><p>Seu código está funcionando corretamente no Render!</p>"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # Porta configurada pelo Render
    app.run(host="0.0.0.0", port=port)
