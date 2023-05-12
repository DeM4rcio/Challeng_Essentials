from random import randrange

tabuleiro = [[1,2,3],[4,"X",6],[7,8,9]]





def display_board(): 
    
    return print(f"""
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
    
    
 # A função aceita um parâmetro contendo o status atual da placa
 # e o imprime no console.


def enter_move():
 ok = False # suposição falsa - precisamos dela para entrar no loop
 while not ok:
    jogada = input("Digite seu movimento: ")

    ok = len(jogada) == 1 and jogada >= '1' and jogada <= '9' # a entrada do usuário é válida?
    if not ok:
        print("Movimento ruim - repita sua entrada!") # não, não é - faça a entrada novamente
        continue

    jogada = int(jogada) - 1 # número da célula de 0 a 8
    row = jogada // 3 # linha da célula
    col = jogada % 3 # coluna da célula
    sign = tabuleiro[row][col] # verifique o quadrado selecionado
    ok = sign not in ['O','X']

    if not ok: # está ocupado - para a entrada novamente
        print("Campo já ocupado - repita sua entrada!")
        continue
    tabuleiro[row][col] = 'O' # definir '0' no quadrado selecionado
    print(tabuleiro)
    
    


 # A função aceita o status atual do tabuleiro, pergunta ao usuário sobre sua jogada, 
 # verifica a entrada e atualiza o quadro de acordo com a decisão do usuário.


def make_list_of_free_fields():
    vazio = []
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            if tabuleiro[i][j] not in ['O','X']: # o celular está livre?
                vazio.append(tabuleiro[i][j])
    return vazio


 
 #  A função navega pelo tabuleiro e constrói uma lista de todas as casas livres; 
 # a lista consiste em tuplas, enquanto cada tupla é um par de números de linha e coluna.


def play():
    while True :
        display_board();
        enter_move();
        draw_move();
        if victory_for()== True:
            print("Vencedor!")
            break
        else:
            pass

def victory_for():
    condicao = False

    for rc in range(3):
        if tabuleiro[rc][0] == ("X" or "O") and tabuleiro[rc][1] == ("X" or "O") and tabuleiro[rc][2] == ("X" or "O"): # verificar linha rc
            print("foi aqui 1")
            condicao = True
        elif tabuleiro[0][rc] == ("X" or "O") and tabuleiro[1][rc] == ("X" or "O") and tabuleiro[2][rc] == ("X" or "O"): # verificar coluna rc
            condicao = True
            print("foi aqui 2")
        elif tabuleiro[0][0] == ("X" or "O") and tabuleiro[1][1] == ("X" or "O") and tabuleiro[2][2] == ("X" or "O"): # verificar 1ª diagonal
            condicao = True
            print("foi aqui 3")
        elif tabuleiro[0][2] == ("X" or "O") and tabuleiro[1][1] == ("X" or "O") and tabuleiro[2][0] == ("X" or "O"): # verifique 2ª diagonal
            condicao = True
            print("foi aqui 4")
        
        
    return condicao
    
    
    
    
    

    
 # A função analisa o estado da placa a fim de verificar se 
 # o jogador usando 'O's ou 'X's ganhou o jogo


def draw_move():
        display_board()
        confirmacao = True
        while confirmacao:
            jogada_bot = randrange(1,10)
        
            for i in range(len(tabuleiro)):
                    for j in range(len(tabuleiro)):  
                        
                        if jogada_bot == tabuleiro[i][j]:
                            tabuleiro[i][j] = "X"
                            confirmacao = False                    
                        else:
                            pass
            

    
   #for i in range(len(tabuleiro)):
   #     for j in range(len(tabuleiro)):

            

            
 
 # A função desenha o movimento do computador e atualiza o tabuleiro.

print(play())