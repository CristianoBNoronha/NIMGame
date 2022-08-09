
# computador_escolhe_jogada(n, m) recebe os valores n, m, e calcula e devolve o valor da jogada do computador.
# computador_escolhe_jogada(n, m) calcula o valor da jogada seguindo o cálculo da estratégia vencedora.
def computador_escolhe_jogada(n, m):
    comp = 0
    i = m
    while not i - comp == 0:
        if n == m:
            comp = n
            return comp
        else:
            if n < m:
                comp = n                
                return comp
                i = comp
            else:
                if (n - m) % (m + 1) == 0:
                    comp = m
                    return comp
                else:
                    if (n - m) % (m + 1) != 0:
                        if (m + 1) + m == n:
                            comp = m
                            return comp
                        else:
                            while not (m + 1) + comp == n and not comp == 1:
                                comp = m
                                if n - comp < m + 1:
                                    comp = comp - 1
                                    return comp
                                    i = comp
                                else:
                                    if comp == 1:
                                        return comp
                                        i = comp
                                    


# usuario_escolhe_jogada(n, m) recebe os valores de n, m, pede a entrada do valor do usuário.
# usuario_escolhe_jogada(n, n) verifica se a entrada é válida e devolve o valor da jogada do usuário.
def usuario_escolhe_jogada(n, m):
    u = False
    while u != True:
        user = int(input("Quantas peças você vai tirar? "))
        print("")
        if user >= 1 and user <= m and not user < 1 and not user > m:
            return user
            u = True
        else:
            if n < m and user >= 1 and user <= m and not user < 1 and not user > m:
                return user
                u = True
            else:
                print("Oops! Jogada inválida! Tente de novo.")
                print("")
                u = False

# partida() pede a entrada dos dados n, m.
# partida() faz o cálculo e decide quem inicia a partida seguindo a estratŕgia vencedora do computador.
def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada?"))
    print("")
    if m == 1 and n % 2 != 0:
        return maquina_um(n, m)
    else:
        if m == 1 and n % 2 == 0:
            return pessoa_um(n, m)
        else:
            if n % (m + 1) == 0:
                return pessoa_um(n, m)
            else:
                if n % (m + 1) != 0:
                    return maquina_um(n, m)

# maquina_um(n, m) recebe os valores de n, m.
# maquina_um(n, m) chama as funções computador_escolhe_jogada(n, m) e jogador_escolhe_jogada(n, m).
# maquina_um(n, m) imprime o número peças que foram retiradas, e calcula e impriime o número de peças que sobraram na mesa.
# maquina_um(n, m) devolve e imprime o ganhador da partida
def maquina_um(n, m):
    print("Computador começa!")
    print("")
    co = False
    us = True
    cwin = False
    while cwin != True:
        if co == False and us == True:
            comp = computador_escolhe_jogada(n, m)
            if comp == 1:
                n = n - 1
                print("O computador tirou uma peça.")
                if n == 1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                    print("")
                    co = True
                    us = False
                else:
                    if n != 1 and n != 0:
                        print("Agora restam", n, " peças no tabuleiro.")
                        print("")
                        co = True
                        us = False
                    else:
                        if n == 0:
                            print("Fim do jogo! O computador ganhou!")
                            print("")
                            cwin = True
                            return cwin
            else:
                if co == False and us == True:
                    if comp != 1:
                        print("O computador tirou", comp, " peças.")
                        n = n - comp
                        if n == 1:
                            print("Agora resta apenas uma peça no tabuleiro.")
                            print("")
                            co = True
                            us = False
                        else:
                            if n != 1 and n != 0:
                                print("Agora restam", n, " peças no tabuleiro.")
                                print("")
                                co = True
                                us = False
                            else:
                                if n == 0:
                                    print("Fim do jogo! O computador ganhou!")
                                    print("")
                                    cwin = True
                                    return cwin
        else:
            if us == False and co == True:
                user = usuario_escolhe_jogada(n, m)
                if user == 1:
                    n = n - 1
                    print("Voce tirou uma peça.")
                    if n == 1:
                        print("Agora resta apenas uma peça no tabuleiro.")
                        print("")
                        co = False
                        us = True
                    else:
                        if n != 1 and n != 0:
                            print("Agora restam", n, " peças no tabuleiro.")
                            print("")
                            co = False
                            us = True
                else:
                    if us == False and co == True:
                        if user != 1:
                            n = n - user
                            print("Voce tirou", user, " peças.")
                            print("")
                            if n == 1:
                                print("Agora resta apenas uma peça no tabuleiro.")
                                co = False
                                us = True
                            else:
                                if n != 1 and n != 0:
                                    print("Agora restam", n, "peças no tabuleiro.")
                                    print("")
                                    co = False
                                    us = True


