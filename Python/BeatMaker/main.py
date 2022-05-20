from sklearn.preprocessing import MinMaxScaler
import pygame

from pygame import mixer

pygame.init()

Width = 1400
Height = 800

black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

screen = pygame.display.set_mode([Width, Height])
pygame.display.set_caption('BeatMaker')
label_font = pygame.font.Font('freesansbold.ttf', 32)

fps = 60
timer = pygame.time.Clock()

run = True
while run:
    timer.tick(fps)