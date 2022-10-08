import random


def modo_jogo(inEscolha):
    nome2 = "BOT"
    if not 1 <= inEscolha <= 2:
        while not 1 <= inEscolha <= 2:
            print("\nEscolha inválida!")
            inEscolha = int(input("Opções de jogo:\n"
                                  "(1) - JxJ (Jogador x Jogador)\n"
                                  "(2) - Contra o computador\n"
                                  "Escolha: "))

    if inEscolha == 1:
        nome2 = str(input("Digite o nome do segundo jogador: "))
        return nome2

    elif inEscolha == 2:
        return nome2


def validar_palitos(x):
    while x % 2 == 0 or not 5 <= x < 40:
        x = int(input("Digite um valor válido: "))

    return x


def retirar_palitos():
    min_p = 0
    max_p = 0
    min_max = []
    while not 1 <= min_p <= 4:
        min_p = int(input("Digite um valor mínimo válido de palitos a serem retirados por rodada (1 - 4): "))
    min_max.append(min_p)
    while not 1 <= max_p <= 4 or max_p < min_max[0]:
        max_p = int(input(f"Digite um valor máximo válido de palitos a serem"
                          f" retirados por rodada ({min_max[0]} - 4): "))
    min_max.append(max_p)

    return min_max


def startp_p(quant_p, players, minim, maxi):
    win_los = []
    perdeu = False
    i = 0
    # Enquanto ninguém perdeu, o código será executado
    while not perdeu:
        # Quando i chegar em 2, ele vai virar 0 de novo
        # Tentei usar o for, mas quando a jogada era inválida dava ruim
        if i == 2:
            i = 0
        # Multiplica a string com | pela quantidade de palitos (pode ser mudado depois, apenas uma ideia)
        print(f'Palitos restantes:'.center(50))
        print_p = "| " * quant_p
        print(print_p.center(50))
        print(f'({quant_p})'.center(50))
        # Pede quantos palitos o jogador quer tirar
        x = int(input(f"Quantos palitos você deseja retirar, {players[i]}? "))
        # Validação da jogada
        if x < minim or x > maxi:
            print("Jogada inválida!".center(50))
            continue
        # Retira os palitos de acordo com a jogada
        quant_p -= x
        # Gambiarra para separar o vencedor do perdedor
        if quant_p == 0:
            print(f'{players[i]} retirou o último palito\n'
                  f'Fim de jogo!')
            if i == 1:
                win_los = [0, 1]
            else:
                win_los = [1, 0]
            perdeu = True
        elif minim >= quant_p:
            print(f'Quantidade mínima a ser retirada maior ou igual que o restante de palitos!\n'
                  f'Fim de jogo!')
            if i == 1:
                win_los = [1, 0]
            else:
                win_los = [0, 1]
            perdeu = True
        i += 1
    # Retorna a lista com os índices do vencedor (1) e perdedor (0)
    return win_los


def startp_b(quant_p, players, minim, maxi):
    win_los = []
    perdeu = False
    i = 0
    while not perdeu:
        if i == 2:
            i = 0
        print(f'Palitos restantes:'.center(50))
        print_p = "| " * quant_p
        print(print_p.center(50))
        print(f'({quant_p})'.center(50))
        # Pede quantos palitos o jogador quer tirar
        if i == 0:
            x = int(input(f"Quantos palitos você deseja retirar, {players[i]}? "))
        else:
            x = random.randint(minim, maxi)
            if x < minim or x > maxi:
                continue
            print(f"o BOT removeu {x} palitos".center(50))
        # Validação da jogada
        if x < minim or x > maxi:
            print("Jogada inválida!".center(50))
            continue
        quant_p -= x
        if quant_p == 0:
            print(f'{players[i]} retirou o último palito\n'
                  f'Fim de jogo!')
            if i == 1:
                win_los = [0, 1]
            else:
                win_los = [1, 0]
            perdeu = True
        elif minim >= quant_p:
            print(f'Quantidade mínima a ser retirada maior ou igual que o restante de palitos!\n'
                  f'Fim de jogo!')
            if i == 1:
                win_los = [1, 0]
            else:
                win_los = [0, 1]
            perdeu = True
        i += 1
    return win_los
