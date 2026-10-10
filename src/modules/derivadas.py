

def erro_max(funcao, a, b):
    n = 1000
    passo = (b-a)/n
    valores = []
    maior = 0

    for i in range(n+1):
        for i in range(n + 1):
            valores.append(abs(funcao(a + i * passo)))

    maior = max(valores)
    return maior

# 2 pontos

def avancada(funcao, d2funcao,x, h):
    dfx = (funcao(x+h) - funcao(x)) / h

    etr= (h/2) * erro_max(d2funcao, x, x+h)

    return dfx, etr

def recuada(funcao, d2funcao,x, h):
    dfx = (funcao(x) - funcao(x-h)) / h

    etr = (h / 2) * erro_max(d2funcao, x, x + h)

    return dfx, etr


# 3 pontos

def centrada(funcao, d3funcao, x, h):
    dfx = (funcao(x + h) - funcao(x - h)) / (2 * h)
    etr = (h ** 2 / 6) * erro_max(d3funcao, x - h, x + h)
    return dfx, etr


def naoCentrada(funcao, d3funcao, x, h):
    dfx = (-3 * funcao(x) + 4 * funcao(x + h) - funcao(x + 2 * h)) / (2 * h)
    etr = (h ** 2 / 3) * erro_max(d3funcao, x, x + 2 * h)
    return dfx, etr