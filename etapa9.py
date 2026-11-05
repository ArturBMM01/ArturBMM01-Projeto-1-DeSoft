 else:
    linha_oponente = random.randint(0,9)
    coluna_oponente = random.randint(0,9)
        
    while [linha_oponente, coluna_oponente] in posicoes_oponente:
        linha_oponente = random.randint(0,9)
        coluna_oponente = random.randint(0,9)
        
    posicoes_oponente.append([linha_oponente, coluna_oponente])
    print(f'Seu oponente está atacando na linha {linha_oponente} e coluna {coluna_oponente}')
    tabuleiro_player = faz_jogada(tabuleiro_player, linha_oponente, coluna_oponente)
        
    if afundados(frota, tabuleiro_player) == 10:
        print('Xi! O oponente derrubou toda a sua frota =(')
        jogando = False