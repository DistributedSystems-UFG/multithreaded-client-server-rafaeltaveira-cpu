import random
import argparse

def gerar_requisicao():
    op = random.choice(["soma", "subtrai", "multiplica", "divide", "fatorial", "primo"])

    if op == "soma":
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        return f"soma {a} {b}"

    elif op == "subtrai":
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        return f"subtrai {a} {b}"

    elif op == "multiplica":
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        return f"multiplica {a} {b}"

    elif op == "divide":
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        return f"divide {a} {b}"

    elif op == "fatorial":
        n = random.randint(5, 20)
        return f"fatorial {n}"

    else:  # primo
        n = random.randint(100000, 200000)
        return f"primo {n}"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--total", type=int, default=500)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output", type=str, default="requests.txt")
    args = parser.parse_args()

    random.seed(args.seed)

    with open(args.output, "w", encoding="utf-8") as f:
        for _ in range(args.total):
            f.write(gerar_requisicao() + "\n")

    print(f"Arquivo '{args.output}' gerado com {args.total} requisições (seed={args.seed}).")

if __name__ == "__main__":
    main()
