import pygame
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

## Peças
verde1 = pygame.image.load("Verde.png")
verde2 = pygame.transform.scale(verde1, (210,200))

amarela1 = pygame.image.load("Amarelo.png")
amarela2 = pygame.transform.scale(amarela1, (210,200))

vermelho1 = pygame.image.load("Vermelho.png")
vermelho2 = pygame.transform.scale(vermelho1, (210,200))


# Verificação de tela
estado = "Capa"

def tela_inicial(estado):
    janela_capa = pygame.display.set_mode((1150,800))
    pygame.display.set_caption("Jogo dos Semáforos")

    janela_capa.blit(capa2,(0,0))

    while estado == "Capa":
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                inicio=False
                estado = "Menu"
                
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
        return estado


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
                if botaoBot.collidepoint(pygame.mouse.get_pos()):
                    estado = "Bot"
                if botao1v1.collidepoint(pygame.mouse.get_pos()):
                    estado = "1v1"
                if botaoSair.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit
                    quit()
        pygame.display.update()

        return estado
    


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
                    estado = "JogoB"
                if botaovoltar2.collidepoint(pygame.mouse.get_pos()):
                    estado = "Menu"


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
                    estado = "Jogo1v1"
                if botaovoltar3.collidepoint(pygame.mouse.get_pos()):
                    estado = "Menu"

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

                

        pygame.display.update()

estado = "JogoB"
tela_JogoB(estado)

# while True:
#     if estado == "Capa":
#         estado = tela_inicial(estado)
#     else:
#         estado = tela_menu(estado)

# estado = "Bot"
# tela_bot(estado)
#estado = "1v1"
#tela_1v1(estado)