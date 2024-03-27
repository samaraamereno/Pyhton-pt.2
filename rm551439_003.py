def validar_float(a):
    while True:
        try:
            a = float(a)
            return a
        except ValueError:
            a = input("Digite uma nota valida, utilize ponto e não virgula : ")
def validar_nota(a):
    while True:
        if 0 <= a <= 10:
            return a
        else:
            a = input("Digite uma nota entre 0 e 10 : ")
            a = validar_float(a)


print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
par, impar = 0, 0
for i in range(2, 51, 2):
    nota = input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {i} : ")
    nota = validar_float(nota)
    nota = validar_nota(nota)
    par += nota
for i in range(1, 50, 2):
    nota = input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {i} : ")
    nota = validar_float(nota)
    nota = validar_nota(nota)
    impar += nota
media_par = par / 25
media_impar = impar / 25
print("A media dos alunos pares foi {:.1f} e a media dos alunos impares foi {:.1f}".format(media_par, media_impar))
if par > impar:
    print("A maior media foi a dos alunos pares")
elif impar > par:
    print("A maior media foi a dos alunos impares")
else:
    print('Foi empate')
