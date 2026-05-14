"""
ANOTAÇÕES: Operadores
=====================
Módulo sobre operadores aritméticos, de comparação e lógicos.
"""

# ============================================
# 1. OPERADORES ARITMÉTICOS
# ============================================

"""
+ : Adição
- : Subtração
* : Multiplicação
/ : Divisão (retorna float)
// : Divisão inteira
% : Resto (módulo)
** : Potenciação
"""

a = 10
b = 3

print("OPERADORES ARITMÉTICOS:")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")      # 3.3333...
print(f"{a} // {b} = {a // b}")    # 3
print(f"{a} % {b} = {a % b}")      # 1
print(f"{a} ** {b} = {a ** b}")    # 1000


# ============================================
# 2. PRECEDÊNCIA DE OPERADORES
# ============================================

"""
Ordem de precedência (do maior para o menor):
1. ** (potenciação)
2. * / // % (multiplicação, divisão, resto)
3. + - (adição, subtração)

Use parênteses para deixar clara a intenção!
"""

resultado1 = 7.5 + 7.8 + 7.7 / 3
print(f"\n7.5 + 7.8 + 7.7 / 3 = {resultado1}")  # 15.3 + (7.7/3)

resultado2 = (7.5 + 7.8 + 7.7) / 3
print(f"(7.5 + 7.8 + 7.7) / 3 = {resultado2}")  # 22.8 / 3


# ============================================
# 3. OPERADORES DE COMPARAÇÃO
# ============================================

"""
Retornam True ou False
== : Igual
!= : Diferente
> : Maior que
< : Menor que
>= : Maior ou igual
<= : Menor ou igual
"""

media_aluno = 7.0
media_aprovacao = 7.5

print("\nOPERADORES DE COMPARAÇÃO:")
print(f"7.0 == 7.5: {media_aluno == media_aprovacao}")    # False
print(f"7.0 != 7.5: {media_aluno != media_aprovacao}")    # True
print(f"7.0 > 7.5: {media_aluno > media_aprovacao}")      # False
print(f"7.0 < 7.5: {media_aluno < media_aprovacao}")      # True
print(f"7.0 >= 7.5: {media_aluno >= media_aprovacao}")    # False
print(f"7.0 <= 7.5: {media_aluno <= media_aprovacao}")    # True


# ============================================
# 4. OPERADORES LÓGICOS
# ============================================

"""
and: Retorna True se TODAS as condições forem verdadeiras
or:  Retorna True se PELO MENOS UMA condição for verdadeira
not: Inverte o resultado (True vira False e vice-versa)
"""

nome = "ana"
idade = 30
plano = "gratuito"

print("\nOPERADORES LÓGICOS:")

# OR - Retorna True se PELO MENOS UMA condição for verdadeira
verificacao_or = nome == "luan" or nome == "ana" or idade == 20
print(f"nome == 'luan' OR nome == 'ana' OR idade == 20: {verificacao_or}")

# AND - Retorna True se TODAS as condições forem verdadeiras
verificacao_and = nome == "ana" and idade >= 18 and plano == "gratuito"
print(f"nome == 'ana' AND idade >= 18 AND plano == 'gratuito': {verificacao_and}")

# NOT - Inverte o resultado
verificacao_not = not (idade < 18)
print(f"NOT (idade < 18): {verificacao_not}")


# ============================================
# 5. OPERADORES DE ATRIBUIÇÃO
# ============================================

"""
= : Atribuição simples
+= : Adiciona e atribui
-= : Subtrai e atribui
*= : Multiplica e atribui
/= : Divide e atribui
"""

print("\nOPERADORES DE ATRIBUIÇÃO:")

valor = 5
print(f"valor = {valor}")

valor += 3  # Equivalente a: valor = valor + 3
print(f"valor += 3 → {valor}")

valor *= 2  # Equivalente a: valor = valor * 2
print(f"valor *= 2 → {valor}")

valor -= 4  # Equivalente a: valor = valor - 4
print(f"valor -= 4 → {valor}")
