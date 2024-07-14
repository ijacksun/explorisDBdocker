import redis
import time

def consumer():
    # Conectando ao Redis
    r = redis.Redis(host='redis', port=6379, db=0)

    # Nome da fila
    queue_name = 'number_queue'

    while True:
        # Obtém um número da fila (bloqueia até que haja um número disponível)
        message = r.blpop(queue_name)

        if message:
            # message[0] é o nome da fila, message[1] é o número em bytes
            number = message[1].decode('utf-8')  # Decodifica os bytes para string UTF-8
            print(f"Consumido: {number}")

        time.sleep(1)  # Adiciona um pequeno delay para simular o tempo de processamento


if __name__ == "__main__":
    consumer()