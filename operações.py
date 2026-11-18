from abc import ABC, abstractmethod

class Operacao(ABC):
    @abstractmethod
    def calcular(self, a, b):
        pass

class Soma(Operacao):
    def calcular(self, a, b):
        return a + b

class Subtracao(Operacao):
    def calcular(self, a, b):
        return a - b

class Multiplicacao(Operacao):
    def calcular(self, a, b):
        return a * b

class Divisao(Operacao):
    def calcular(self, a, b):
        if b == 0:
            return "Erro: divisão por zero"
        return a / b

