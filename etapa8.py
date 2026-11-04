def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    
    return texto

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_player = posiciona_frota(frota)

jogando = True
posicoes_jogadas = []
posicoes_oponente = []

while jogando == True:
    print(monta_tabuleiros(tabuleiro_player, tabuleiro_oponente))
    posicao_repetida = True
    
    while posicao_repetida == True:
        linha = int(input('Jogador, qual linha deseja atacar? '))
        
        while linha < 0 or linha > 9:
            print('Linha inválida!')
            linha = int(input('Jogador, qual linha deseja atacar? '))
        coluna = int(input('Jogador, qual coluna deseja atacar? '))
       
        while coluna < 0 or coluna > 9:
            print('Coluna inválida!')
            coluna = int(input('Jogador, qual coluna deseja atacar? '))
       
        if [linha, coluna] in posicoes_jogadas:
            print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
      
        else:
            posicao_repetida = False
    posicoes_jogadas.append([linha, coluna])
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False