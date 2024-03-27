#importação de funções específica do módulo calc.py
from calc import multiplicar
#solicitando valores ao usuário
valor1 = input("Digite um valor: ")
valor2 = input("Digite outro valor: ")
#armazenando a soma
multiplicacao = multiplicar(valor1, valor2)
#exibindo a soma
print("A soma é {}".format(multiplicacao))