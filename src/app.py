from modules.expressoes import (
    criar_funcao, criar_derivada, criar_derivada2, criar_derivada3,
    traduzir_numero, ExpressaoInvalidaError,
)
from modules.derivadas import avancada, recuada, centrada, naoCentrada


def main():
    try:
        expr = input("f(x) = ")
        x = traduzir_numero(input("x = "), "x")
        h = traduzir_numero(input("h = "), "h")
        if h <= 0:
            print("h deve ser positivo.")
            return

        f = criar_funcao(expr)
        df = criar_derivada(expr)
        d2f = criar_derivada2(expr)
        d3f = criar_derivada3(expr)

        exato = df(x)
        print(f"\nf'(x) exato = {exato:.10f}\n")

        metodos = [
            ("Avançada (2 pontos)", avancada, d2f),
            ("Recuada (2 pontos)", recuada, d2f),
            ("Centrada (3 pontos)", centrada, d3f),
            ("Não centrada (3 pontos)", naoCentrada, d3f),
        ]
        print(f"{'Método':<26}{'Aproximação':>16}{'Erro real':>14}{'Limite do erro':>16}")
        for nome, metodo, derivada_erro in metodos:
            dfx, etr = metodo(f, derivada_erro, x, h)
            print(f"{nome:<26}{dfx:>16.10f}{abs(dfx - exato):>14.2e}{etr:>16.2e}")

    except ExpressaoInvalidaError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    try:
        main()  # o que você já executa hoje
    except Exception as e:
        print(f"\nErro: {e}")
    input("\nPressione Enter para sair...")