from difflib import SequenceMatcher

# Lê o número de palavras do dicionário
n = int(input())

# Lê as palavras do dicionário e armazena em uma lista
dicionario = []
for i in range(n):
    palavra = input()
    dicionario.append(palavra)

# Lê a palavra-chave que foi digitada com erro
palavra_chave = input()

# Define o número mínimo de letras que precisam ser iguais para considerar uma palavra parecida
porcentagem_minima = 0.65
porcentagem_maxima = 0.79

# Inicializa uma lista para armazenar as palavras parecidas encontradas
palavras_parecidas = []

# Percorre o dicionário e verifica se cada palavra é parecida com a palavra-chave
for palavra in dicionario:
    # Usa a função SequenceMatcher da biblioteca difflib para comparar as strings
    semelhanca = SequenceMatcher(None, palavra_chave, palavra).ratio()
    # print(semelhanca, palavra)
    if semelhanca >= porcentagem_minima and semelhanca <= porcentagem_maxima:
        if palavra != palavra_chave:
            palavras_parecidas.append(palavra)

# Ordena a lista de palavras parecidas em ordem alfabética
palavras_parecidas.sort()

# Imprime as palavras parecidas encontradas
for palavra in palavras_parecidas:
    print(palavra)
