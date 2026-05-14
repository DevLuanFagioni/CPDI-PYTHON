# AS FUNÇÕES SERVEM PARA ORGANIZAR O CÓDIGO, EVITANDO REPETIÇÕES E MELHORANDO A LEGIBILIDADE
# ELAS SÃO BLOCO DE CÓDIGOS QUE PODEM SER REUTILIZADOS EM VÁRIAS PARTES DO PROGRAMA
# AS FUNÇÕES PODEM RECEBER PARÂMETROS DE ENTRADA E RETORNAR VALORES DE SAÍDA

alunos = [
    {
        "nome_completo": "Luan Fagioni",
        "matricula": "123456",
        "serie": "2º",
        "turno": "matutino",
        "materias": {
            "portugues": {
                "notas": [8.5, 7.0, 9.0],
                "media": 0,
                "situacao": "pendente"
            },
            "matematica": {
                "notas": [9.0, 8.5, 7.5],
                "media": 0,
                "situacao": "pendente"
            },
            "ciencias": {
                "notas": [7.0, 8.0, 9.5],
                "media": 0,
                "situacao": "pendente"
            }
        }
    },
    {
        "nome_completo": "Maria Silva",
        "matricula": "123457",
        "serie": "2º",
        "turno": "matutino",
        "materias": {
            "portugues": {
                "notas": [9.5, 8.5, 9.0],
                "media": 0,
                "situacao": "aprovado"
            },
            "matematica": {
                "notas": [8.0, 9.0, 8.5],
                "media": 0,
                "situacao": "aprovado"
            },
            "ciencias": {
                "notas": [9.0, 9.5, 8.0],
                "media": 0,
                "situacao": "aprovado"
            }
        }
    },
    {
        "nome_completo": "João Santos",
        "matricula": "123458",
        "serie": "2º",
        "turno": "vespertino",
        "materias": {
            "portugues": {
                "notas": [7.5, 8.0, 7.5],
                "media": 0,
                "situacao": "aprovado"
            },
            "matematica": {
                "notas": [8.5, 8.0, 9.0],
                "media": 0,
                "situacao": "aprovado"
            },
            "ciencias": {
                "notas": [8.0, 7.5, 8.5],
                "media": 0,
                "situacao": "aprovado"
            }
        }
    },
    {
        "nome_completo": "Ana Costa",
        "matricula": "123459",
        "serie": "2º",
        "turno": "noturno",
        "materias": {
            "portugues": {
                "notas": [6.5, 7.0, 7.5],
                "media": 0,
                "situacao": "pendente"
            },
            "matematica": {
                "notas": [7.0, 6.5, 7.0],
                "media": 0,
                "situacao": "pendente"
            },
            "ciencias": {
                "notas": [6.0, 7.0, 6.5],
                "media": 0,
                "situacao": "pendente"
            }
        }
    },
]

# NUNCA É EXECUTADA DE INICIO
def imprimir():
    print("OLÁ MUNDO!")

# PARA EXECUTAR A FUNÇÃO, É NECESSÁRIO CHAMÁ-LA PELO NOME
imprimir()
imprimir()
imprimir()


def exibir_alunos():
    for aluno in alunos:
        print("Nome:", aluno["nome_completo"])
        print("Matrícula:", aluno["matricula"])
        print("Série:", aluno["serie"])
        print("Turno:", aluno["turno"])
        print("Materias:", aluno["materias"])
        print("================================")

exibir_alunos()
exibir_alunos()

# NO PYTHON TEMOS FUNÇÕES PRONTAS PARA USAR, COMO A FUNÇÃO TYPE() QUE RETORNA O TIPO DE DADO DE UMA VARIÁVEL

# FUNCOES PRONTAS PARA USAR (GLOBAL)
print()
type()

# FUNÇÕES ESPECIFICAS (LOCAL)
texto = "Olá"
lista = [1, 2, 3]
dicionario = {"chave": "valor"}

texto.upper() # TRANSFORMA O TEXTO EM MAIÚSCULO
lista.append(4) # ADICIONA O ELEMENTO 4 NA LISTA
dicionario.keys() # RETORNA AS CHAVES DO DICIONÁRIO