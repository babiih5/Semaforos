import pygame
import random
import sys
from pygame.locals import *


pygame.init()

# Fundos
capa1 = pygame.image.load("Capa.png")
capa2 = pygame.transform.scale(capa1, (1150,800))

menu1 = pygame.image.load("menu.png")
menu2 = pygame.transform.scale(menu1,(1150,800))

regras1 = pygame.image.load("regras.png")
regras2 = pygame.transform.scale(regras1, (1150,800))

bot1 = pygame.image.load("tela_p1.png")
bot2 = pygame.transform.scale(bot1, (1150,800))

pvsp1 = pygame.image.load("tela_p2.png")
pvsp2 = pygame.transform.scale(pvsp1, (1150,800))

jogo1 = pygame.image.load("JOGO.png")
jogo2 = pygame.transform.scale(jogo1,(1150,800))

win1 = pygame.image.load("win.png")
win2 = pygame.transform.scale(win1,(1150,800))

## Peças
verde1 = pygame.image.load("Verde.png")
verde2 = pygame.transform.scale(verde1, (210,200))

amarela1 = pygame.image.load("Amarelo.png")
amarela2 = pygame.transform.scale(amarela1, (210,200))

vermelho1 = pygame.image.load("Vermelho.png")
vermelho2 = pygame.transform.scale(vermelho1, (210,200))



def tela_inicial(estado):
    janela_capa = pygame.display.set_mode((1150,800))
    pygame.display.set_caption("Jogo dos Semáforos")

    janela_capa.blit(capa2,(0,0))

    while estado == "Capa":
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                estado = "Menu"
                tela_menu(estado)

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()


def tela_menu(estado):
    janela_menu = pygame.display.set_mode((1150,800))
    pygame.display.set_caption("Jogo dos Semáforos")
    janela_menu.blit(menu2,(0,0))

    ## ativar Botao regras
    botaoregras = pygame.Rect((50,457),(312,98))

    ## ativar botao Sair
    botaoSair = pygame.Rect((423, 646),(312,98))

    ## ativar botao BOT
    botaoBot = pygame.Rect((423, 457),(312,98))

    ## ativar Botao 1vs1
    botao1v1 = pygame.Rect((804, 457),(312,98))



    while estado == "Menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botaoregras.collidepoint(pygame.mouse.get_pos()):
                    estado = "Regras"
                    tela_regras(estado)
                    
                if botaoBot.collidepoint(pygame.mouse.get_pos()):
                    estado = "Bot"
                    tela_bot(estado)

                if botao1v1.collidepoint(pygame.mouse.get_pos()):
                    estado = "1v1"
                    tela_1v1(estado)

                if botaoSair.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit
                    quit()
        pygame.display.update()


def tela_regras(estado):
    janela_regras = pygame.display.set_mode((1150,800))
    pygame.display.set_caption("Jogo dos Semáforos")
    janela_regras.blit(regras2,(0,0))

    ## Botao voltar
    voltar = pygame.Rect((419,672),(312,98))


    while estado == "Regras":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if voltar.collidepoint(pygame.mouse.get_pos()):
                        estado = "Menu"
                        tela_menu(estado)

        pygame.display.update()

