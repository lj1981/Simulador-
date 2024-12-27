import time
from flask import Flask

app = Flask(__name__)
hosts = ['100.20.92.101', '44.255.181.72', '44.227.217.144']
port = int(os.environ.get('PORT', 10000))

while True:
    for host in hosts:
        app.run(host=host, port=port)
        time.sleep(60)  # Pausar por 60 segundos antes de trocar de host
