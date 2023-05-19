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

    while estado == "Menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()

        return estado

def tela_jogbot(estado):
    janela_bot = pygame.display.set_mode((1150,800))
    pygame.display.set_caption("Jogo dos Semáforos")
    janela_bot.blit(bot2,(0,0))
    nome_jogador1 = ""

    while estado == "Bot":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

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

        



# while True:
#     if estado == "Capa":
#         estado = tela_inicial(estado)
#     else:
#         estado = tela_menu(estado)

# estado = "Bot"
# tela_jogbot(estado)