# pessoa_um(n, m) recebe os valores de n, m.
# pessoa_um(n, m) chama as funções jogador_escolhe_jogada(n, m) e computador_escolhe_jogada(n, m).
# pessoa_um(n, m) imprime o número peças que foram retiradas, e calcula e impriime o número de peças que sobraram na mesa.
# pessoa_um(n, m) devolve e imprime o ganhador da partida
def pessoa_um(n, m):
    print("Você começa!")
    print("")
    cwin = False
    us = False
    co = True
    while cwin != True:
        if us == False and co == True:
            user = usuario_escolhe_jogada(n, n)
            if user == 1:
                n = n - 1
                print("Voce tirou uma peça.")
                if n == 1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                    print("")
                    us = True
                    co = False
                else:
                    if n != 1 and n != 0:
                        print("Agora restam", n, " peças no tabuleiro.")
                        print("")
                        us = True
                        co = False
            else:
                if us == False and co == True:
                    if user != 1:
                        n = n - user
                        print("Voce tirou", user, " peças.")
                        if n == 1:
                            print("Agora resta apenas uma peça no tabuleiro.")
                            print("")
                            us = True
                            co = False
                        else:
                            if n != 1 and n != 0:
                                print("Agora restam", n, " peças no tabuleiro.")
                                print("")
                                us = True
                                co = False
        else:
            if co == False and us == True:
                comp = computador_escolhe_jogada(n, m)
                if comp == 1:
                    n = n - 1
                    print("O computador tirou uma peça.")
                    if n == 1:
                        print("Agora resta apenas uma peça no tabuleiro.")
                        print("")
                        co = True
                        us = False
                    else:
                        if n != 1 and n != 0:
                            print("Agora restam", n, " peças no tabuleiro.")
                            print("")
                            co = True
                            us = False
                        else:
                            if n == 0:
                                print("Fim do jogo! O computador ganhou!")
                                print("")
                                cwin = True
                                return cwin
                else:
                    if co == False and us == True:
                        if comp != 1:
                            print("O computador tirou", comp, " peças.")
                            n = n - comp
                            if n == 1:
                                print("Agora resta apenas uma peça no tabuleiro.")
                                print("")
                                co = True
                                us = False
                            else:
                                if n != 1 and n != 0:
                                    print("Agora restam", n, " peças no tabuleiro.")
                                    print("")
                                    co = True
                                    us = False
                                else:
                                    if n == 0:
                                        print("Fim do jogo! O computador ganhou!")
                                        print("")
                                        cwin = True
                                        return cwin



# campeonato() chama três vezes partida() recebe o ganhador de cada partida e imprime o resultado final.
def campeonato():
    camp = 1
    cwin = False
    uwin = False
    c = 0
    u = 0
    while not (camp == 4):
        if camp == 1:
            print("**** Rodada 1 ****")
            print("")
            camp = camp + 1
            cwin = partida()
            if cwin == True:
                c = 1
        else:
            if camp == 2:
                print("**** Rodada 2 ****")
                print("")
                camp = camp + 1
                cwin = partida()
                if cwin == True:
                    c = c + 1
            else:
                if camp == 3:
                    print("**** Rodada 3 ****")
                    print("")
                    cwin = partida()
                    if cwin == True:
                        c = c + 1
                    print("**** Final do campeonato! ****")
                    print("")
                    print("Placar: Você", u, " X ", c, "Computador")
                    camp = camp + 1


print("")
print("Bem-vindo ao jogo do NIM! Escolha:")
print("")
print("1 - para jogar uma partida isolada")
var = int(input("2 - para jogar um campeonato "))
print("")
if var == 1 and not var == 2:
    print("Voce escolheu uma partida!")
    print("")
    partida()
else:
    if var == 2and not var == 1:
        print("Voce escolheu um campeonato!")
        print("")
        campeonato()




