# Importa o outro arquivo py com as funções (como uma biblioteca)
import functions

# Lista para colocar o nome dos dois jogadores
players = []
# Lista para colocar no primeiro índice o perdedor e segundo o vencedor
win_los = []
# Pede o nome do primeiro jogador
player1 = str(input("Digite seu nome: "))
# Adiciona na lista o primeiro jogador
players.append(player1)
print("Bem-vindo ao NIM".center(60, '='))
# Faz o input do modo de jogo
inModo = int(input("Opções de jogo:\n"
                   "(1) - JxJ (Jogador x Jogador)\n"
                   "(2) - Contra o computador\n"
                   "Escolha: "))

# Chama a função para definir o nome do segundo jogador (1- (nome) ou 2- BOT
player2 = functions.modo_jogo(inModo)
# Adiciona o nome do segundo jogador
players.append(player2)
# Pede a quantidade de palitos que terão no jogo
quantidade_palitos = int(input("Quantos palitos serão utilizados? Ímpar e  entre 5 - 39: \n"))
# Chama a função para validar a quantidade de palitos
quantidade_palitos = functions.validar_palitos(quantidade_palitos)
# Chama a função para ver o mínimo e máximo de palitos que serão retirados em cada rodada
retirar_palitos = functions.retirar_palitos()
# Armazena em duas variáveis o mínimo e máximo
minim = retirar_palitos[0]
maxi = retirar_palitos[1]

# Aqui separa as duas funções, uma para o JxJ e outra para jogar contra o computador
if inModo == 1:
    win_los = functions.startp_p(quantidade_palitos, players, minim, maxi)
# Aqui será a função (no arquivo functions.py) para fazer o jogo contra o computador
# OBS: pode fazer ctrl c + ctrl v no código da função JxJ e adaptar
# Nome da função é startp_b
else:
    win_los = functions.startp_b(quantidade_palitos, players, minim, maxi)

winner = win_los[0]
loser = win_los[1]
print(f'Vencedor: {players[winner]}\n'
      f'Perdedor: {players[loser]}')
with open("vencedores.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
                  f"Vencedor: {players[winner]}\nPerdedor: {players[loser]}\n"
                  "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
