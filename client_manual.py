from socket import *
from constCS import SERVER_HOST, PORT, BUFFER_SIZE

def main():
    print("Cliente iniciado.")
    print(f"Conectando em {SERVER_HOST}:{PORT}")

    while True:
        requisicao = input("\nDigite a requisição (ou 'sair'): ").strip()

        if requisicao.lower() == "sair":
            print("Encerrando cliente.")
            break

        if not requisicao:
            print("Digite algum comando.")
            continue

        with socket(AF_INET, SOCK_STREAM) as s:
            s.connect((SERVER_HOST, PORT))
            s.sendall(requisicao.encode())

            resposta = b""
            while True:
                bloco = s.recv(BUFFER_SIZE)
                if not bloco:
                    break
                resposta += bloco

        print("\nResposta do servidor:")
        print(resposta.decode())

if __name__ == "__main__":
    main()
