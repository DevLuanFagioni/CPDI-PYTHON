# =====================================================================
# EXERCÍCIOS - ESTRUTURA DE REPETIÇÃO (FOR)
# =====================================================================
# Tópicos: for in, range(), dicionários e estruturas de controle
# =====================================================================


# =====================================================================
# PARTE 1: FOR IN - ITERANDO SOBRE LISTAS
# =====================================================================

# Exercício 1.1: Listar todos os produtos
# Crie uma lista com 5 produtos e imprima cada um deles usando for in
# Resultado esperado: Cada produto em uma linha

# SOLUÇÃO:
# produtos = ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Webcam']
# for produto in produtos:
#     print(produto)


# Exercício 1.2: Somar elementos de uma lista
# Crie uma lista com 5 números e use for in para somar todos eles
# Dica: Use uma variável acumuladora

# SOLUÇÃO:
# numeros = [10, 20, 30, 40, 50]
# total = 0
# for numero in numeros:
#     total += numero
# print(f"Total: {total}")


# Exercício 1.3: Contar quantos elementos tem em uma lista
# Sem usar len(), use for in para contar quantos elementos existem na lista
# Lista: ['Python', 'Java', 'C++', 'JavaScript', 'Go', 'Rust']

# SOLUÇÃO:
# linguagens = ['Python', 'Java', 'C++', 'JavaScript', 'Go', 'Rust']
# contador = 0
# for linguagem in linguagens:
#     contador += 1
# print(f"Total de linguagens: {contador}")


# =====================================================================
# PARTE 2: ENTENDENDO RANGE()
# =====================================================================
# range(inicio, fim, passo)
# - inicio: por onde começa (padrão: 0)
# - fim: até onde vai (NÃO INCLUI o fim)
# - passo: de quanto em quanto salta (padrão: 1)

# Exercício 2.1: Range básico
# Use range(10) para imprimir os números de 0 a 9

# SOLUÇÃO:
# for numero in range(10):
#     print(numero)


# Exercício 2.2: Range com início e fim
# Use range(5, 15) para imprimir os números de 5 a 14

# SOLUÇÃO:
# for numero in range(5, 15):
#     print(numero)


# Exercício 2.3: Range com passo
# Use range(0, 20, 2) para imprimir números pares de 0 a 18

# SOLUÇÃO:
# for numero in range(0, 20, 2):
#     print(numero)


# Exercício 2.4: Range regressivo
# Use range(10, 0, -1) para imprimir os números de 10 a 1 (regressivo)

# SOLUÇÃO:
# for numero in range(10, 0, -1):
#     print(numero)


# Exercício 2.5: Acessar elementos de uma lista usando range
# Dada a lista: ['A', 'B', 'C', 'D', 'E']
# Use range com len() para imprimir o índice e o valor de cada elemento
# Resultado esperado: 
# 0 - A
# 1 - B
# 2 - C
# etc...

# SOLUÇÃO:
# letras = ['A', 'B', 'C', 'D', 'E']
# for i in range(len(letras)):
#     print(f"{i} - {letras[i]}")


# =====================================================================
# PARTE 3: ITERANDO SOBRE DICIONÁRIOS - CHAVE E VALOR
# =====================================================================

# Exercício 3.1: Acessar chaves e valores de um dicionário
# Dado o dicionário de alunos com suas notas:
# alunos_notas = {"Maria": 8.5, "João": 7.0, "Pedro": 9.5, "Ana": 8.0}
# Use for com .items() para imprimir cada aluno e sua nota
# Resultado esperado:
# Maria tem nota 8.5
# João tem nota 7.0
# etc...

# SOLUÇÃO:
# alunos_notas = {"Maria": 8.5, "João": 7.0, "Pedro": 9.5, "Ana": 8.0}
# for aluno, nota in alunos_notas.items():
#     print(f"{aluno} tem nota {nota}")


# Exercício 3.2: Calcular média usando dicionário
# Dado o dicionário: {"P1": 7.5, "P2": 8.0, "P3": 9.5}
# Use for com .items() para calcular a média das provas
# Dica: Use acumulador

# SOLUÇÃO:
# provas = {"P1": 7.5, "P2": 8.0, "P3": 9.5}
# total = 0
# for prova, nota in provas.items():
#     total += nota
# media = total / len(provas)
# print(f"Média: {media}")


# Exercício 3.3: Converter valores de um dicionário
# Dado o dicionário de preços: {"notebook": 2500, "mouse": 50, "teclado": 150}
# Use for com .items() para aplicar 10% de desconto em cada item
# Imprima o novo preço de cada produto
# Resultado esperado:
# notebook: R$ 2250.0
# mouse: R$ 45.0
# etc...

# SOLUÇÃO:
# precos = {"notebook": 2500, "mouse": 50, "teclado": 150}
# desconto = 0.10
# for produto, preco in precos.items():
#     novo_preco = preco - (preco * desconto)
#     print(f"{produto}: R$ {novo_preco}")


# =====================================================================
# PARTE 4: ESTRUTURA DE CONTROLE DENTRO DO FOR (PESQUISA DE DADOS)
# =====================================================================

# Exercício 4.1: Buscar um elemento específico em uma lista
# Lista: ['Python', 'Java', 'JavaScript', 'C++', 'Go']
# Procure pela linguagem 'Java' e imprima uma mensagem se encontrar
# Use if dentro do for

# SOLUÇÃO:
# linguagens = ['Python', 'Java', 'JavaScript', 'C++', 'Go']
# busca = 'Java'
# for linguagem in linguagens:
#     if linguagem == busca:
#         print(f"Encontrei {busca}!")
#         break


