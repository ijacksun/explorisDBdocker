import redis
import time

# Conexão com o servidor Redis
client = redis.Redis(host='redis', port=6379, db=0)

def calculo_demorado(param):
    # Simula uma operação custosa
    time.sleep(5)
    return param * 2

def get_resultado(param):
    # Tenta obter o resultado do cache
    cache_key = f"resultado:{param}"
    resultado = client.get(cache_key)
    
    if resultado:
        print("Resultado obtido do cache")
        return int(resultado)
    else:
        print("Calculando resultado")
        resultado = calculo_demorado(param)
        # Armazena o resultado no cache com um tempo de expiração de 10 segundos
        client.setex(cache_key, 10, resultado)
        return resultado

if __name__ == "__main__":
    param = 10
    
    # Primeira chamada: o resultado será calculado
    print(get_resultado(param))
    
    # Segunda chamada: o resultado será obtido do cache
    print(get_resultado(param))