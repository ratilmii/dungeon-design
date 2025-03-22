import pygame
import random

class Dungeon:
    def __init__(self, width, height, room_count):
        self.width = width
        self.height = height
        self.room_count = room_count
        self.rooms = []
        self.distribute_points()


    #Luodaan room_count -kokoinen joukko satunnaisesti sijoitettuja pisteitä 
    def distribute_points(self):
        self.rooms = [
            (random.randint(300, self.width - 100), random.randint(100, self.height - 100))
            for _ in range(self.room_count)
        ]

    #Piirretään huoneiden keskipisteet näytölle
    def draw_vertices(self, screen):
        for x, y in self.rooms:
            pygame.draw.circle(screen, (255, 0, 0), (x, y), 2)