# Documentação: Cache & Enfileiramento utilizando Redis<br>
Introdução <br>
Este documento descreve o funcionamento de dois exemplos de código em Python que utiliza o Redis para implementar um sistema de cache(cache.py) e outro para demonstrar tecnica de enfileiramento(produtor.py & consumidor.py). O objetivo é armazenar temporariamente os resultados de operações custosas para melhorar o desempenho e reduzir o tempo de resposta em aplicações.<br>
<br>

Requisitos:<br>
• Python 3.x<br>
• Biblioteca redis-py (pode ser instalada com pip install redis)<br>
• Servidor Redis em execução<br>

# Exemplo Cache(cache.py):<br>

Descrição do Código<br>
O código consiste em três funções principais:<br>

calculo_demorado(param): Simula uma operação custosa que demora 5 segundos para ser concluída.<br>
get_resultado(param): Tenta obter o resultado de uma operação custosa a partir do cache Redis. Se o resultado não estiver no cache, calcula o resultado e o armazena no cache com um tempo de expiração de 10 segundos.<br>
main: Executa a função get_resultado duas vezes para demonstrar o uso do cache.<br>
<br>
Dependências:<br>
import redis<br>
import time<br>

Execução do Código: <br>

Calculando resultado<br>
20<br>
Resultado obtido do cache<br>
20<br>

# Exemplo Enfileiramento(produtor.py & consumidor.py):

Aqui é descrito um exemplo de implementação de enfileiramento utilizando Redis em Python. O enfileiramento é uma técnica fundamental em sistemas distribuídos para comunicação assíncrona entre processos ou serviços.<br>

- Produtor (produtor.py)<br>
Descrição: <br>
O produtor é responsável por adicionar números a uma fila no Redis.<br>

• Funcionamento<br>
Conexão ao Redis: Estabelece uma conexão com o servidor Redis.<br>
Adição à Fila: Utiliza r.rpush(queue_name, number) para adicionar cada número ao final da fila chamada number_queue.<br>

- Consumidor (consumidor.py)<br>
Descrição:<br>
O consumidor é responsável por retirar números da fila no Redis e processá-los.<br>

• Funcionamento<br>
Conexão ao Redis: Estabelece uma conexão com o servidor Redis.<br>
Obtenção da Mensagem: Utiliza r.blpop(queue_name) para bloquear e esperar por um número na fila number_queue.<br>
Processamento: Decodifica o número (armazenado como bytes) e o processa.<br>
Delay: Adiciona um pequeno delay (time.sleep(1)) para simular o tempo de processamento.<br>

• Execução<br>
Para executar esses scripts:<br>

utiliza-se o comando:<br>
docker-compose up --build<br>

