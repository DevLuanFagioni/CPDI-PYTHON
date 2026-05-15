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
                "notas": [9.0, 9.5, 9.5],
                "media": 0,
                "situacao": "pendente"
            }
        }
    },
]

MEDIA_APROVACAO = 7.5
MEDIA_REPROVACAO = 5.0

def calcular_media(notas):
    media = sum(notas) / len(notas)
    return media

def verificar_situacao(media):
    if media >= MEDIA_APROVACAO:
        return "aprovado"
    elif media >= MEDIA_REPROVACAO and media < MEDIA_APROVACAO:
        return "recuperacao"
    elif media < MEDIA_REPROVACAO:
        return "reprovado"
    else:
        return "pendente"

def verificar_bolsa(situacao, media):
    if situacao == "aprovado" and media > 9:
        return "Parabens voce ganhou 10% de desconto na materia" 
    else: 
        return "-"

for aluno in alunos:
    materias = aluno["materias"]
    
    for materia, dados in materias.items():
        media_calculada = calcular_media( dados["notas"] )
        dados["media"] = media_calculada

        situacao = verificar_situacao( dados["media"] )
        dados["situacao"] = situacao

        mensagem = verificar_bolsa( dados["situacao"], dados["media"] )
        dados["observacao"] = mensagem
