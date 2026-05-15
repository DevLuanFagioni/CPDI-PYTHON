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
def imprimir(texto):
    print(texto)

# PARA EXECUTAR A FUNÇÃO, É NECESSÁRIO CHAMÁ-LA PELO NOME
imprimir("Olá, mundo!")
imprimir("Como vai você?")
imprimir("Estou bem, obrigado!")


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


def somar(a, b):
    soma = a + b
    return soma    

resultado = somar(10, 20)
print(resultado)


def calcular_media(lista_notas=[0,0,0]):
    notas = lista_notas
    media = sum(notas) / len(notas)
    return media

notas_aluno = [8.5, 7.0, 9.0]
media_calculada = calcular_media( notas_aluno )

MEDIA_APROVACAO = 7.5
MEDIA_REPROVACAO = 5.0

def verificar_situacao(media):
    if media >= MEDIA_APROVACAO:
        return "Aprovado"
    elif media >= MEDIA_REPROVACAO and media < MEDIA_APROVACAO:
        return "Pendente"
    elif media < MEDIA_REPROVACAO:
        return "Reprovado"
    
situacao_aluno = verificar_situacao(7)

def exemplo(valor):
    if valor > 10:
        return "Valor maior que 10"  
    elif valor == 10:
        return "Valor igual a 10"
    else:
        return 10 / 2

teste = exemplo(15)


def verificar_bolsa(situacao, media):
    if situacao == "aprovado" and media > 9:
        return "Parabens voce ganhou 10% de desconto na materia"
    else: 
        return "-"


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