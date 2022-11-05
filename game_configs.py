'''
configurações do jogo
'''

import pygame, os

pygame.init()
directory = os.path.dirname(os.path.realpath(__file__))

# Configurando sons
soundCrash = pygame.mixer.Sound(directory + "\\sounds\\crash.wav")
soundPoints = pygame.mixer.Sound(directory + "\\sounds\\diamond.wav")
soundVictory_Versus = pygame.mixer.Sound(directory + "\\sounds\\victory_versus.mp3")
soundGameOver = pygame.mixer.Sound(directory + "\\sounds\\gameOver.wav")

# Configurando a janela
SCREENWIDTH=800
SCREENHEIGHT=500
size = (800, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Driver")
os.environ['SDL_VIDEO_CENTERED'] = '1'


# Configurando a fonte
myfont = pygame.font.SysFont('Lucida Console', 20)


# Configurando menu inicial
menu_background = pygame.image.load(directory + "\\sprites\\menuBg.png").convert_alpha()


# Configurando as cores
RED = (255, 0, 0)
GREEN = (20, 255, 140)
BLUE = (100, 100, 255)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MAGENTA = (194,9,84)
