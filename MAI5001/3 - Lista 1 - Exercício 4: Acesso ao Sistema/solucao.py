jogada = input()


def ganhou(tabuleiro):
    for i in range(3):
        resultado_linhas = tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == "x"
        if resultado_linhas:
            return True
        
    for i in range(3):
        resultado_colunas = tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == "x"
        if resultado_colunas:
            return True
        
    diagonal1 = tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == "x"
    diagonal2 = tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == "x"

    if diagonal1 or diagonal2:
        return True
    
    return False


tabuleiro = []
for linha in jogada.split("|"):
    if len(linha) > 0:
        data = list(linha)
        tabuleiro.append([data[0], data[2], data[4]])
        
        
resultado = ganhou(tabuleiro)

if resultado:
    print("x ganhou")
else:
    print("x perdeu")