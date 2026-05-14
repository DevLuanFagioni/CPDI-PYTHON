# Exercícios - Estrutura de Repetição (FOR)

**Tópicos:** for in, range(), dicionários e estruturas de controle

---

## PARTE 1: FOR IN - Iterando sobre Listas

### Exercício 1.1: Listar todos os produtos

Crie uma lista com 5 produtos e imprima cada um deles usando `for in`.

**Resultado esperado:** Cada produto em uma linha

<details>
<summary>Solução</summary>

```python
produtos = ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Webcam']
for produto in produtos:
    print(produto)
```

</details>

---

### Exercício 1.2: Somar elementos de uma lista

Crie uma lista com 5 números e use `for in` para somar todos eles.

**Dica:** Use uma variável acumuladora

<details>
<summary>Solução</summary>

```python
numeros = [10, 20, 30, 40, 50]
total = 0
for numero in numeros:
    total += numero
print(f"Total: {total}")
```

</details>

---


## PARTE 2: Entendendo RANGE()

> **Sintaxe:** `range(inicio, fim, passo)`
> - **inicio**: por onde começa (padrão: 0)
> - **fim**: até onde vai (NÃO INCLUI o fim)
> - **passo**: de quanto em quanto salta (padrão: 1)

### Exercício 2.1: Range básico

Use `range(10)` para imprimir os números de 0 a 9.

<details>
<summary>Solução</summary>

```python
for numero in range(10):
    print(numero)
```

</details>

---

### Exercício 2.2: Range com início e fim

Use `range(5, 15)` para imprimir os números de 5 a 14.

<details>
<summary>Solução</summary>

```python
for numero in range(5, 15):
    print(numero)
```

</details>

---

### Exercício 2.3: Range com passo

Use `range(0, 20, 2)` para imprimir números pares de 0 a 18.

<details>
<summary>Solução</summary>

```python
for numero in range(0, 20, 2):
    print(numero)
```

</details>

---

## PARTE 3: Iterando sobre Dicionários - Chave e Valor

### Exercício 3.1: Acessar chaves e valores de um dicionário

Dado o dicionário de alunos com suas notas:
```python
alunos_notas = {"Maria": 8.5, "João": 7.0, "Pedro": 9.5, "Ana": 8.0}
```

Use `for` com `.items()` para imprimir cada aluno e sua nota.

**Resultado esperado:**
```
Maria tem nota 8.5
João tem nota 7.0
```

<details>
<summary>Solução</summary>

```python
alunos_notas = {"Maria": 8.5, "João": 7.0, "Pedro": 9.5, "Ana": 8.0}
for aluno, nota in alunos_notas.items():
    print(f"{aluno} tem nota {nota}")
```

</details>

---

### Exercício 3.2: Converter valores de um dicionário

Dado o dicionário de preços: `{"notebook": 2500, "mouse": 50, "teclado": 150}`

Use `for` com `.items()` para aplicar 10% de desconto em cada item.

Imprima o novo preço de cada produto.

**Resultado esperado:**
```
notebook: R$ 2250.0
mouse: R$ 45.0
```

<details>
<summary>Solução</summary>

```python
precos = {"notebook": 2500, "mouse": 50, "teclado": 150}
desconto = 0.10
for produto, preco in precos.items():
    novo_preco = preco - (preco * desconto)
    print(f"{produto}: R$ {novo_preco}")
```

</details>

---

## PARTE 4: Estrutura de Controle dentro do FOR (Pesquisa de Dados)

### Exercício 4.1: Buscar um elemento específico em uma lista

Lista: `['Python', 'Java', 'JavaScript', 'C++', 'Go']`

Procure pela linguagem 'Java' e imprima uma mensagem se encontrar.

Use `if` dentro do `for`.

<details>
<summary>Solução</summary>

```python
linguagens = ['Python', 'Java', 'JavaScript', 'C++', 'Go']
busca = 'Java'
for linguagem in linguagens:
    if linguagem == busca:
        print(f"Encontrei {busca}!")
        break
```

</details>

---

### Exercício 4.2: Filtrar números maiores que um valor

Lista: `[5, 12, 8, 25, 3, 18, 30, 7]`

Use `for` com `if` para imprimir apenas os números maiores que 15.

<details>
<summary>Solução</summary>

```python
numeros = [5, 12, 8, 25, 3, 18, 30, 7]
limite = 15
for numero in numeros:
    if numero > limite:
        print(numero)
```

</details>

---

## PARTE 5: Desafios

### Desafio 1: Listar produtos com desconto

Dicionário: `{"camiseta": 80, "calça": 150, "tênis": 250, "meia": 20}`

Use `for` com `if` para:
1. Listar apenas produtos acima de R$ 100
2. Calcular o preço com 15% de desconto

**Resultado esperado:**
```
calça: R$ 150 -> R$ 127.5
tênis: R$ 250 -> R$ 212.5
```

<details>
<summary>Solução</summary>

```python
roupas = {"camiseta": 80, "calça": 150, "tênis": 250, "meia": 20}
for roupa, preco in roupas.items():
    if preco > 100:
        desconto = preco * 0.15
        preco_final = preco - desconto
        print(f"{roupa}: R$ {preco} -> R$ {preco_final}")
```

</details>

---

### Desafio 2: Buscar múltiplas linguagens

Lista: `['Python', 'Java', 'C++', 'JavaScript', 'Go', 'Ruby', 'Rust']`

Palavras a buscar: 'Python' e 'Go'

Use `for` com `if` para procurar ambas e imprima quando encontrar.

**Dica:** Use uma lista para armazenar o que buscar

<details>
<summary>Solução</summary>

```python
linguagens = ['Python', 'Java', 'C++', 'JavaScript', 'Go', 'Ruby', 'Rust']
buscar = ['Python', 'Go']
for linguagem in linguagens:
    if linguagem in buscar:
        print(f"Encontrei: {linguagem}")
```

</details>

---

### Desafio 3: Relatório de vendas

Dicionário com vendas por mês:
```python
vendas = {"Janeiro": 1500, "Fevereiro": 2000, "Março": 1800, "Abril": 2500}
```

Use `for` para:
1. Imprimir cada mês e sua venda
2. Identificar o mês com maior venda
3. Calcular o total de vendas

<details>
<summary>Solução</summary>

```python
vendas = {"Janeiro": 1500, "Fevereiro": 2000, "Março": 1800, "Abril": 2500}
total = 0
maior_venda = 0
melhor_mes = ""
for mes, venda in vendas.items():
    print(f"{mes}: R$ {venda}")
    total += venda
    if venda > maior_venda:
        maior_venda = venda
        melhor_mes = mes
print(f"Total: R$ {total}")
print(f"Melhor mês: {melhor_mes} com R$ {maior_venda}")
```

</details>

---

##  Dicas Importantes

### 1. Use nomes descritivos nas variáveis do `for`
```python
✓ for aluno in alunos_lista:
✗ for x in lista:
```

### 2. `range()` vai do início até fim-1 (não inclui o fim)
```python
range(0, 10) = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 
# Não inclui o 10
```

### 3. Use `.items()` para acessar chave E valor de um dicionário
```python
for chave, valor in dicionario.items():
    # Aqui você tem acesso a chave e valor
```

### 4. Use `if` dentro do `for` para filtrar e pesquisar dados
```python
for elemento in lista:
    if condicao:
        # fazer algo
```

### 5. Use `break` para sair do loop quando encontrar o que busca
```python
for elemento in lista:
    if elemento_encontrado:
        break  # Sai do loop imediatamente
```

---

**Bom estudo! 🎓**
