import pygame
from constants import WIDTH_DISPLAY, HEIGHT_DISPLAY, COLOR_BG, FPS, VELOCITY
from characters import Personaje


jugador = Personaje(90,90)

pygame.init()


screen = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY))
pygame.display.set_caption("movimienton personaje")

#definir las variables de movimiento del jugador
mover_arriba = False
mover_abajo = False
mover_derecha = False
mover_izquierda = False

#controlar el frame rate
reloj = pygame.time.Clock()


run = True
while run == True:
    
  
    # movimiento a 60 FPS
    reloj.tick(FPS)
    
    screen.fill(COLOR_BG)
    
    #calcular movimiento del jugador
    delta_x = 0
    delta_y = 0
    
    if mover_derecha == True:
        delta_x = VELOCITY
    
    if mover_izquierda == True:
        delta_x = -VELOCITY
    
    if mover_abajo == True:
        delta_y = VELOCITY
    
    if mover_arriba == True:
        delta_y = -VELOCITY


    #mover al jugador
    jugador.movimiento(delta_x, delta_y)
    
    
    jugador.draw(screen)
    
    for event in pygame.event.get():
        
        # evento para cerrar el juego
        if event.type == pygame.QUIT:
            run = False
        
        #evento para reconocer tecleo de letra
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False

    pygame.display.update()

pygame.quit()