def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicao_no_tabuleiro = define_posicoes(linha, coluna, orientacao, tamanho)
    
    if nome_navio not in frota:
        frota[nome_navio] = []
    
    frota[nome_navio].append(posicao_no_tabuleiro)
    
    return frota