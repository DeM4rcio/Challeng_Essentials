from random import randrange

tabuleiro = [[1,2,3],[4,5,6],[7,8,9]]





def display_board(): 
    
    print(f"""
+-------+-------+-------+
|       |       |       |
|   {tabuleiro[0][0]}   |   {tabuleiro[0][1]}   |   {tabuleiro[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {tabuleiro[1][0]}   |   {tabuleiro[1][1]}   |   {tabuleiro[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {tabuleiro[2][0]}   |   {tabuleiro[2][1]}   |   {tabuleiro[2][2]}   |
|       |       |       |
+-------+-------+-------+
    """)
    return
    
 # A função aceita um parâmetro contendo o status atual da placa
 # e o imprime no console.


def enter_move():
    while True:
        draw_move()
        display_board(),
        jogada = int(input("Digite seu movimento"))
        for i in range(len(tabuleiro)):
            for j in range(len(tabuleiro)):
                if jogada == tabuleiro[i][j]:
                    tabuleiro[i][j] = "O"                    
                else:
                     pass
        if victory_for():
            break
        else:
            pass

        
    
    


 # A função aceita o status atual do tabuleiro, pergunta ao usuário sobre sua jogada, 
 # verifica a entrada e atualiza o quadro de acordo com a decisão do usuário.


def make_list_of_free_fields(board):
    

 pass
 #  A função navega pelo tabuleiro e constrói uma lista de todas as casas livres; 
 # a lista consiste em tuplas, enquanto cada tupla é um par de números de linha e coluna.


def victory_for():
    

    # Finalização por linha
    if ([tabuleiro[0][0],tabuleiro[0][1],tabuleiro[0][2]]) == ['X','X','X'] or ['O','O','O']:
        return True
    elif ([tabuleiro[1][0],tabuleiro[1][1],tabuleiro[1][2]]) == ['X','X','X'] or ['O','O','O']:
        return True
    elif ([tabuleiro[2][0],tabuleiro[2][1],tabuleiro[2][2]]) == ['X','X','X'] or ['O','O','O']:
        return True

    #Finalização por coluna
    elif ([tabuleiro[0][0],tabuleiro[1][0],tabuleiro[2][0]]) == ['X','X','X'] or ['O','O','O']:
        return True
    elif ([tabuleiro[0][1],tabuleiro[1][1],tabuleiro[2][1]]) == ['X','X','X'] or ['O','O','O']:
        return True
    elif ([tabuleiro[0][2],tabuleiro[1][2],tabuleiro[2][2]]) == ['X','X','X'] or ['O','O','O']:
        return True


    #Finalização pela diagonal
    elif ([tabuleiro[0][0],tabuleiro[1][1],tabuleiro[2][2]]) == ['X','X','X'] or ['O','O','O']:
        return True
    elif ([tabuleiro[0][2],tabuleiro[1][1],tabuleiro[2][0]]) == ['X','X','X'] or ['O','O','O']:
        return True
    
    else:
        return False

    
    
    
    
    

    
 # A função analisa o estado da placa a fim de verificar se 
 # o jogador usando 'O's ou 'X's ganhou o jogo


def draw_move():
   display_board(),
   

   for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            if randrange(8) == tabuleiro[i][j]:
                tabuleiro[i][j] = "X"  
                             
            else:
                pass

            
 
 # A função desenha o movimento do computador e atualiza o tabuleiro.

print(enter_move())