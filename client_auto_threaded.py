from socket import *
from threading import Thread
from time import perf_counter
from statistics import mean
import argparse

from constCS import SERVER_HOST, PORT, BUFFER_SIZE

def carregar_requisicoes(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        return [linha.strip() for linha in f if linha.strip()]

def enviar_requisicao(req):
    inicio = perf_counter()

    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((SERVER_HOST, PORT))
        s.sendall(req.encode())

        resposta = b""
        while True:
            bloco = s.recv(BUFFER_SIZE)
            if not bloco:
                break
            resposta += bloco

    fim = perf_counter()
    return resposta.decode(), fim - inicio

def worker(indice, req, latencias):
    _, lat = enviar_requisicao(req)
    latencias[indice] = lat

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, default="requests.txt")
    args = parser.parse_args()

    requisicoes = carregar_requisicoes(args.file)
    latencias = [0.0] * len(requisicoes)
    threads = []

    inicio_total = perf_counter()

    for i, req in enumerate(requisicoes):
        t = Thread(target=worker, args=(i, req, latencias))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    fim_total = perf_counter()

    tempo_total = fim_total - inicio_total
    throughput = len(requisicoes) / tempo_total if tempo_total > 0 else 0

    print(f"TOTAL_REQUISICOES={len(requisicoes)}")
    print(f"TEMPO_TOTAL={tempo_total:.6f}")
    print(f"LATENCIA_MEDIA={mean(latencias):.6f}")
    print(f"THROUGHPUT={throughput:.2f}")

if __name__ == "__main__":
    main()
