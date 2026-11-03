def define_posicoes(linha, coluna, orientacao, tamanho):
    posicao_no_tabuleiro = []
    
    if orientacao == 'vertical':
        for i in range(linha, linha+tamanho):
            posicao_no_tabuleiro.append([i,coluna])
    
    elif orientacao == 'horizontal':
        for i in range(coluna, coluna+tamanho):
            posicao_no_tabuleiro.append([linha,i])
    
    return posicao_no_tabuleiro