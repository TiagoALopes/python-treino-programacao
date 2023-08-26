import pygame
pygame.init()
pygame.mixer.music.load('exe21.mp3')
pygame.mixer.music.play()
input('Tecle entar para finalizar: ')
pygame.event.wait()