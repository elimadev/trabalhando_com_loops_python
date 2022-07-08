from re import I

curso = {
    "nome": "Programando em python",
    "conteudos": [
        "Conceitos básicos da linguagem",
        "Biblioteca-padrão",
        "Coleções",
        "Estruturas de controle",
        "Funções e módulos",
        "Parâmetros default, variáveis e nomeados",
        "Programação funcional",
        "Classes e Objetos",
        "Herança e Polimorfismo",
        "Armazenamento de dados em arquivos",
        "Acesso a banco de dados",
        "Manipulação de API Rest",
        "Testes unitários"
    ],
    "instrutor": {
        "Nome": "Júlio Pereira",
        "Contato": "33 99154-2651"
    },
    "alunos": [
        "Aldair Ribeiro",
        "André de Castro",
        "Danilo Pereira",
        "Elton Lima",
        "Fabio Ferraz",
        "Gideão Sudario",
        "Jefferson André",
        "Jeova Vieira",
        "Lucas Pires",
        "Marcelo São Pedro",
        "Meggy Mendes",
        "Michael Rochumback",
        "Nilza Ferreira",
        "Paulo Sergio"
    ]
}

# ========= USANDO  APENAS METHODOS, IF OU LIST COMPREENSHIONS

# CRIAR OS CONJUNTOS

# 1 - Lista de todas as keys do curso
#chaves_curso = [k for k in curso.keys()]
#print(chaves_curso)

# Correção: 
chaves_curso = [k for k in curso]
print(chaves_curso)
print()

# 2 - Lista de tuplas para criar 5 relacionamento entre os alunos
# Correção: 
# RESPOSTA => [(1,2), (3,5), (7,9), (2,2), (3,6)]
import random

num_a = random.sample(range(5), k=1)
num_b = random.sample(range(5), k=1)

rel = [(num_a[0], num_b[0]) for x in range(5)]
print(rel)
print()


# 3 - Lista com os nomes dos alunos
# nomes_alunos = [nome for nome in curso.get('alunos')]
# print(nomes_alunos)
# Correção: 
alunos = [x for x in curso['alunos']]
print(alunos)
print()

# 4 - Lista com os nomes dos alunos MOSTRANDO APENAS AS TRÊS PRIMEIRAS LETRAS
# Correção: 
alunos_3_letras = [x[0:3] for x in curso['alunos']]
print(alunos_3_letras)
print()

"""
DICA
texto = 'Julio'
print(texto[1:4]) # Imprime uli
"""

# 5 - Lista de conteudos que COMECA COM A LETRA A
#alunos_com_a = [nomes_a for nomes_a in curso.get('alunos') if nomes_a.startswith('A')]
#print(alunos_com_a)
# Correção: 
conteudo_a = [x for x in curso['conteudos'] if x[0] == 'A' or x[0] == 'A']
print(conteudo_a)
print()

# ========= USANDO APENAS METHODOS, IF OU WHILE

conteudo_while = []

# 1 - Preencher o conjunto conteudo_while com uma lista de dicionarios dos conteudos conforme o exemplo:
# Exemplo: [{nome: "Conceitos básicos da linguagem", active: True}]

'''
i = 0
while i < len(curso.get('conteudos')):
    conteudo_while.append()
    i += 1
print(conteudo_while)
'''    
# Correção: 
x = 0
while x < len(curso['conteudos']):
    conteudo_while.append({'nome': curso['conteudos'][x], 'active': True})
    x += 1
print(conteudo_while)
print()

# ========= USANDO APENAS METHODOS, IF OU FOR

curso_for = {}
alunos_for = []
conteudos_for = []
instrutor_for = {}

# 1 - preenche a coleção curso_for com os dados do curso e acrecenta o atributo active com valor true
for x in curso.items():
    curso_for[x[0]] = x[1]
curso_for['active'] = True
print(curso_for)
print()

# 2 - preenche a coleção alunos_for com os nomes dos alunos.
#for nomes in curso.get('alunos'):
#    alunos_for.append(nomes)
#print(alunos_for)
# Correção:
for x in curso['alunos']:
    alunos_for.append(x)
print(alunos_for)
print()

# 3 - preenche a coleção conteudos_for com os dados dos conteudos.
#for conteudo in curso.get('conteudos'):
#    conteudos_for.append(conteudo)
#print(conteudos_for)
# Correção:
for x in curso['conteudos']:
    conteudos_for.append(x)
print(conteudos_for)
print()

    
# 4 - preenche a coleção instrutor_for com os dados dos instrutor e acrecentar os meios de contatos
#for instrutor in curso.get('instrutor'):
#    instrutor_for['nome'].appen(instrutor)  
#print(instrutor_for)
# Correção:
for x in curso['instrutor'].items():
    instrutor_for[x[0]] = x[1]
instrutor_for['GitHub'] = 'http://github.com'
print()

# 5 - faça uma busca na coleção curso_for e imprime apenas os dados do instrutor
for x in curso_for['instrutor'].items():    
    print(x)
print()    


# 6 - faça uma busca na coleção alunos e imprime o aluno com index 5
for x in alunos_for:
    if x == alunos_for[5]:
        print(x)
print()


# 7 - Faça uma leitura na coleção conteudos_for ALTERANDO todos conteudos a partir do index 6 para "NÃO APLICADO"
for x in conteudos_for:
    if conteudos_for.index(x) > 5:
        conteudos_for[conteudos_for.index(x)] = 'NAO APLICADO'
print(conteudos_for)
print()