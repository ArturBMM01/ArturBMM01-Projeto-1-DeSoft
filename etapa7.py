frota = {}   
nome = ['porta-aviões', 'navio-tanque', 'navio-tanque', 'contratorpedeiro', 'contratorpedeiro', 'contratorpedeiro', 'submarino', 'submarino', 'submarino', 'submarino' ]
tamanho = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

for i in range(9):
    verificacao = False
    
    while verificacao == False:
        print(f'Insira as informações referentes ao navio {nome[i]} que possui tamanho {tamanho[i]}')
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        
        if nome[i] != 'submarino':
            orientacao = int(input('[1] Vertical [2] Horizontal >'))
            
            if orientacao == 1:
                orientacao = 'vertical'
            
            elif orientacao == 2:
                orientacao = 'horizontal'
        
        else:
            orientacao = 'vertical'
        
        verificacao = posicao_valida(frota, linha, coluna, orientacao, tamanho[i])
       
        if verificacao == False:
            print('Esta posição não está válida!')
    
    posicao_final = define_posicoes(linha, coluna, orientacao, tamanho[i])
   
    if nome[i] not in frota:
        frota[nome[i]] = []
    
    frota[nome[i]].append(posicao_final)
   
    print(frota)