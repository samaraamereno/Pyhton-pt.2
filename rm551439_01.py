#esse algoritmo calcula o faturamento a partir da assinatura escolhida
faturamento = float(input("digite seu faturamento"))
print("1-basic\n2-sivler\n3-gold\n4-platinum")
assinatura = int(input("escolha sua assinatura"))
#tipos de assinaturas assinaturas:
if assinatura == 1 :
    valor_a_pagar = faturamento * 0.3
elif assinatura == 2 :
    valor_a_pagar = faturamento * 0.2
elif assinatura == 3 :
    valor_a_pagar = faturamento * 0.1
elif assinatura == 4 :
    valor_a_pagar = faturamento * 0.05
print(valor_a_pagar)

