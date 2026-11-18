# Calculadora em Python

## 1. Descrição do projeto

Este projeto consiste em uma calculadora desenvolvida em Python, utilizando a biblioteca Tkinter para criar uma interface gráfica.

A calculadora permite realizar operações matemáticas básicas e armazenar um histórico dos cálculos realizados durante a execução do programa.

## 2. Funcionalidades

- Adição (+)
- Subtração (-)
- Multiplicação (*)
- Divisão (/)
- Limpar o visor (C)
- Visualizar o histórico dos cálculos
- Limpar o histórico

## 3. Estrutura do projeto

```text
Calculadora/
│
├── main.py
├── operações.py
├── historico.py
├── calculadora.py
├── interface.py
└── Read.me
```

## 4. Função dos arquivos

**main.py:** arquivo principal que inicia a calculadora.

**operações.py:** contém as funções responsáveis pelas operações matemáticas.

**historico.py:** armazena, mostra e limpa o histórico dos cálculos.

**calculadora.py:** conecta as operações matemáticas ao histórico e retorna os resultados.

**interface.py:** cria a interface gráfica utilizando Tkinter, incluindo visor e botões.

**Read.me:** contém as informações e instruções do projeto.

## 5. Tecnologias utilizadas

- Python
- Tkinter
- Visual Studio Code

## 6. Como executar

1. Instale o Python no computador.
2. Abra a pasta do projeto no VS Code.
3. Verifique se todos os arquivos estão na mesma pasta.
4. Abra o terminal do VS Code.
5. Execute o comando:

```bash
python main.py
```

A janela da calculadora será aberta.

## 7. Como utilizar

1. Digite o primeiro número.
2. Escolha a operação matemática desejada.
3. Digite o segundo número.
4. Pressione o botão `=` para visualizar o resultado.
5. Utilize `C` para limpar o visor.
6. Clique em **Histórico** para visualizar os cálculos no terminal.
7. Clique em **Limpar histórico** para apagar os registros.

## 8. Observações

- O histórico fica armazenado temporariamente na memória.
- Ao fechar o programa, o histórico será perdido.
- A calculadora possui tratamento para divisão por zero.
- Não é necessário instalar bibliotecas externas quando o Tkinter já está disponível na instalação do Python.

## 9. Conclusão

O projeto demonstra a utilização de funções, listas, condicionais, importação de módulos e interface gráfica em Python.

A divisão do código em arquivos facilita sua organização, manutenção e futuras melhorias.