# Exercício 4.2: Filtrar números maiores que um valor
# Lista: [5, 12, 8, 25, 3, 18, 30, 7]
# Use for com if para imprimir apenas os números maiores que 15

# SOLUÇÃO:
# numeros = [5, 12, 8, 25, 3, 18, 30, 7]
# limite = 15
# for numero in numeros:
#     if numero > limite:
#         print(numero)


# Exercício 4.3: Contar ocorrências de um item
# Lista: ['maçã', 'banana', 'maçã', 'laranja', 'maçã', 'banana']
# Use for com if para contar quantas vezes 'maçã' aparece na lista

# SOLUÇÃO:
# frutas = ['maçã', 'banana', 'maçã', 'laranja', 'maçã', 'banana']
# fruta_busca = 'maçã'
# contador = 0
# for fruta in frutas:
#     if fruta == fruta_busca:
#         contador += 1
# print(f"'{fruta_busca}' aparece {contador} vezes")


# Exercício 4.4: Buscar por padrão em strings
# Lista: ['João Silva', 'Maria Santos', 'João Pereira', 'Pedro Silva']
# Busque todas as pessoas com o nome 'João' e imprima
# Use 'in' para verificar se 'João' está no nome

# SOLUÇÃO:
# nomes = ['João Silva', 'Maria Santos', 'João Pereira', 'Pedro Silva']
# busca = 'João'
# for nome in nomes:
#     if busca in nome:
#         print(nome)


# Exercício 4.5: Buscar em dicionário com estrutura de controle
# Dicionário de produtos com estoque:
# {"Notebook": 5, "Mouse": 15, "Teclado": 0, "Monitor": 3, "Webcam": 8}
# Procure por produtos que estão COM ESTOQUE (quantidade > 0)
# Imprima o produto e a quantidade

# SOLUÇÃO:
# estoque = {"Notebook": 5, "Mouse": 15, "Teclado": 0, "Monitor": 3, "Webcam": 8}
# for produto, quantidade in estoque.items():
#     if quantidade > 0:
#         print(f"{produto}: {quantidade} unidades")


# Exercício 4.6: Buscar preço de um produto específico em dicionário
# Dicionário: {"notebook": 2500, "mouse": 50, "teclado": 150, "monitor": 800}
# Procure pelo produto 'mouse' e imprima seu preço
# Use if para verificar se a chave existe no dicionário

# SOLUÇÃO:
# precos = {"notebook": 2500, "mouse": 50, "teclado": 150, "monitor": 800}
# produto_busca = 'mouse'
# for chave, valor in precos.items():
#     if chave == produto_busca:
#         print(f"O preço de {chave} é R$ {valor}")


# =====================================================================
# PARTE 5: DESAFIOS INTEGRADOS
# =====================================================================

# Desafio 1: Listar produtos com desconto
# Dicionário: {"camiseta": 80, "calça": 150, "tênis": 250, "meia": 20}
# Use for com if para:
# 1. Listar apenas produtos acima de R$ 100
# 2. Calcular o preço com 15% de desconto
# Resultado esperado:
# calça: R$ 150 -> R$ 127.5
# tênis: R$ 250 -> R$ 212.5

# SOLUÇÃO:
# roupas = {"camiseta": 80, "calça": 150, "tênis": 250, "meia": 20}
# for roupa, preco in roupas.items():
#     if preco > 100:
#         desconto = preco * 0.15
#         preco_final = preco - desconto
#         print(f"{roupa}: R$ {preco} -> R$ {preco_final}")


# Desafio 2: Buscar múltiplas linguagens
# Lista: ['Python', 'Java', 'C++', 'JavaScript', 'Go', 'Ruby', 'Rust']
# Palavras a buscar: 'Python' e 'Go'
# Use for com if para procurar ambas e imprima quantas foi encontrada
# Dica: Use uma lista para armazenar o que buscar

# SOLUÇÃO:
# linguagens = ['Python', 'Java', 'C++', 'JavaScript', 'Go', 'Ruby', 'Rust']
# buscar = ['Python', 'Go']
# for linguagem in linguagens:
#     if linguagem in buscar:
#         print(f"Encontrei: {linguagem}")


# Desafio 3: Relatório de vendas
# Dicionário com vendas por mês:
# vendas = {"Janeiro": 1500, "Fevereiro": 2000, "Março": 1800, "Abril": 2500}
# Use for para:
# 1. Imprimir cada mês e sua venda
# 2. Identificar o mês com maior venda
# 3. Calcular o total de vendas

# SOLUÇÃO:
# vendas = {"Janeiro": 1500, "Fevereiro": 2000, "Março": 1800, "Abril": 2500}
# total = 0
# maior_venda = 0
# melhor_mes = ""
# for mes, venda in vendas.items():
#     print(f"{mes}: R$ {venda}")
#     total += venda
#     if venda > maior_venda:
#         maior_venda = venda
#         melhor_mes = mes
# print(f"Total: R$ {total}")
# print(f"Melhor mês: {melhor_mes} com R$ {maior_venda}")


# =====================================================================
# DICAS IMPORTANTES
# =====================================================================
# 1. Sempre use nomes descritivos para variáveis no for
#    ✓ for aluno in alunos_lista
#    ✗ for x in lista
#
# 2. Range sempre vai do início até fim-1 (não inclui o fim)
#    range(0, 10) = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 (não inclui 10)
#
# 3. Use .items() para acessar chave E valor de um dicionário
#    for chave, valor in dicionario.items()
#
# 4. Use if dentro do for para filtrar e pesquisar dados
#    if condição:
#        fazer algo
#
# 5. Use break para sair do loop quando encontrar o que busca
#    if elemento_encontrado:
#        break
# =====================================================================
