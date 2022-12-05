import pygame, os

pygame.init()
directory = os.path.dirname(os.path.realpath(__file__))

# Configurando sons
sound_crash = pygame.mixer.Sound(directory + "\\sounds\\crash.wav")
sound_points = pygame.mixer.Sound(directory + "\\sounds\\diamond.wav")
sound_victory_versus = pygame.mixer.Sound(directory + "\\sounds\\victory_versus.wav")
sound_gameover = pygame.mixer.Sound(directory + "\\sounds\\gameOver.wav")

# Configurando a janela
SCREENWIDTH=1000
SCREENHEIGHT=625
size = (1000, 625)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Driver")
os.environ['SDL_VIDEO_CENTERED'] = '1'


# Configurando a fonte
myfont = pygame.font.SysFont('rockwellnegrito', 20)


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
DARKBLUE = (52, 77, 103)
LIGHTGREEN = (110, 204, 175)
YELLOWGREEN = (173, 231, 146)
