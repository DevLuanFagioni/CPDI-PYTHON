"""
ANOTAÇÕES: Variáveis
====================
Módulo sobre criação, manipulação e boas práticas com variáveis.
"""

# ============================================
# 1. CRIAR VARIÁVEIS
# ============================================

"""
Uma variável é um espaço na memória que armazena um valor.
Convenção: usar snake_case para nomes (letras minúsculas com underscores)
"""

nome_usuario = "Luan"
sobre_nome_usuario = "Fagioni"
idade_usuario = 30
altura_usuario = 1.75
estudante_usuario = True

print(f"Nome: {nome_usuario}")
print(f"Sobrenome: {sobre_nome_usuario}")
print(f"Idade: {idade_usuario}")
print(f"Altura: {altura_usuario}m")
print(f"Estudante: {estudante_usuario}")


# ============================================
# 2. ACESSAR E MODIFICAR VARIÁVEIS
# ============================================

nome_usuario = "Ana"  # Modificar o valor da variável
nome_completo_usuario = nome_usuario + " " + sobre_nome_usuario

print(f"Nome completo: {nome_completo_usuario}")


# ============================================
# 3. EXEMPLO PRÁTICO: CÁLCULO DE MÉDIA
# ============================================

nota_aluno1 = 8.5
nota_aluno2 = 5.5
nota_aluno3 = 8.0

media_aluno = (nota_aluno1 + nota_aluno2 + nota_aluno3) / 3

print(f"\nNotas: {nota_aluno1}, {nota_aluno2}, {nota_aluno3}")
print(f"Média: {media_aluno:.2f}")


# ============================================
# 4. CONSTANTES
# ============================================

"""
Por convenção, variáveis constantes são escritas em MAIÚSCULAS.
Em Python não há forma de forçar uma variável a ser constante,
mas essa convenção sinaliza que ela não deve ser alterada.
"""

SENHA_PADRAO = '123456'
LIMITE_TENTATIVAS = 3
PI = 3.14159

print(f"\nSenha padrão: {SENHA_PADRAO}")
print(f"Limite de tentativas: {LIMITE_TENTATIVAS}")
print(f"Pi: {PI}")
