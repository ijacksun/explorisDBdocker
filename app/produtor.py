import redis

def producer():
    # Conectando ao Redis
    r = redis.Redis(host='redis', port=6379, db=0)

    # Nome da fila
    queue_name = 'number_queue'

    # Números para adicionar à fila
    numbers = [1, 2, 3, 4, 5]

    for number in numbers:
        # Adiciona o número ao final da fila
        r.rpush(queue_name, number)
        print(f"Produzido: {number}")


if __name__ == "__main__":
    producer()