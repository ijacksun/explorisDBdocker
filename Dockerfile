FROM python:3

WORKDIR /app

COPY . .

# Instale as dependências do seu projeto
RUN pip install --no-cache-dir -r requirements.txt

# Adicione um comando para verificar a instalação do redis
RUN pip show redis

CMD ["sh", "-c", "python app/cache.py & python app/produtor.py & python app/consumidor.py"]