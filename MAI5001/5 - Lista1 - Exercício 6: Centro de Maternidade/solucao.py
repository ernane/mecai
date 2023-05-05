import csv
import pickle

arquivo_txt = "dados-bebes.txt"
arquivo_bin = "dados-bebes.bin"

class Bebe:
    def __init__(self, data_nascimento, sexo, altura, peso, nome):
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.altura = altura
        self.peso = peso
        self.nome = nome

    def __repr__(self):
        return f"{self.nome} ({self.sexo}), nascido(a) em {self.data_nascimento}, com altura de {self.altura} m e peso de {self.peso} kg."


def total_bebes_por_sexo(bebes):
    total_m = 0
    total_f = 0
    for bebe in bebes:
        if bebe.sexo == "m":
            total_m += 1
        elif bebe.sexo == "f":
            total_f += 1
    return total_m, total_f


def media_peso_por_sexo(bebes):
    soma_peso_m = 0
    soma_peso_f = 0
    total_m = 0
    total_f = 0
    for bebe in bebes:
        if bebe.sexo == "m":
            soma_peso_m += bebe.peso
            total_m += 1
        elif bebe.sexo == "f":
            soma_peso_f += bebe.peso
            total_f += 1
    return soma_peso_m / total_m, soma_peso_f / total_f


def media_altura_por_sexo(bebes):
    soma_altura_m = 0
    soma_altura_f = 0
    total_m = 0
    total_f = 0
    for bebe in bebes:
        if bebe.sexo == "m":
            soma_altura_m += bebe.altura
            total_m += 1
        elif bebe.sexo == "f":
            soma_altura_f += bebe.altura
            total_f += 1
    return soma_altura_m / total_m, soma_altura_f / total_f

bebes = []
with open(arquivo_txt, newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter="|")
    for row in reader:
        data_nascimento, sexo, altura, peso, nome = row
        altura = float(altura)
        peso = float(peso)
        bebe = Bebe(data_nascimento, sexo, altura, peso, nome)
        bebes.append(bebe)
        

# Definir uma lista vazia para armazenar as linhas lidas do arquivo
lista = []

# Abrir o arquivo binário no formato pickle em modo de leitura
with open(arquivo_bin, "rb") as f:
    # Carregar os objetos do arquivo usando o método load do pickle
    while True:
        try:
            linha = pickle.load(f)
            lista.append(linha)
        except EOFError:
            break
            
for i in range(0, len(lista), 5):
    data_nascimento = lista[i]
    sexo = lista[i + 1]
    altura = lista[i + 2]
    peso = lista[i + 3]
    nome = lista[i + 4]
    bebe = Bebe(data_nascimento, sexo, altura, peso, nome)
    bebes.append(bebe)
    

total_m, total_f = total_bebes_por_sexo(bebes)
media_peso_m, media_peso_f = media_peso_por_sexo(bebes)
media_altura_m, media_altura_f = media_altura_por_sexo(bebes)

print(
    f"""Dados dos Bebes Homens:
Total: {total_m}
Media do Peso: {media_peso_m:.2f}
Media da Altura: {media_altura_m:.2f}

Dados dos Bebes Mulheres:
Total: {total_f}
Media do Peso: {media_peso_f:.2f}
Media da Altura: {media_altura_f:.2f}""")