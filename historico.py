
historico = []

def adicionar(calculo):
    historico.append(calculo)

def mostrar():
    for calculo in historico:
        print(calculo)

def limpar():
    historico.clear()
