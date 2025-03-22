import pygame
import sys
from dungeon import Dungeon

pygame.init()

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.display.set_caption("Dungeon Designer")

dungeon = Dungeon(WIDTH, HEIGHT, 10)

font = pygame.font.Font(None, 32)
text = font.render("Room count: 10", True, (255, 255, 255))

generate_button_rect = pygame.Rect(20, 100, 150, 40)

while True:
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,255,255), (250,50, 980, 620), 1)
    screen.blit(text, (20, 50))

    pygame.draw.rect(screen, (100, 100, 100), generate_button_rect)
    button_text = font.render("Generate", True, (255, 255, 255))
    screen.blit(button_text, (40, 110))

    dungeon.draw_vertices(screen)
    dungeon.draw_rooms(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:  
            if generate_button_rect.collidepoint(event.pos):
                dungeon.generate_rooms()

    pygame.display.flip()

pygame.quit()