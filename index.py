from pygame.locals import *
import pygame
import sys

clock = pygame.time.Clock()

pygame.init()  # iniciando o pygame

pygame.display.set_caption('Metal Slug 🎮')

WINDOW_SIZE = (650, 400)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)  # Inicializando a tela

img_fundo = pygame.image.load('./IMG/florest.png').convert()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

    screen.blit(img_fundo, (0, 0))

    pygame.display.flip()

    clock.tick(60)
