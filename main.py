"""
CENTRAL DE ESTUDOS - Python
============================

ATENÇÃO: Este arquivo foi reorganizado em uma estrutura mais clara!

Suas anotações de estudo agora estão organizadas em:

📖 /conceitos/        - Anotações teóricas de cada conceito
📝 /exemplos/         - Exemplos práticos prontos para executar
🏋️  /exercicios/     - Exercícios para praticar

Para começar:
1. Leia o arquivo README.md (guia completo)
2. Leia o arquivo COMEÇAR_AQUI.md (instruções para iniciantes)
3. Execute: python3 exemplos/main.py
4. Estude os conceitos em ordem (01 → 04)

Boa sorte! 🚀
"""


# CONTROLES DE FLUXO
plano = "abc"

if plano == "plus":
  print("Plano plus")    
elif plano == "pro":     
  print("Plano pro") 
elif plano == "max":
  print("Plano max")
else:
  print("Voce nao tem um plano valido")


campo_nome = ""
campo_email = "ana@gmail.com"
campo_senha = "123456"

if campo_nome != "" and campo_email != "" and campo_senha != "":
    print("Cadastro realizado com sucesso")
else: 
    print("Preencha todos os campos para realizar o cadastro")



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

for aluno in alunos:
    materias = aluno["materias"]
    
    for materia, dados in materias.items():
        notas = dados["notas"]
        somatorio = 0

        for nota in notas:
            somatorio += nota

        media_calculada = somatorio / len(notas)
        dados["media"] = media_calculada


MEDIA_APROVACAO = 7.5
MEDIA_REPROVACAO = 5.0

for aluno in alunos:
    materias = aluno["materias"]

    for materia, dados in materias.items():
        media = dados["media"]

        if media >= MEDIA_APROVACAO:
            dados["situacao"] = "aprovado"
        elif media >= MEDIA_REPROVACAO and media < MEDIA_APROVACAO:
            dados["situacao"] = "recuperacao"
        elif media < MEDIA_REPROVACAO:
            dados["situacao"] = "reprovado"
        else:
            dados["situacao"] = "pendente"


for aluno in alunos:
    print("Nome:", aluno["nome_completo"])
    print("Matrícula:", aluno["matricula"])
    print("Série:", aluno["serie"])
    print("Turno:", aluno["turno"])
    print("Materias:", aluno["materias"])
    print("================================")


for aluno in alunos:
    materias = aluno["materias"]

    for materia, dados in materias.items():

        if dados["situacao"] == "aprovado":
            print("Parabens, voce foi aprovado em: ", materia)

            if dados["media"] >= 9.0:
                print("Parabens voce ganhou uma bolsa para o proximo ano na materia: " , materia)           