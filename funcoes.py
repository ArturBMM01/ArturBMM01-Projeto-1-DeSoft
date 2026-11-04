#_________________________________________QUESTION 1_________________________________________

def define_posicoes(linha, coluna, orientacao, tamanho):
    posicao_no_tabuleiro = []
    
    if orientacao == 'vertical':
        for i in range(linha, linha+tamanho):
            posicao_no_tabuleiro.append([i,coluna])
    
    elif orientacao == 'horizontal':
        for i in range(coluna, coluna+tamanho):
            posicao_no_tabuleiro.append([linha,i])
    
    return posicao_no_tabuleiro


#_________________________________________QUESTION 2_________________________________________

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicao_no_tabuleiro = define_posicoes(linha, coluna, orientacao, tamanho)
    
    if nome_navio not in frota:
        frota[nome_navio] = []
    
    frota[nome_navio].append(posicao_no_tabuleiro)
    
    return frota


#_________________________________________QUESTION 3_________________________________________

def faz_jogada(tabuleiro, linha, coluna):
    
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    
    elif tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    
    return tabuleiro