from pydoc import cli
from sklearn.preprocessing import MinMaxScaler
import pygame

from pygame import mixer

pygame.init()

Width = 1400
Height = 800

black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
green = (0, 255, 0)
gold = (212, 175, 55)
blue = (0, 255, 255)

screen = pygame.display.set_mode([Width, Height])
pygame.display.set_caption('BeatMaker')
label_font = pygame.font.Font('freesansbold.ttf', 28)

fps = 60
timer = pygame.time.Clock()
beats = 8
instruments = 6
boxes = []


# Lista con las boxes activadas. La inicializo con todas las posiciones a -1
# Cuando hago click en una box, se activa a 1
clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]

# 4 pulsos/segundo
bpm = 240

playing = True
active_length = 0
active_beat = 1
beat_changed = True

def draw_grid(clicked, ):
    # Rectángulo de la izquierda
    left_box = pygame.draw.rect(screen, gray, [0,0,200,Height-200], 5)
    # Rectangulo de abajo con botones
    bottom_box = pygame.draw.rect(screen, gray, [0, Height - 200, Width, 200], 5)
    boxes = []
    colors = [gray, white, gray]
    
    hi_hat_text = label_font.render('Hi Hat', True, white)
    screen.blit(hi_hat_text, (30, 30))
    snare_text = label_font.render('Snare', True, white)
    screen.blit(snare_text, (30, 130))
    kick_text = label_font.render('Bass Drum', True, white)
    screen.blit(kick_text, (30, 230))
    crash_text = label_font.render('Crash', True, white)
    screen.blit(crash_text, (30, 330))
    clap_text = label_font.render('Clap', True, white)
    screen.blit(clap_text, (30, 430))
    floor_text = label_font.render('Floor Tom', True, white)
    screen.blit(floor_text, (30, 530))

    for i in range(instruments):
        pygame.draw.line(screen, gray, (0, (i * 100) + 100), (200, (i * 100) + 100), 3)

    for i in range(beats):
        for j in range(instruments):
            # Si no esta activo
            if clicked[j][i] == -1:
                color = gray
            # Si esta activo
            else:
                color = green
            # Los rectangulos de los beats
            rect = pygame.draw.rect(screen, color,
                                    [i * ((Width - 200) // beats) + 205, (j * 100) + 5, ((Width - 200) // beats) - 10,
                                     90], 0, 3)
            # Guardo el rectangulo y sus coordenadas para el collision detection
            boxes.append((rect, (i, j)))
    
        active = pygame.draw.rect(screen, blue, [beat * ])
    return boxes

run = True
while run:
    timer.tick(fps)
    screen.fill(black)
    boxes = draw_grid(clicked)

    # Un click de mouse, teclado es un evento
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(boxes)):
                # Accedo al rect y compruebo si le he dado click
                if boxes[i][0].collidepoint(event.pos):
                    coords = boxes[i][1]
                    # Alterno de 1 a -1
                    clicked[coords[1]][coords[0]] *= -1

    beat_length = 3600 // bpm

    if playing:
        # Si todavia no ha acabado el pulso voy incrementando hasta que lo haga
        if active_length < beat_length:
            active_length += 1
        else:
            active_length = 0
            # Si todavia no hemos terminado todos los beats
            if active_beat < beats - 1:
                active_beat += 1
                beat_changed = True
            else:
                active_beat = 0



    pygame.display.flip()

pygame.quit()
