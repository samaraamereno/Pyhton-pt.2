def validar_input(a):
    while True:
        if a.isdigit() and 0 <= int(a) < 60:
            return a
        else:
            a = input('Valor invalido, digite um valor inteiro entre 0 e 59: ')
            # solicita a digitação e repete

minutos = input("Digite a minutagem da sua maquina : ")
minutos = validar_input(minutos)
minutos = int(minutos)
fatorial = 1
for i in range(1, minutos + 1):
    fatorial *= i
print(f"A senha é LIBERDADE{fatorial}")
