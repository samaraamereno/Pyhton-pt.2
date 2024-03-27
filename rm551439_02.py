#Esse algoritmo calcula a quantidade de votos por semana
segunda = int(input("Digite o valor de votos de segunda-feira: "))
terca= int(input("Digite o valor de votos de terça-feira: "))
quarta = int(input("Digite o valor de votos de quarta-feira: "))
quinta = int(input("Digite o valor de votos de quinta-feira: "))
sexta = int(input("Digite o valor de votos de sexta-feira: "))
max_votos = max(segunda, terca, quarta, quinta, sexta)
if max_votos == segunda:
    diaEscolhido = "segunda-feira"
elif max_votos == terca:
    diaEscolhido = "terça-feira"
elif max_votos == quarta:
    diaEscolhido = "quarta-feira"
elif max_votos == quinta:
    diaEscolhido = "quinta-feira"
else :
    diaEscolhido = "sexta-feira"
print(f"Dia escolhido foi {diaEscolhido}")
