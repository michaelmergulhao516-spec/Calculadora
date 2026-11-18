import tkinter as tk
from calculadora import calcular
from historico import mostrar, limpar

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora")
        self.geometry("300x400")

        self.visor = tk.Entry(self, font=("Arial", 20), justify="right")
        self.visor.pack(fill="x", padx=10, pady=10)

        self.numero1 = 0
        self.operacao = ""

        quadro = tk.Frame(self)
        quadro.pack(expand=True, fill="both")

        botoes = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "=", "+"
        ]

        for i, texto in enumerate(botoes):
            tk.Button(
                quadro, text=texto,
                font=("Arial", 16),
                command=lambda t=texto: self.clicar(t)
            ).grid(row=i//4, column=i%4, sticky="nsew")

        for i in range(4):
            quadro.grid_columnconfigure(i, weight=1)
            quadro.grid_rowconfigure(i, weight=1)

        tk.Button(self, text="Histórico", command=mostrar).pack(fill="x")
        tk.Button(self, text="Limpar histórico", command=limpar).pack(fill="x")

    def clicar(self, valor):
        if valor == "C":
            self.visor.delete(0, tk.END)
            self.operacao = ""

        elif valor in "+-*/":
            try:
                self.numero1 = float(self.visor.get())
                self.operacao = valor
                self.visor.delete(0, tk.END)
            except ValueError:
                self.exibir("Erro")

        elif valor == "=":
            try:
                numero2 = float(self.visor.get())
                self.exibir(calcular(self.numero1, numero2, self.operacao))
            except ValueError:
                self.exibir("Erro")

        else:
            self.visor.insert(tk.END, valor)

    def exibir(self, valor):
        self.visor.delete(0, tk.END)
        self.visor.insert(0, str(valor))

