from pygame.locals import *
import pygame
import sys

clock = pygame.time.Clock()

pygame.init()  # iniciando o pygame

pygame.display.set_caption('Metal Slug 🎮')

WINDOW_SIZE = (650, 400)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)  # Inicializando a tela

img_fundo = pygame.image.load('./IMG/florest.png').convert()

# Walk Left

WALK_LEFT = [
    pygame.image.load('./IMG/PlayerWalking/0.png').convert(),
    pygame.image.load('./IMG/PlayerWalking/1.png').convert(),
    pygame.image.load('./IMG/PlayerWalking/2.png').convert(),
    pygame.image.load('./IMG/PlayerWalking/3.png').convert(),
    pygame.image.load('./IMG/PlayerWalking/4.png').convert(),
    pygame.image.load('./IMG/PlayerWalking/5.png').convert(),
    pygame.image.load('./IMG/PlayerWalking/6.png').convert(),
    pygame.image.load('./IMG/PlayerWalking/7.png').convert(),
    pygame.image.load('./IMG/PlayerWalking/8.png').convert(),
    pygame.image.load('./IMG/PlayerWalking/9.png').convert(),
    pygame.image.load('./IMG/PlayerWalking/10.png').convert(),
    pygame.image.load('./IMG/PlayerWalking/11.png').convert(),
    pygame.image.load('./IMG/PlayerWalking/12.png').convert(),
    pygame.image.load('./IMG/PlayerWalking/13.png').convert(),
    pygame.image.load('./IMG/PlayerWalking/14.png').convert(),
    pygame.image.load('./IMG/PlayerWalking/15.png').convert(),
    pygame.image.load('./IMG/PlayerWalking/16.png').convert(),
    pygame.image.load('./IMG/PlayerWalking/17.png').convert(),
    pygame.image.load('./IMG/PlayerWalking/18.png').convert(),
    pygame.image.load('./IMG/PlayerWalking/19.png').convert(),
    pygame.image.load('./IMG/PlayerWalking/20.png').convert(),
    pygame.image.load('./IMG/PlayerWalking/21.png').convert(),
    pygame.image.load('./IMG/PlayerWalking/22.png').convert(),
]


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            

    pygame.display.update()

    #background da imagem
    screen.blit(img_fundo, (0, 0))

    pygame.display.flip()
    clock.tick(60)
