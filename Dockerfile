FROM python:3.9
#
WORKDIR /usr/src/app
COPY . .

RUN pip install -r requirements.txt

CMD [ "sh", "-c", "python3 visualização_de_dados_financeiros.py " ]
