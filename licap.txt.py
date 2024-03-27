# Função que calcula a velocidade média
def calcularVelocidadeMedia(distancia, tempo):
    # calcular a velocidade média
    velocidade_media = distancia / tempo
    # exibir o resultado
    print("A velocidade média é {} km/h".format(velocidade_media))


# aqui começa o programa principal
distancia = float(input("Informe a distância"))
tempo = float(input("Informe o tempo"))
# chamando a função com valores definidos pelo usuário
calcularVelocidadeMedia(distancia, tempo)


# chamando a função com valores definidos pelo programador
calcularVelocidadeMedia(15, 2)