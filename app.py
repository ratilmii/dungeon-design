import pygame
import sys
from dungeon import Dungeon

pygame.init()

#Alustetaan ikkuna
WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Dungeon Designer")

#Luodaan 10 huoneen dungeon-olio
dungeon = Dungeon(WIDTH, HEIGHT, 10)

#Teksti joka kertoo huoneiden määrän
font = pygame.font.Font(None, 32)
text = font.render("Room count: 10", True, (255, 255, 255))

#Luodaan button uuden luolaston generoinnille
generate_button_rect = pygame.Rect(20, 100, 150, 40)

#Varsinainen silmukka
while True:
    screen.fill((0,0,0))
    #Harmaa alue huoneiden piirtämistä varten
    pygame.draw.rect(screen, (115, 115, 115), (250,50, 980, 620)) 
    screen.blit(text, (20, 50))
    #Generate-nappi näytölle
    pygame.draw.rect(screen, (100, 100, 100), generate_button_rect)
    button_text = font.render("Generate", True, (255, 255, 255))
    screen.blit(button_text, (40, 110))

    #Piirretään huoneet ja niiden keskipisteet
    dungeon.draw_rooms(screen)
    dungeon.draw_vertices(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        #Generate-nappi kutsuu huoneet generoivaa metodia
        elif event.type == pygame.MOUSEBUTTONDOWN:  
            if generate_button_rect.collidepoint(event.pos):
                dungeon.generate_rooms()

    pygame.display.flip()

pygame.quit()