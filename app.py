from flask import Flask
import os

app = Flask(__name__)

# Rota principal
@app.route("/")
def home():
    return "Hello, Render!"

# Certifique-se de usar a porta especificada pela variável de ambiente
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # Padrão 5000 caso PORT não esteja definido
    app.run(host="0.0.0.0", port=port)
