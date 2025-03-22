import pygame
import random

class Dungeon:
    def __init__(self, width, height, room_count):
        self.width = width
        self.height = height
        self.room_count = room_count
        self.rooms = []

        self.room_width_min_len = 50
        self.room_height_min_len = 50
        self.room_width_max_len = 200
        self.room_height_max_len = 200

        self.generate_rooms()

    #Luodaan satunnaisen kokoiset huoneet satunnaisiin sijainteihin 
    def generate_rooms(self):
        self.rooms = [
            (
                random.randint(400, self.width - 200),
                random.randint(200, self.height - 200), 
                random.randint(self.room_width_min_len, self.room_width_max_len),
                random.randint(self.room_height_min_len, self.room_height_max_len)
            )
            for _ in range(self.room_count)
        ]

    #Piirretään huoneiden keskipisteet näytölle
    def draw_vertices(self, screen):
        for x, y, _, _ in self.rooms:
            pygame.draw.circle(screen, (255, 0, 0), (x, y), 2)

    #Piirretään huoneiden seinät pisteiden ympärille
    def draw_rooms(self, screen):
        for x, y, w, h in self.rooms:
            rect_x = x - w // 2
            rect_y = y - h // 2
            pygame.draw.rect(screen, (255, 255, 255), (rect_x, rect_y, w, h), 1)