qtd_total_estoque = 0
qtd_estoque = 0
preco_unitario = 0
produto_menor_valor_total = None
produto_maior_valor_total = None
produto_mais_caro = None
produto_mais_barato = 'produto'
valor_produto_mais_caro = 0
valor_produto_mais_barato = float('inf')
valor_total = preco_unitario * qtd_estoque
maior_valor_total = 0
menor_valor_total = float('inf')
valor_total_estoque = 0

while True:
    produto = input('Digite o nome do produto: ')
    preco_unitario = float(input('Digite o preço unitário do produto: '))
    if preco_unitario < 0:
        break
    qtd_estoque = int(input('Digite a quantidade em estoque: '))
    valor_total = preco_unitario * qtd_estoque
    
    if valor_total > maior_valor_total:
        maior_valor_total = valor_total
        produto_maior_valor_total = produto
        
    if valor_total < menor_valor_total:
        menor_valor_total = valor_total
        produto_menor_valor_total = produto

    if preco_unitario > valor_produto_mais_caro:
        valor_produto_mais_caro = preco_unitario
        produto_mais_caro = produto

    if preco_unitario < valor_produto_mais_barato:
        valor_produto_mais_barato = preco_unitario
        produto_mais_barato = produto

    qtd_total_estoque = qtd_total_estoque + qtd_estoque
    valor_total_estoque = valor_total_estoque + valor_total


print(f"O produto com maior valor total é: {produto_maior_valor_total}")
print(f"O produto com menor valor total é: {produto_menor_valor_total}")
print(f"O produto mais caro é: {produto_mais_caro}")
print(f"O produto mais barato é: {produto_mais_barato}")
print(f"O valor total de todos os produtos é R$ {valor_total_estoque}")
print(f"A quantidade de produtos no estoque é {qtd_total_estoque}")


