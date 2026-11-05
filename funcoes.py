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


#_________________________________________QUESTION 4_________________________________________

def posiciona_frota(frota):

    resultado = (
[
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
    )

    for navio in frota:
        posicao = frota[navio]

        for lista in posicao:

            for i in range(len(lista)):
                linha = lista[i][0]
                coluna = lista[i][1]
                resultado[linha][coluna] = 1
    
    return resultado


#_________________________________________QUESTION 5_________________________________________

def afundados(frota, tabuleiro):
    afundado = 0
    
    for navio in frota:
        pos = frota[navio]
        
        for lista in pos:
            soma = 0
            
            for i in range(len(lista)):
                linha = lista[i][0]
                coluna = lista[i][1]
                
                if tabuleiro[linha][coluna] == 'X':
                    soma +=1
           
            if soma == len(lista):
                afundado +=1
   
    return afundado


#_________________________________________QUESTION 6_________________________________________

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


#_________________________________________QUESTION 7_________________________________________
#____________________________________código_no_programa.py___________________________________

#_________________________________________QUESTION 8_________________________________________

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    
    return texto

#_________________________________________QUESTION 9_________________________________________
#____________________________________código_no_programa.py___________________________________
