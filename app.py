import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Render!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Use a variável PORT ou 5000 como fallback
    app.run(host="0.0.0.0", port=port)

