def define_posicoes(linha, coluna, orientacao, tamanho):
    posicao_no_tabuleiro = []
    
    if orientacao == 'vertical':
        
        for i in range(linha, linha+tamanho):
            posicao_no_tabuleiro.append([i,coluna])
    
    elif orientacao == 'horizontal':
        
        for i in range(coluna, coluna+tamanho):
            posicao_no_tabuleiro.append([linha,i])
    
    return posicao_no_tabuleiro

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicao_ocupada = define_posicoes(linha, coluna, orientacao, tamanho)
    
    for j in range(len(posicao_ocupada)):
        
        if posicao_ocupada[j][0] > 9 or posicao_ocupada[j][1] > 9:
           
            return False
        
        if 9<linha<0 or 9<coluna<0:
           
            return False
        
        for navio in frota:
            pos = frota[navio]
           
            for lista in pos:
           
                for i in range(len(lista)):
                    linhas = lista[i][0]
                    colunas = lista[i][1]
           
                    if posicao_ocupada[j][0] == linhas and posicao_ocupada[j][1] == colunas:
           
                        return False
    
    return True