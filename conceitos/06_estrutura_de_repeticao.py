
# USAMOS PARA REPITIR UM BLOCO DE CÓDIGOS
# ENQUANTO UMA CONDIÇÃO FOR VERDADEIRA
# O INTUITO DO USO É PRINCIPALMENTE BUSCAR DADOS DE LISTAS E DICIONÁRIOS


# === FORMAS DE ITERAR SOBRE LISTAS ===
#           0        1        2       3
alunos_lista = ['Maria', 'João', 'Pedro', 'Ana', 'Lucas', 'Carla', 'Rafael', 'Fernanda', 'Gustavo', 'Camila']

for aluno in alunos_lista:
    print(aluno)

# busca os dados da lista, mas tem controle sobre o índice
# i = indice
# range(início, fim, somador)
for i in range(0, 10, 2):
    print( i, alunos_lista[i] )

# === FORMAS DE ITERAR SOBRE DICIONÁRIOS ===

alunos_dicionario = {
    "aluno1": "Maria",
    "aluno2": "João",
    "aluno3": "Pedro",
    "aluno4": "Ana",
    "aluno5": "Lucas",
    "aluno6": "Carla",
    "aluno7": "Rafael",
    "aluno8": "Fernanda",
    "aluno9": "Gustavo",
    "aluno10": "Camila"
}

# 1. ACESSAR APENAS AS CHAVES
for chave in alunos_dicionario:
    print(chave)

# 2. ACESSAR APENAS OS VALORES
for valor in alunos_dicionario.values():
    print(valor)

# 3. ACESSAR CHAVE E VALOR JUNTOS (MAIS ÚTIL)
for chave, valor in alunos_dicionario.items():
    print(chave, valor)


## EXEMPLOS DE USO
print(" ")
print(" ")
print("======= EXEMPLOS =======")

paises = ["Brasil", "Argentina", "Chile", "Uruguai", "Paraguai", "Colômbia", "Peru", "Venezuela", "Equador", "Bolívia"]

for pais in paises:
    if pais == "Equador":
        print(pais, "Encontrei o equador")
    else:
        print(pais, "Não é o equador")



alunos = [
    {
        "nome_completo": "Luan Fagioni",
        "matricula": "123456",
        "serie": "2º",
        "turno": "matutino",
        "situacao": "pendente",
        "notas": {
            "portugues": [8.5, 7.0, 9.0],
            "matematica": [9.0, 8.5, 7.5],
            "ciencias": [7.0, 8.0, 9.5]
        }
    },
    {
        "nome_completo": "Maria Silva",
        "matricula": "123457",
        "serie": "2º",
        "turno": "matutino",
        "situacao": "aprovado",
        "notas": {
            "portugues": [9.5, 8.5, 9.0],
            "matematica": [8.0, 9.0, 8.5],
            "ciencias": [9.0, 9.5, 8.0]
        }
    },
    {
        "nome_completo": "João Santos",
        "matricula": "123458",
        "serie": "2º",
        "turno": "vespertino",
        "situacao": "aprovado",
        "notas": {
            "portugues": [7.5, 8.0, 7.5],
            "matematica": [8.5, 8.0, 9.0],
            "ciencias": [8.0, 7.5, 8.5]
        }
    },
    {
        "nome_completo": "Ana Costa",
        "matricula": "123459",
        "serie": "2º",
        "turno": "noturno",
        "situacao": "pendente",
        "notas": {
            "portugues": [6.5, 7.0, 7.5],
            "matematica": [7.0, 6.5, 7.0],
            "ciencias": [6.0, 7.0, 6.5]
        }
    }
]


MATRICULA_PESQUISADA = "123457"
for aluno in alunos:
    if aluno["matricula"] == MATRICULA_PESQUISADA:
        print(aluno)
        break
    else:
        print("Aluno não encontrado")

for aluno in alunos:
    nome = aluno["nome_completo"]
    

alunos = [
    {
        "nome_completo": "Luan Fagioni",
        "matricula": "123456",
        "serie": "2º",
        "turno": "matutino",
        "situacao": "pendente",
        "materias": {
            "portugues": {
                "notas": [8.5, 7.0, 9.0],
                "media": 0
            },
            "matematica": {
                "notas": [9.0, 8.5, 7.5],
                "media": 0
            },
            "ciencias": {
                "notas": [7.0, 8.0, 9.5],
                "media": 0
            }
        }
    },
    {
        "nome_completo": "Maria Silva",
        "matricula": "123457",
        "serie": "2º",
        "turno": "matutino",
        "situacao": "aprovado",
        "materias": {
            "portugues": {
                "notas": [9.5, 8.5, 9.0],
                "media": 0
            },
            "matematica": {
                "notas": [8.0, 9.0, 8.5],
                "media": 0
            },
            "ciencias": {
                "notas": [9.0, 9.5, 8.0],
                "media": 0
            }
        }
    },
    {
        "nome_completo": "João Santos",
        "matricula": "123458",
        "serie": "2º",
        "turno": "vespertino",
        "situacao": "aprovado",
        "materias": {
            "portugues": {
                "notas": [7.5, 8.0, 7.5],
                "media": 0
            },
            "matematica": {
                "notas": [8.5, 8.0, 9.0],
                "media": 0
            },
            "ciencias": {
                "notas": [8.0, 7.5, 8.5],
                "media": 0
            }
        }
    },
    {
        "nome_completo": "Ana Costa",
        "matricula": "123459",
        "serie": "2º",
        "turno": "noturno",
        "situacao": "pendente",
        "materias": {
            "portugues": {
                "notas": [6.5, 7.0, 7.5],
                "media": 0
            },
            "matematica": {
                "notas": [7.0, 6.5, 7.0],
                "media": 0
            },
            "ciencias": {
                "notas": [6.0, 7.0, 6.5],
                "media": 0
            }
        }
    },
]

# PRIMEIRO FOR IRA DEVOLVER UMA LISTA/DICIONARIO NOVAMENTE
# NA LISTA DEVOLVIDA PRECISMAOS ACESSAR AS MATERIAS, QUE É UM DICIONÁRIO

for aluno in alunos:
    materias = aluno["materias"]
    
    for materia, dados in materias.items():
        notas = dados["notas"]
        somatorio = 0

        for nota in notas:
            somatorio += nota

        media_calculada = somatorio / len(notas)
        dados["media"] = media_calculada


