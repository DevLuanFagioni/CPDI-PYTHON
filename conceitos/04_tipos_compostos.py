"""
ANOTAÇÕES: Tipos de Dados Compostos
====================================
Módulo sobre Listas e Dicionários (estruturas de dados).
"""

# ============================================
# 1. LISTAS
# ============================================

"""
LISTA: Coleção ordenada de elementos
- Posições começam em 0
- Pode conter diferentes tipos de dados
- Você pode adicionar, remover, alterar elementos
- Sintaxe: [elemento1, elemento2, elemento3, ...]
"""

print("=" * 50)
print("LISTAS")
print("=" * 50)

# Criar uma lista
notas_aluno = [10, 0, 7, 9, 5.5, 9, 8.5, 6, 7.5]
print(f"Lista de notas: {notas_aluno}")

# Acessar elementos (índice começa em 0)
print(f"\nPrimeira nota (índice 0): {notas_aluno[0]}")
print(f"Última nota (índice -1): {notas_aluno[-1]}")
print(f"Quinta nota (índice 4): {notas_aluno[4]}")

# Modificar elementos
notas_aluno[0] = 9.5
print(f"Após modificar primeira nota: {notas_aluno}")

# Operações com listas
print(f"Quantidade de notas: {len(notas_aluno)}")
print(f"Maior nota: {max(notas_aluno)}")
print(f"Menor nota: {min(notas_aluno)}")
print(f"Soma das notas: {sum(notas_aluno)}")
print(f"Média de notas: {sum(notas_aluno) / len(notas_aluno):.2f}")


# ============================================
# 2. DICIONÁRIOS
# ============================================

"""
DICIONÁRIO: Estrutura de dados que armazena pares chave-valor
- Cada chave é única
- Acesso através da chave, não por índice
- Muito útil para armazenar informações estruturadas
- Sintaxe: {"chave1": valor1, "chave2": valor2, ...}
"""

print("\n" + "=" * 50)
print("DICIONÁRIOS")
print("=" * 50)

# Criar um dicionário
usuario = {
    "nome": "Luan",
    "sobrenome": "Fagioni",
    "idade": 30,
    "altura": 1.75,
    "estudante": True,
}

print(f"Usuário: {usuario}")

# Acessar valores
print(f"\nNome: {usuario['nome']}")
print(f"Idade: {usuario['idade']}")

# Adicionar uma nova chave-valor
usuario["plano"] = "gratuito"
usuario["email"] = "luan@gmail.com"

print(f"\nApós adicionar plano e email: {usuario}")

# Modificar um valor
usuario["idade"] = 31
print(f"Após modificar idade: {usuario['idade']}")

# Remover uma chave
del usuario["altura"]
print(f"\nApós remover altura: {usuario}")


# ============================================
# 3. LISTA DE DICIONÁRIOS
# ============================================

"""
NO MUNDO REAL, geralmente usamos ambos em conjunto:
Uma LISTA DE DICIONÁRIOS para armazenar múltiplos registros
"""

print("\n" + "=" * 50)
print("LISTA DE DICIONÁRIOS")
print("=" * 50)

SENHA_PADRAO = '123456'

usuarios = [
    {
        "email": "luan@gmail.com",
        "nome": "Luan",
        "senha": SENHA_PADRAO,
        "bio": "Desenvolvedor Python",
    },
    {
        "email": "ana@gmail.com",
        "nome": "Ana",
        "senha": SENHA_PADRAO,
        "bio": "Analista de dados",
    },
    {
        "email": "carlos@gmail.com",
        "nome": "Carlos",
        "senha": SENHA_PADRAO,
        "bio": "Designer UI/UX",
    },
]

print(f"Total de usuários: {len(usuarios)}")

# Acessar um usuário específico
primeiro_usuario = usuarios[0]
print(f"\nPrimeiro usuário: {primeiro_usuario['nome']} ({primeiro_usuario['email']})")

# Iterar sobre a lista
print("\nTodos os usuários:")
for usuario in usuarios:
    print(f"  - {usuario['nome']}: {usuario['email']}")
