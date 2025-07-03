"""
Você trabalha em um armazém e precisa organizar o estoque de um produto que vem em diferentes tamanhos de caixas. Seu objetivo é determinar quantas caixas de cada tipo são necessárias para armazenar uma quantidade total de itens, priorizando o uso das caixas maiores para otimizar o espaço.
Instruções:
Solicite ao usuário a quantidade total de itens que precisa ser armazenada.
Considere que você tem os seguintes tipos de caixas, com suas respectivas capacidades:
Caixa Grande: 100 itens
Caixa Média: 50 itens
Caixa Pequena: 10 itens
Caixa Mini: 1 item
Calcule e informe quantas caixas de cada tipo serão necessárias para armazenar a quantidade total de itens, utilizando o menor número de caixas possível e sempre priorizando as caixas maiores.
Além disso, informe quantos itens restarão avulsos (que não couberam em nenhuma caixa). 
"""

qtd_itens = int(input("Digite a quantidade de itens para armazenar: "))

caixa_grande = qtd_itens // 100
itens_restantes = qtd_itens % 100

caixa_media = itens_restantes // 50
itens_restantes = itens_restantes % 50

caixa_pequena = itens_restantes // 10
itens_restantes = itens_restantes % 10

caixa_mini = itens_restantes // 1

print(f"Para armazenar {qtd_itens} produtos e manter o estoque organizado, serão necessárias {caixa_grande} caixas grandes, {caixa_media} caixas médias, {caixa_pequena} caixas pequenas e {caixa_mini} caixas mini")