def tela_bot(estado):
    janela_bot = pygame.display.set_mode((1150,800))
    pygame.display.set_caption("Jogo dos Semáforos")
    janela_bot.blit(bot2,(0,0))

    botaovoltar2 = pygame.Rect((261, 528),(312,98))
    botaoplay1 = pygame.Rect((605,528),(312,98))

    nome_jogador1 = ""

    while estado == "Bot":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if botaoplay1.collidepoint(pygame.mouse.get_pos()):
                    estado = "JogoA"
                    tela_JogoA(estado)
                    
                if botaovoltar2.collidepoint(pygame.mouse.get_pos()):
                    estado = "Menu"
                    tela_menu(estado)
                    


            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_BACKSPACE:

                    nome_jogador1 = nome_jogador1[:-1]


                else:

                    nome_jogador1 += event.unicode

        pygame.display.update()

        fonte = pygame.font.Font(None, 46)
        texto_jogador1 = fonte.render(nome_jogador1, True, (255,255,255))


        posicao_texto_jogador1 = texto_jogador1.get_rect(midleft=(1150 // 2 - 350, 800 // 2 + 6))

        janela_bot.blit(texto_jogador1, posicao_texto_jogador1)

        pygame.display.update()



def tela_1v1(estado):
    janela_bot = pygame.display.set_mode((1150,800))
    pygame.display.set_caption("Jogo dos Semáforos")
    janela_bot.blit(pvsp2,(0,0))

    botaovoltar3 = pygame.Rect((250,621),(312,98))
    botaoplay2 = pygame.Rect((594,621),(312,98))

    area_j1 = pygame.Rect((206,344),(743,56))
    area_j2 = pygame.Rect((206,495),(743,56))
    #pygame.draw.rect(janela_bot, (173, 216, 230), (206, 495, 743, 56))
    jogador_atual = 1
    nome_jogador1 = ""
    nome_jogador2 = ""

    while estado == "1v1":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if botaoplay2.collidepoint(pygame.mouse.get_pos()):
                    estado = "JogoB"
                    tela_JogoB(estado)
                    
                if botaovoltar3.collidepoint(pygame.mouse.get_pos()):
                    estado = "Menu"
                    tela_menu(estado)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if jogador_atual == 1:
                        jogador_atual = 2
                    else:
                        jogador_atual = 1

                elif event.key == pygame.K_BACKSPACE:
                    if jogador_atual == 1:
                        nome_jogador1 = nome_jogador1[:-1]
                    else:
                        nome_jogador2 = nome_jogador2[:-1]

                else:
                    if jogador_atual == 1:
                        nome_jogador1 += event.unicode
                    else:
                        nome_jogador2 += event.unicode


        pygame.display.update()

        fonte = pygame.font.Font(None, 46)
        texto_jogador1 = fonte.render(nome_jogador1, True, (255,255,255))
        texto_jogador2 = fonte.render(nome_jogador2,True,(255,255,255))


        posicao_texto_jogador1 = texto_jogador1.get_rect(midleft=(1150 // 2 - 350, 800 // 2 - 23))
        posicao_texto_jogador2 = texto_jogador1.get_rect(midleft=(1150 // 2 - 350, 800 // 2 + 124))

        janela_bot.blit(texto_jogador1, posicao_texto_jogador1)
        janela_bot.blit(texto_jogador2, posicao_texto_jogador2)

        pygame.display.update()

########

## BOT  


def tela_JogoA(estado):
    janela_bot = pygame.display.set_mode((1150,800))
    pygame.display.set_caption("Jogo dos Semáforos")
    janela_bot.blit(jogo2,(0,0))

    ## Areas de Jogo
    A1 = pygame.Rect((170, 163), (186, 158))
    A2 = pygame.Rect((170, 336), (186, 138))
    A3 = pygame.Rect((170, 490), (186, 165))

    B1 = pygame.Rect((367, 163), (205, 158))
    B2 = pygame.Rect((367, 336), (205, 138))
    B3 = pygame.Rect((367, 490), (205, 165))

    C1 = pygame.Rect((587, 163), (197, 158))
    C2 = pygame.Rect((587, 336), (197, 138))
    C3 = pygame.Rect((587, 490), (197, 165))

    D1 = pygame.Rect((800, 163), (182, 158))
    D2 = pygame.Rect((800, 336), (182, 138))
    D3 = pygame.Rect((800, 490), (182, 165))

    #Estados
    eA1 = ''
    eA2 = ''
    eA3 = ''

    eB1 = ''
    eB2 = ''
    eB3 = ''

    eC1 = ''
    eC2 = ''
    eC3 = ''

    eD1 = ''
    eD2 = ''
    eD3 = ''

    p1 = False
    p2 = False
    p_win = ''

    win = False

    while estado == "JogoA":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            changeplayer(p1, p2, janela_bot)
            
            
            
            if (p1 == False):

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if A1.collidepoint(pygame.mouse.get_pos()):
                        if eA1 == '':
                            janela_bot.blit(verde2,(170, 150))
                            eA1 = 'G'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                            

                        elif eA1 == 'G':
                            pygame.draw.rect(janela_bot, (197, 188, 151), (170, 163, 180, 150))
                            janela_bot.blit(amarela2,(170, 150))
                            eA1 = 'Y'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        elif eA1 == 'Y':
                            pygame.draw.rect(janela_bot, (197, 188, 151), (170, 163, 180, 150))
                            janela_bot.blit(vermelho2,(170, 150))
                            eA1 = 'R'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        win = vitoria(eA1, eA2, eA3, eB1, eB2, eB3, eC1, eC2, eC3, eD1, eD2, eD3)


                    if A2.collidepoint(pygame.mouse.get_pos()):
                        if eA2 == '':
                            janela_bot.blit(verde2,(170, 310))
                            eA2 = 'G'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        elif eA2 == 'G':
                            pygame.draw.rect(janela_bot, (197, 188, 151), (170, 336, 180, 130))
                            janela_bot.blit(amarela2,(170, 310))
                            eA2 = 'Y'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        elif eA2 == 'Y':
                            pygame.draw.rect(janela_bot, (197, 188, 151), (170, 336, 180, 130))
                            janela_bot.blit(vermelho2,(170, 310))
                            eA2 = 'R'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        win = vitoria(eA1, eA2, eA3, eB1, eB2, eB3, eC1, eC2, eC3, eD1, eD2, eD3)


                    if A3.collidepoint(pygame.mouse.get_pos()):
                        if eA3 == '':
                            janela_bot.blit(verde2,(170, 470))
                            eA3 = 'G'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        elif eA3 == 'G':
                            pygame.draw.rect(janela_bot, (197, 188, 151), (170, 500, 180, 130))
                            janela_bot.blit(amarela2,(170, 470))
                            eA3 = 'Y'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        elif eA3 == 'Y':
                            pygame.draw.rect(janela_bot, (197, 188, 151), (170, 500, 180, 130))
                            janela_bot.blit(vermelho2,(170, 470))
                            eA3 = 'R'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        win = vitoria(eA1, eA2, eA3, eB1, eB2, eB3, eC1, eC2, eC3, eD1, eD2, eD3)

    #################### B
                    if B1.collidepoint(pygame.mouse.get_pos()):
                        if eB1 == '':
                            janela_bot.blit(verde2,(367, 150))
                            eB1 = 'G'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        elif eB1 == 'G':
                            pygame.draw.rect(janela_bot, (197, 188, 151), (370, 163, 180, 150))
                            janela_bot.blit(amarela2,(367, 150))
                            eB1 = 'Y'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        elif eB1 == 'Y':
                            pygame.draw.rect(janela_bot, (197, 188, 151), (370, 163, 180, 150))
                            janela_bot.blit(vermelho2,(367, 150))
                            eB1 = 'R'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        win = vitoria(eA1, eA2, eA3, eB1, eB2, eB3, eC1, eC2, eC3, eD1, eD2, eD3)


                    if B2.collidepoint(pygame.mouse.get_pos()):
                        if eB2 == '':
                            janela_bot.blit(verde2,(367, 310))
                            eB2 = 'G'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        elif eB2 == 'G':
                            pygame.draw.rect(janela_bot, (197, 188, 151), (370, 336, 180, 130))
                            janela_bot.blit(amarela2,(367, 310))
                            eB2 = 'Y'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        elif eB2 == 'Y':
                            pygame.draw.rect(janela_bot, (197, 188, 151), (370, 336, 180, 130))
                            janela_bot.blit(vermelho2,(367, 310))
                            eB2 = 'R'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        win = vitoria(eA1, eA2, eA3, eB1, eB2, eB3, eC1, eC2, eC3, eD1, eD2, eD3)


                    if B3.collidepoint(pygame.mouse.get_pos()):
                        if eB3 == '':
                            janela_bot.blit(verde2,(367, 470))
                            eB3 = 'G'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        elif eB3 == 'G':
                            pygame.draw.rect(janela_bot, (197, 188, 151), (370, 500, 180, 130))
                            janela_bot.blit(amarela2,(367, 470))
                            eB3 = 'Y'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False
            

                        elif eB3 == 'Y':
                            pygame.draw.rect(janela_bot, (197, 188, 151), (370, 500, 180, 130))
                            janela_bot.blit(vermelho2,(367, 470))
                            eB3 = 'R'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        win = vitoria(eA1, eA2, eA3, eB1, eB2, eB3, eC1, eC2, eC3, eD1, eD2, eD3)


    #################### C
                    if C1.collidepoint(pygame.mouse.get_pos()):
                        if eC1 == '':
                            janela_bot.blit(verde2,(587, 150))
                            eC1 = 'G'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        elif eC1 == 'G':
                            pygame.draw.rect(janela_bot, (197, 188, 151), (595, 163, 180, 150))
                            janela_bot.blit(amarela2,(587, 150))
                            eC1 = 'Y'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        elif eC1 == 'Y':
                            pygame.draw.rect(janela_bot, (197, 188, 151), (595, 163, 180, 150))
                            janela_bot.blit(vermelho2,(587, 150))
                            eC1 = 'R'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        win = vitoria(eA1, eA2, eA3, eB1, eB2, eB3, eC1, eC2, eC3, eD1, eD2, eD3)


                    if C2.collidepoint(pygame.mouse.get_pos()):
                        if eC2 == '':
                            janela_bot.blit(verde2,(587, 310))
                            eC2 = 'G'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        elif eC2 == 'G':
                            pygame.draw.rect(janela_bot, (197, 188, 151), (595, 336, 180, 130))
                            janela_bot.blit(amarela2,(587, 310))
                            eC2 = 'Y'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        elif eC2 == 'Y':
                            pygame.draw.rect(janela_bot, (197, 188, 151), (595, 336, 180, 130))
                            janela_bot.blit(vermelho2,(587, 310))
                            eC2 = 'R'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        win = vitoria(eA1, eA2, eA3, eB1, eB2, eB3, eC1, eC2, eC3, eD1, eD2, eD3)


                    if C3.collidepoint(pygame.mouse.get_pos()):
                        if eC3 == '':
                            janela_bot.blit(verde2,(587, 470))
                            eC3 = 'G'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        elif eC3 == 'G':
                            pygame.draw.rect(janela_bot, (197, 188, 151), (595, 500, 180, 130))
                            janela_bot.blit(amarela2,(587, 470))
                            eC3 = 'Y'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        elif eC3 == 'Y':
                            pygame.draw.rect(janela_bot, (197, 188, 151), (595, 500, 180, 130))
                            janela_bot.blit(vermelho2,(587, 470))
                            eC3 = 'R'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        win = vitoria(eA1, eA2, eA3, eB1, eB2, eB3, eC1, eC2, eC3, eD1, eD2, eD3)



    #################### D
                    if D1.collidepoint(pygame.mouse.get_pos()):
                        if eD1 == '':
                            janela_bot.blit(verde2,(780, 150))
                            eD1 = 'G'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        elif eD1 == 'G':
                            pygame.draw.rect(janela_bot, (197, 188, 151), (830, 163, 180, 150))
                            janela_bot.blit(amarela2,(780, 150))
                            eD1 = 'Y'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        elif eD1 == 'Y':
                            pygame.draw.rect(janela_bot, (197, 188, 151), (830, 163, 180, 150))
                            janela_bot.blit(vermelho2,(780, 150))
                            eD1 = 'R'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        win = vitoria(eA1, eA2, eA3, eB1, eB2, eB3, eC1, eC2, eC3, eD1, eD2, eD3)

                    if D2.collidepoint(pygame.mouse.get_pos()):
                        if eD2 == '':
                            janela_bot.blit(verde2,(780, 310))
                            eD2 = 'G'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        elif eD2 == 'G':
                            pygame.draw.rect(janela_bot, (197, 188, 151), (830, 336, 180, 130))
                            janela_bot.blit(amarela2,(780, 310))
                            eD2 = 'Y'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        elif eD2 == 'Y':
                            pygame.draw.rect(janela_bot, (197, 188, 151), (830, 336, 180, 130))
                            janela_bot.blit(vermelho2,(780, 310))
                            eD2 = 'R'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        win = vitoria(eA1, eA2, eA3, eB1, eB2, eB3, eC1, eC2, eC3, eD1, eD2, eD3)

                    if D3.collidepoint(pygame.mouse.get_pos()):
                        if eD3 == '':
                            janela_bot.blit(verde2,(780, 470))
                            eD3 = 'G'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        elif eD3 == 'G':
                            pygame.draw.rect(janela_bot, (197, 188, 151), (830, 500, 180, 130))
                            janela_bot.blit(amarela2,(780, 470))
                            eD3 = 'Y'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        elif eD3 == 'Y':
                            pygame.draw.rect(janela_bot, (197, 188, 151), (830, 500, 180, 130))
                            janela_bot.blit(vermelho2,(780, 470))
                            eD3 = 'R'

                            if (p1 == False):
                                changeplayer(p1, p2, janela_bot)
                                p1 = True
                                p2 = False

                            elif (p2 == False):
                                changeplayer(p1, p2, janela_bot)
                                p2 = True
                                p1 = False

                        win = vitoria(eA1, eA2, eA3, eB1, eB2, eB3, eC1, eC2, eC3, eD1, eD2, eD3)

            

            elif (p2 == False):
                random.seed()
                opcoes_linha = ('1','2','3')
                opcoes_coluna = ('A','B','C','D')
                valida = False

                
                while (valida == False):
                    opcao_lin = random.choice(opcoes_linha)
                    opcao_col = random.choice(opcoes_coluna)

                    casa =  opcao_col + opcao_lin

                    if(casa == 'A1'):
                        if(eA1 == ''):
                            janela_bot.blit(verde2,(170, 150))
                            eA1 = 'G'
                            valida = True

                        elif(eA1 == 'G'):
                            pygame.draw.rect(janela_bot, (197, 188, 151), (170, 163, 180, 150))
                            janela_bot.blit(amarela2,(170, 150))
                            eA1 = 'Y'
                            valida = True

                        elif(eA1 == 'Y'):
                            pygame.draw.rect(janela_bot, (197, 188, 151), (170, 163, 180, 150))
                            janela_bot.blit(vermelho2,(170, 150))
                            eA1 = 'R'
                            valida = True
                    
                    if(casa == 'A2'):
                        if(eA2 == ''):
                            janela_bot.blit(verde2,(170, 310))
                            eA2 = 'G'
                            valida = True

                        elif(eA2 == 'G'):
                            pygame.draw.rect(janela_bot, (197, 188, 151), (170, 336, 180, 130))
                            janela_bot.blit(amarela2,(170, 310))
                            eA2 = 'Y'
                            valida = True

                        elif(eA2 == 'Y'):
                            pygame.draw.rect(janela_bot, (197, 188, 151), (170, 336, 180, 130))
                            janela_bot.blit(vermelho2,(170, 310))
                            eA2 = 'R'
                            valida = True
                    
                    if(casa == 'A3'):
                        if(eA3 == ''):
                            janela_bot.blit(verde2,(170, 470))
                            eA3 = 'G'
                            valida = True

                        elif(eA3 == 'G'):
                            pygame.draw.rect(janela_bot, (197, 188, 151), (170, 500, 180, 130))
                            janela_bot.blit(amarela2,(170, 470))
                            eA3 = 'Y'
                            valida = True

                        elif(eA3 == 'Y'):
                            pygame.draw.rect(janela_bot, (197, 188, 151), (170, 500, 180, 130))
                            janela_bot.blit(vermelho2,(170, 470))
                            eA3 = 'R'
                            valida = True

                    ###### B
                    if(casa == 'B1'):
                        if(eB1 == ''):
                            janela_bot.blit(verde2,(367, 150))
                            eB1 = 'G'
                            valida = True

                        elif(eB1 == 'G'):
                            pygame.draw.rect(janela_bot, (197, 188, 151), (370, 163, 180, 150))
                            janela_bot.blit(amarela2,(367, 150))
                            eB1 = 'Y'
                            valida = True

                        elif(eB1 == 'Y'):
                            pygame.draw.rect(janela_bot, (197, 188, 151), (370, 163, 180, 150))
                            janela_bot.blit(vermelho2,(367, 150))
                            eB1 = 'R'
                            valida = True
                    
                    if(casa == 'B2'):
                        if(eB2 == ''):
                            janela_bot.blit(verde2,(367, 310))
                            eB2 = 'G'
                            valida = True

                        elif(eB2 == 'G'):
                            pygame.draw.rect(janela_bot, (197, 188, 151), (370, 336, 180, 130))
                            janela_bot.blit(amarela2,(367, 310))
                            eB2 = 'Y'
                            valida = True

                        elif(eB2 == 'Y'):
                            pygame.draw.rect(janela_bot, (197, 188, 151), (370, 336, 180, 130))
                            janela_bot.blit(vermelho2,(367, 310))
                            eB2 = 'R'
                            valida = True
                    
                    if(casa == 'B3'):
                        if(eB3 == ''):
                            janela_bot.blit(verde2,(367, 470))
                            eB3 = 'G'
                            valida = True

                        elif(eB3 == 'G'):
                            pygame.draw.rect(janela_bot, (197, 188, 151), (370, 500, 180, 130))
                            janela_bot.blit(amarela2,(367, 470))
                            eB3 = 'Y'
                            valida = True

                        elif(eB3 == 'Y'):
                            pygame.draw.rect(janela_bot, (197, 188, 151), (370, 500, 180, 130))
                            janela_bot.blit(vermelho2,(367, 470))
                            eB3 = 'R'
                            valida = True

                    ###### C
                    if(casa == 'C1'):
                        if(eC1 == ''):
                            janela_bot.blit(verde2,(587, 150))
                            eC1 = 'G'
                            valida = True

                        elif(eC1 == 'G'):
                            pygame.draw.rect(janela_bot, (197, 188, 151), (595, 163, 180, 150))
                            janela_bot.blit(amarela2,(587, 150))
                            eC1 = 'Y'
                            valida = True

                        elif(eC1 == 'Y'):
                            pygame.draw.rect(janela_bot, (197, 188, 151), (595, 163, 180, 150))
                            janela_bot.blit(vermelho2,(587, 150))
                            eC1 = 'R'
                            valida = True
                    
                    if(casa == 'C2'):
                        if(eC2 == ''):
                            janela_bot.blit(verde2,(587, 310))
                            eC2 = 'G'
                            valida = True

                        elif(eC2 == 'G'):
                            pygame.draw.rect(janela_bot, (197, 188, 151), (595, 336, 180, 130))
                            janela_bot.blit(amarela2,(587, 310))
                            eC2 = 'Y'
                            valida = True

                        elif(eC2 == 'Y'):
                            pygame.draw.rect(janela_bot, (197, 188, 151), (595, 336, 180, 130))
                            janela_bot.blit(vermelho2,(587, 310))
                            eC2 = 'R'
                            valida = True
                    
                    if(casa == 'C3'):
                        if(eC3 == ''):
                            janela_bot.blit(verde2,(587, 470))
                            eC3 = 'G'
                            valida = True

                        elif(eC3 == 'G'):
                            pygame.draw.rect(janela_bot, (197, 188, 151), (595, 500, 180, 130))
                            janela_bot.blit(amarela2,(587, 470))
                            eC3 = 'Y'
                            valida = True

                        elif(eC3 == 'Y'):
                            pygame.draw.rect(janela_bot, (197, 188, 151), (595, 500, 180, 130))
                            janela_bot.blit(vermelho2,(587, 470))
                            eC3 = 'R'
                            valida = True
                    
                    ###### D
                    if(casa == 'D1'):
                        if(eD1 == ''):
                            janela_bot.blit(verde2,(780, 150))
                            eD1 = 'G'
                            valida = True

                        elif(eD1 == 'G'):
                            pygame.draw.rect(janela_bot, (197, 188, 151), (830, 163, 180, 150))
                            janela_bot.blit(amarela2,(780, 150))
                            eD1 = 'Y'
                            valida = True

                        elif(eD1 == 'Y'):
                            pygame.draw.rect(janela_bot, (197, 188, 151), (830, 163, 180, 150))
                            janela_bot.blit(vermelho2,(780, 150))
                            eD1 = 'R'
                            valida = True
                    
                    if(casa == 'D2'):
                        if(eD2 == ''):
                            janela_bot.blit(verde2,(780, 310))
                            eD2 = 'G'
                            valida = True

                        elif(eD2 == 'G'):
                            pygame.draw.rect(janela_bot, (197, 188, 151), (830, 336, 180, 130))
                            janela_bot.blit(amarela2,(780, 310))
                            eD2 = 'Y'
                            valida = True

                        elif(eD2 == 'Y'):
                            pygame.draw.rect(janela_bot, (197, 188, 151), (830, 336, 180, 130))
                            janela_bot.blit(vermelho2,(780, 310))
                            eD2 = 'R'
                            valida = True
                    
                    if(casa == 'D3'):
                        if(eD3 == ''):
                            janela_bot.blit(verde2,(780, 470))
                            eD3 = 'G'
                            valida = True

                        elif(eD3 == 'G'):
                            pygame.draw.rect(janela_bot, (197, 188, 151), (830, 500, 180, 130))
                            janela_bot.blit(amarela2,(780, 470))
                            eD3 = 'Y'
                            valida = True

                        elif(eD3 == 'Y'):
                            pygame.draw.rect(janela_bot, (197, 188, 151), (830, 500, 180, 130))
                            janela_bot.blit(vermelho2,(780, 470))
                            eD3 = 'R'
                            valida = True
                        

                p1 = False

            win = vitoria(eA1, eA2, eA3, eB1, eB2, eB3, eC1, eC2, eC3, eD1, eD2, eD3)
                
                
            if(win == True):

                
                A1 = None
                A2 = None
                A3 = None
                B1 = None
                B2 = None
                B3 = None
                C1 = None
                C2 = None
                C3 = None
                D1 = None
                D2 = None
                D3 = None
                
                janela_bot = pygame.display.set_mode((1150,800))
                pygame.display.set_caption("Jogo dos Semáforos")
                janela_bot.blit(win2,(0,0))

                if (p1 == True):
                    p_win = 'Player 1'
                else:
                    p_win = 'BOT Diogo'


                estado = "Vitoria"

                tela_vitoria(estado, p_win)

        pygame.display.update()


###############


def vitoria(eA1, eA2, eA3, eB1, eB2, eB3, eC1, eC2, eC3, eD1, eD2, eD3):

    v =False

    ## Linhas
    if (eA1 == eB1 and eA1 == eC1 and eA1 != '' and eB1 != '' and eC1 != ''):
        v = True
    if (eB1 == eC1 and eB1 == eD1 and eB1 != '' and eC1 != '' and eD1 != ''):
        v = True
    
    if (eA2 == eB2 and eA2 == eC2 and eA2 != '' and eB2 != '' and eC2 != ''):
        v = True
    if (eB2 == eC2 and eB2 == eD2 and eB2 != '' and eC2 != '' and eD2 != ''):
        v = True

    if (eA3 == eB3 and eA3 == eC3 and eA3 != '' and eB3 != '' and eC3 != ''):
        v = True
    if (eB3 == eC3 and eB3 == eD3 and eB3 != '' and eC3 != '' and eD3 != ''):
        v = True
    

    ## Colunas
    if (eA1 == eA2 and eA1 == eA3 and eA1 != '' and eA2 != '' and eA3 != ''):
        v = True
    
    if (eB1 == eB2 and eB1 == eB3 and eB1 != '' and eB2 != '' and eB3 != ''):
        v = True

    if (eC1 == eC2 and eC1 == eC3 and eC1 != '' and eC2 != '' and eC3 != ''):
        v = True

    if (eD1 == eD2 and eD1 == eD3 and eD1 != '' and eD2 != '' and eD3 != ''):
        v = True

    ## Diagonais
    if (eA1 == eB2 and eA1 == eC3 and eA1 != '' and eB2 != '' and eC3 != ''):
        v = True
    if (eB1 == eC2 and eB1== eD3 and eB1 != '' and eC2 != '' and eD3 != ''):
        v = True
    if (eC1 == eB2 and eC1 == eA3 and eC1 != '' and eB2 != '' and eA3 != ''):
        v = True
    if (eD1 == eC2 and eD1 == eB3 and eD1 != '' and eC2 != '' and eB3 != ''):
        v = True



    if (v == True):
        print("\n\nFim do jogo! Vitória")


        return True

    return False
        

def changeplayer(p1, p2, janela_bot):
    if(p1 == False):
        fonte = pygame.font.Font(None, 46)
        texto_p1 = fonte.render("Player 1", True, (255,255,255))

        pygame.draw.rect(janela_bot, (222, 197, 119), (400, 735, 400, 45))

        pos1 = texto_p1.get_rect(midleft=(1150 // 2 - 30, 800 // 2 + 360))

        janela_bot.blit(texto_p1, pos1)

    elif(p2 == False):
        fonte = pygame.font.Font(None, 46)
        texto_p2 = fonte.render("Player 2", True, (255,255,255))

        pygame.draw.rect(janela_bot, (222, 197, 119), (400, 735, 400, 45))

        pos2 = texto_p2.get_rect(midleft=(1150 // 2 - 30, 800 // 2 + 360))

        janela_bot.blit(texto_p2, pos2)

def tela_JogoB(estado):
    janela_bot = pygame.display.set_mode((1150,800))
    pygame.display.set_caption("Jogo dos Semáforos")
    janela_bot.blit(jogo2,(0,0))


    p1 = False
    p2 = False
    p_win = ''

    win =  False

    #pygame.draw.rect(janela_bot, (173, 216, 230), (400, 735, 400, 45))
    #janela_bot.blit(vermelho2,(367, 310))

    ## Areas de Jogo
    A1 = pygame.Rect((170, 163), (186, 158))
    A2 = pygame.Rect((170, 336), (186, 138))
    A3 = pygame.Rect((170, 490), (186, 165))

    B1 = pygame.Rect((367, 163), (205, 158))
    B2 = pygame.Rect((367, 336), (205, 138))
    B3 = pygame.Rect((367, 490), (205, 165))

    C1 = pygame.Rect((587, 163), (197, 158))
    C2 = pygame.Rect((587, 336), (197, 138))
    C3 = pygame.Rect((587, 490), (197, 165))

    D1 = pygame.Rect((800, 163), (182, 158))
    D2 = pygame.Rect((800, 336), (182, 138))
    D3 = pygame.Rect((800, 490), (182, 165))

    #Estados
    eA1 = ''
    eA2 = ''
    eA3 = ''

    eB1 = ''
    eB2 = ''
    eB3 = ''

    eC1 = ''
    eC2 = ''
    eC3 = ''

    eD1 = ''
    eD2 = ''
    eD3 = ''

    while estado == "JogoB":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            changeplayer(p1, p2, janela_bot)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if A1.collidepoint(pygame.mouse.get_pos()):
                    if eA1 == '':
                        janela_bot.blit(verde2,(170, 150))
                        eA1 = 'G'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False

                    elif eA1 == 'G':
                        pygame.draw.rect(janela_bot, (197, 188, 151), (170, 163, 180, 150))
                        janela_bot.blit(amarela2,(170, 150))
                        eA1 = 'Y'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False

                    elif eA1 == 'Y':
                        pygame.draw.rect(janela_bot, (197, 188, 151), (170, 163, 180, 150))
                        janela_bot.blit(vermelho2,(170, 150))
                        eA1 = 'R'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False


                if A2.collidepoint(pygame.mouse.get_pos()):
                    if eA2 == '':
                        janela_bot.blit(verde2,(170, 310))
                        eA2 = 'G'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False

                    elif eA2 == 'G':
                        pygame.draw.rect(janela_bot, (197, 188, 151), (170, 336, 180, 130))
                        janela_bot.blit(amarela2,(170, 310))
                        eA2 = 'Y'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False

                    elif eA2 == 'Y':
                        pygame.draw.rect(janela_bot, (197, 188, 151), (170, 336, 180, 130))
                        janela_bot.blit(vermelho2,(170, 310))
                        eA2 = 'R'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False


                if A3.collidepoint(pygame.mouse.get_pos()):
                    if eA3 == '':
                        janela_bot.blit(verde2,(170, 470))
                        eA3 = 'G'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False

                    elif eA3 == 'G':
                        pygame.draw.rect(janela_bot, (197, 188, 151), (170, 500, 180, 130))
                        janela_bot.blit(amarela2,(170, 470))
                        eA3 = 'Y'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False

                    elif eA3 == 'Y':
                        pygame.draw.rect(janela_bot, (197, 188, 151), (170, 500, 180, 130))
                        janela_bot.blit(vermelho2,(170, 470))
                        eA3 = 'R'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False

#################### B
                if B1.collidepoint(pygame.mouse.get_pos()):
                    if eB1 == '':
                        janela_bot.blit(verde2,(367, 150))
                        eB1 = 'G'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False

                    elif eB1 == 'G':
                        pygame.draw.rect(janela_bot, (197, 188, 151), (370, 163, 180, 150))
                        janela_bot.blit(amarela2,(367, 150))
                        eB1 = 'Y'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False

                    elif eB1 == 'Y':
                        pygame.draw.rect(janela_bot, (197, 188, 151), (370, 163, 180, 150))
                        janela_bot.blit(vermelho2,(367, 150))
                        eB1 = 'R'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False


                if B2.collidepoint(pygame.mouse.get_pos()):
                    if eB2 == '':
                        janela_bot.blit(verde2,(367, 310))
                        eB2 = 'G'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False

                    elif eB2 == 'G':
                        pygame.draw.rect(janela_bot, (197, 188, 151), (370, 336, 180, 130))
                        janela_bot.blit(amarela2,(367, 310))
                        eB2 = 'Y'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False

                    elif eB2 == 'Y':
                        pygame.draw.rect(janela_bot, (197, 188, 151), (370, 336, 180, 130))
                        janela_bot.blit(vermelho2,(367, 310))
                        eB2 = 'R'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False


                if B3.collidepoint(pygame.mouse.get_pos()):
                    if eB3 == '':
                        janela_bot.blit(verde2,(367, 470))
                        eB3 = 'G'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False

                    elif eB3 == 'G':
                        pygame.draw.rect(janela_bot, (197, 188, 151), (370, 500, 180, 130))
                        janela_bot.blit(amarela2,(367, 470))
                        eB3 = 'Y'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False

                    elif eB3 == 'Y':
                        pygame.draw.rect(janela_bot, (197, 188, 151), (370, 500, 180, 130))
                        janela_bot.blit(vermelho2,(367, 470))
                        eB3 = 'R'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False


#################### C
                if C1.collidepoint(pygame.mouse.get_pos()):
                    if eC1 == '':
                        janela_bot.blit(verde2,(587, 150))
                        eC1 = 'G'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False

                    elif eC1 == 'G':
                        pygame.draw.rect(janela_bot, (197, 188, 151), (595, 163, 180, 150))
                        janela_bot.blit(amarela2,(587, 150))
                        eC1 = 'Y'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False

                    elif eC1 == 'Y':
                        pygame.draw.rect(janela_bot, (197, 188, 151), (595, 163, 180, 150))
                        janela_bot.blit(vermelho2,(587, 150))
                        eC1 = 'R'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False


                if C2.collidepoint(pygame.mouse.get_pos()):
                    if eC2 == '':
                        janela_bot.blit(verde2,(587, 310))
                        eC2 = 'G'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False

                    elif eC2 == 'G':
                        pygame.draw.rect(janela_bot, (197, 188, 151), (595, 336, 180, 130))
                        janela_bot.blit(amarela2,(587, 310))
                        eC2 = 'Y'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False

                    elif eC2 == 'Y':
                        pygame.draw.rect(janela_bot, (197, 188, 151), (595, 336, 180, 130))
                        janela_bot.blit(vermelho2,(587, 310))
                        eC2 = 'R'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False


                if C3.collidepoint(pygame.mouse.get_pos()):
                    if eC3 == '':
                        janela_bot.blit(verde2,(587, 470))
                        eC3 = 'G'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False

                    elif eC3 == 'G':
                        pygame.draw.rect(janela_bot, (197, 188, 151), (595, 500, 180, 130))
                        janela_bot.blit(amarela2,(587, 470))
                        eC3 = 'Y'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False

                    elif eC3 == 'Y':
                        pygame.draw.rect(janela_bot, (197, 188, 151), (595, 500, 180, 130))
                        janela_bot.blit(vermelho2,(587, 470))
                        eC3 = 'R'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False



#################### D
                if D1.collidepoint(pygame.mouse.get_pos()):
                    if eD1 == '':
                        janela_bot.blit(verde2,(780, 150))
                        eD1 = 'G'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False

                    elif eD1 == 'G':
                        pygame.draw.rect(janela_bot, (197, 188, 151), (830, 163, 180, 150))
                        janela_bot.blit(amarela2,(780, 150))
                        eD1 = 'Y'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False

                    elif eD1 == 'Y':
                        pygame.draw.rect(janela_bot, (197, 188, 151), (830, 163, 180, 150))
                        janela_bot.blit(vermelho2,(780, 150))
                        eD1 = 'R'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False


                if D2.collidepoint(pygame.mouse.get_pos()):
                    if eD2 == '':
                        janela_bot.blit(verde2,(780, 310))
                        eD2 = 'G'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False

                    elif eD2 == 'G':
                        pygame.draw.rect(janela_bot, (197, 188, 151), (830, 336, 180, 130))
                        janela_bot.blit(amarela2,(780, 310))
                        eD2 = 'Y'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False

                    elif eD2 == 'Y':
                        pygame.draw.rect(janela_bot, (197, 188, 151), (830, 336, 180, 130))
                        janela_bot.blit(vermelho2,(780, 310))
                        eD2 = 'R'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False


                if D3.collidepoint(pygame.mouse.get_pos()):
                    if eD3 == '':
                        janela_bot.blit(verde2,(780, 470))
                        eD3 = 'G'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False

                    elif eD3 == 'G':
                        pygame.draw.rect(janela_bot, (197, 188, 151), (830, 500, 180, 130))
                        janela_bot.blit(amarela2,(780, 470))
                        eD3 = 'Y'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False

                    elif eD3 == 'Y':
                        pygame.draw.rect(janela_bot, (197, 188, 151), (830, 500, 180, 130))
                        janela_bot.blit(vermelho2,(780, 470))
                        eD3 = 'R'

                        if (p1 == False):
                            changeplayer(p1, p2, janela_bot)
                            p1 = True
                            p2 = False

                        elif (p2 == False):
                            changeplayer(p1, p2, janela_bot)
                            p2 = True
                            p1 = False


               

                win = vitoria(eA1, eA2, eA3, eB1, eB2, eB3, eC1, eC2, eC3, eD1, eD2, eD3)
                
                
                if(win == True):

                    
                    A1 = None
                    A2 = None
                    A3 = None
                    B1 = None
                    B2 = None
                    B3 = None
                    C1 = None
                    C2 = None
                    C3 = None
                    D1 = None
                    D2 = None
                    D3 = None
                    
                    janela_bot = pygame.display.set_mode((1150,800))
                    pygame.display.set_caption("Jogo dos Semáforos")
                    janela_bot.blit(win2,(0,0))

                    if (p1 == True):
                        p_win = 'Player 1'
                    elif (p2 == True):
                        p_win = 'Player 2'


                    estado = "Vitoria"

                    tela_vitoria(estado, p_win)


        pygame.display.update()


def tela_vitoria(estado, p_win):
    print(p_win)
    janela_bot = pygame.display.set_mode((1150,800))
    pygame.display.set_caption("Jogo dos Semáforos")
    janela_bot.blit(win2,(0,0))


    ## ativar Sair
    sair = pygame.Rect((817, 146),(312,98))

    ## ativar Menu

    menu = pygame.Rect((817, 22),(312,98))

    #pygame.draw.rect(janela_bot, (173, 216, 230), (817, 146, 312, 98))

    while estado == "Vitoria":
        fonte = pygame.font.Font(None, 46)
        texto = fonte.render(p_win, True, (255,255,255))

        pygame.draw.rect(janela_bot, (222, 197, 119), (400, 735, 400, 45))

        pos = texto.get_rect(midleft=(1150 // 2 - 40, 800 // 2 + 360))

        janela_bot.blit(texto, pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                            if menu.collidepoint(pygame.mouse.get_pos()):
                                estado = "Menu"
                                tela_menu(estado)
                            
                            if sair.collidepoint(pygame.mouse.get_pos()):
                                pygame.quit
                                quit()
        
        

        
        
        pygame.display.update()


            
            
        



estado = "Capa"
tela_inicial(estado)