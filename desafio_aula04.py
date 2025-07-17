alunos = 0
aprovados = 0
reprovados = 0
maior_media = 0
menor_media = 99
media_turma = 0
aluno_maior_media = "aluno"
aluno_menor_media = "aluno2"

while True:
    nome = input('Digite seu nome: ')
    if nome == "fim":
        break
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))

    media = (nota1 + nota2 + nota3) / 3
    if media > maior_media:
        maior_media = media
        aluno_maior_media = nome

    if media < menor_media:
        menor_media = media
        aluno_menor_media = nome

    if media >= 7:
        aprovados += 1

    if media <7:
        reprovados +=1

alunos += 1
media_turma = media_turma + media

print(f'Alunos aprovados: {aprovados}, alunos reprovados: {reprovados}, maior média: {maior_media:.2f}, menor média: {menor_media:.2f}, média geral da turma: {media_turma:.2f}. Aluno que obteve a maior média: {aluno_maior_media}, aluno com menor média: {aluno_menor_media}')