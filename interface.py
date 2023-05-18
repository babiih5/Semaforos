import pygame
import sys
from pygame.locals import *



pygame.init()

## Janela do jogo

janela = pygame.display.set_mode((1150,800))
pygame.display.set_caption("Jogo dos Semáforos")


##Fundos

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


## Verificação de tela
inicio = True
menu = False


def tela_inicial(janela):
    estado = True
    janela.blit(capa2,(0,0))
    
    for event in pygame.event.get():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                estado=False
        return estado


def tela_menu(janela):
    estado = True
    janela.blit(menu2,(0,0))




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    if inicio==True:
        inicio = tela_inicial(janela)
     

    else:
        if menu == True:
            tela_menu(janela)



    pygame.display.update()