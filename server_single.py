from socket import *
from constCS import PORT, BUFFER_SIZE, BACKLOG, VERBOSE
from operations import montar_resposta

def atender_cliente(conn, addr):
    with conn:
        data = conn.recv(BUFFER_SIZE)

        if not data:
            return

        requisicao = data.decode().strip()

        if VERBOSE:
            print(f"[SINGLE] Cliente conectado: {addr}")
            print(f"[SINGLE] Requisição recebida: {requisicao}")

        resposta = montar_resposta(requisicao)
        conn.sendall(resposta.encode())

        if VERBOSE:
            print("[SINGLE] Conexão encerrada.\n")

def main():
    with socket(AF_INET, SOCK_STREAM) as s:
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        s.bind(("0.0.0.0", PORT))
        s.listen(BACKLOG)

        print(f"Servidor SINGLE ouvindo na porta {PORT}...")

        while True:
            conn, addr = s.accept()
            atender_cliente(conn, addr)

if __name__ == "__main__":
    main()
