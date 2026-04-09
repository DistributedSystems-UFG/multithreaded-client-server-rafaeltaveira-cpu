from socket import *
from threading import Thread
from constCS import PORT, BUFFER_SIZE, BACKLOG, VERBOSE
from operations import montar_resposta

def atender_cliente(conn, addr):
    with conn:
        data = conn.recv(BUFFER_SIZE)

        if not data:
            return

        requisicao = data.decode().strip()

        if VERBOSE:
            print(f"[THREAD] Cliente conectado: {addr}")
            print(f"[THREAD] Requisição recebida: {requisicao}")

        resposta = montar_resposta(requisicao)
        conn.sendall(resposta.encode())

        if VERBOSE:
            print(f"[THREAD] Atendimento finalizado para {addr}\n")

def main():
    with socket(AF_INET, SOCK_STREAM) as s:
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        s.bind(("0.0.0.0", PORT))
        s.listen(BACKLOG)

        print(f"Servidor MULTITHREAD ouvindo na porta {PORT}...")

        while True:
            conn, addr = s.accept()
            t = Thread(target=atender_cliente, args=(conn, addr), daemon=True)
            t.start()

if __name__ == "__main__":
    main()
