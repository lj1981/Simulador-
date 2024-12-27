import os
from flask import Flask

# Inicializar o app Flask
app = Flask(__name__)

# Rota principal para testar
@app.route('/')
def index():
    return "Hello, Render! Your Flask app is running."

# Ponto de entrada da aplicação
if __name__ == '__main__':
    # Render exige que o aplicativo escute na porta especificada pela variável PORT
    port = int(os.getenv("PORT", 5000))  # Porta padrão 5000 caso não exista a variável de ambiente PORT
    app.run(host='0.0.0.0', port=port)  # Host 0.0.0.0 permite conexões externas

