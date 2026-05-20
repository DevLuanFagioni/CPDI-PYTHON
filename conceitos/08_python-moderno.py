# FUNÇÕES ANONIMAS
def funcao_normal(param1, param2):
    print(param1, param2)
    return param1 + param1

variavel = lambda param: param / 10
print( variavel(20) )

# lambda usada dentro de um dicionario o parametro vai referenciar o proprio dicionario 
aluno = {
    "nome": "luan",
    "sobrenome": "fagioni",
    "nomecompleto": lambda d: f"{d['nome']} {d['sobrenome']}",
    "idade": 21,
    "altura": 1.90,
    "peso": 90,
    "imc": lambda d: d["peso"] / (d["altura"] ** 2),
    "notas": [10, 9, 8, 7, 5],
}

def calcular_media(notas):
    return sum(notas) / len(notas)

aluno2 = {
    "nome": "luan",
    "sobrenome": "fagioni",
    "nomecompleto": lambda d: f"{d['nome']} {d['sobrenome']}",
    "idade": 21,
    "altura": 1.90,
    "peso": 90,
    "imc": lambda d: d["peso"] / (d["altura"] ** 2),
    "notas": [10, 9, 8, 7, 5],
    "media": lambda a: sum(a["notas"]) / len(a["notas"]),
    "notas_baixas": lambda a: list( filter(lambda n: n<6, a["notas"]) )
}


# podemos usar dentro de outros metodos como fallback
# map, filter, reduce, sorted




# IF DE UMA LINHA

