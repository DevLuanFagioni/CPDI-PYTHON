"""
ANOTAÇÕES: Comentários e Tipos de Dados Primitivos
====================================================
Módulo sobre comentários e tipos de dados básicos em Python.
"""

# ============================================
# 1. COMENTÁRIOS
# ============================================

# COMENTÁRIO DE UMA LINHA
# Tudo após a # é ignorado pelo Python

"""
BLOCO DE COMENTÁRIO
O PYTHON IGNORA TUDO QUE ESTIVER ENTRE AS TRÊS ASPAS DUPLAS
VOCÊ PODE ESCREVER VÁRIAS LINHAS DE COMENTÁRIO
"""


# ============================================
# 2. TIPOS DE DADOS PRIMITIVOS
# ============================================

"""
TIPOS BÁSICOS:
    - TEXTO (STRING): Sequência de caracteres - "Luan", 'Python'
    - NÚMEROS INTEIROS (INT): Números sem decimais - 30, -5, 0
    - NÚMEROS DECIMAIS (FLOAT): Números com decimais - 1.75, 3.14
    - BOOLEANOS (BOOL): Verdadeiro ou Falso - True, False
"""

# Exemplos de tipos primitivos
texto = "Luan"           # String
numero_inteiro = 30      # Int
numero_decimal = 1.75    # Float
booleano = True          # Bool

print(f"Texto: {texto} (tipo: {type(texto)})")
print(f"Inteiro: {numero_inteiro} (tipo: {type(numero_inteiro)})")
print(f"Decimal: {numero_decimal} (tipo: {type(numero_decimal)})")
print(f"Booleano: {booleano} (tipo: {type(booleano)})")


# ============================================
# 3. TIPAGEM DINÂMICA
# ============================================

"""
O Python usa TIPAGEM DINÂMICA:
- Você NÃO precisa declarar o tipo de dado de uma variável
- O tipo é determinado automaticamente pelo valor atribuído
- Uma variável pode mudar de tipo durante a execução
"""

variavel = 10           # Int
print(type(variavel))   # <class 'int'>

variavel = "texto"      # Agora é String
print(type(variavel))   # <class 'str'>

variavel = 3.14         # Agora é Float
print(type(variavel))   # <class 'float'>
