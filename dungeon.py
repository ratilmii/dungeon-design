import pygame
import random

class Dungeon:
    def __init__(self, width, height, room_count):
        self.width = width
        self.height = height
        self.room_count = room_count
        
        #Määritellään huoneiden minimi- ja maksimikoot
        self.room_width_min_len = 50
        self.room_height_min_len = 50
        self.room_width_max_len = 200
        self.room_height_max_len = 200

        self.generate_rooms()

    #Luodaan satunnaisen kokoiset huoneet satunnaisiin sijainteihin 
    def generate_rooms(self):
        self.rooms = []
        BUFFER = 20 #Tyhjä tila huoneiden välillä
        attempts_left = 100 #Estetään ikuinen silmukka
        ruutu_x, ruutu_y, ruutu_w, ruutu_h = 250, 50, 980, 620 #Harmaan piirtotilan koordinaatit ja mitat

        while len(self.rooms) < self.room_count and attempts_left > 0:
            #Leveys ja korkeus
            w = random.randint(self.room_width_min_len, self.room_width_max_len)
            h = random.randint(self.room_height_min_len, self.room_height_max_len)

            #Koordinaatit aloituskulmalle
            x = random.randint(ruutu_x + BUFFER, ruutu_x + ruutu_w - w - BUFFER)
            y = random.randint(ruutu_y + BUFFER, ruutu_y + ruutu_h - h - BUFFER)

            new_room = pygame.Rect(x, y, w, h)

            #Estetään päällekkäisyys
            if not any(new_room.inflate(BUFFER, BUFFER).colliderect(existing.inflate(BUFFER, BUFFER)) for existing in self.rooms):
                self.rooms.append(new_room)
            
            attempts_left -= 1

    #Piirretään huoneiden keskipisteet näytölle
    def draw_vertices(self, screen):
        for rect in self.rooms:
            pygame.draw.circle(screen, (255, 0, 0), rect.center, 2)

    #Piirretään huoneiden seinät pisteiden ympärille
    def draw_rooms(self, screen):
        for rect in self.rooms:
            pygame.draw.rect(screen, (255, 255, 255), rect, 1)