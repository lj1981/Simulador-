import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Render!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Use a variável PORT ou 5000 como fallback
    app.run(host="100.20.92.101", port=port)

