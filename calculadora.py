from operações import Soma, Subtracao, Multiplicacao, Divisao
from historico import adicionar

def calcular(a, b, operacao):
    operacoes = {
        "+": Soma(),
        "-": Subtracao(),
        "*": Multiplicacao(),
        "/": Divisao()
    }

    if operacao not in operacoes:
        return "Operação inválida"

    resultado = operacoes[operacao].calcular(a, b)

    adicionar(f"{a} {operacao} {b} = {resultado}")

    return resultado
