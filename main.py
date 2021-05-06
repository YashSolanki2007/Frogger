# Imports
import pygame
import math
import time 
import sys
import random
import colorama
from colorama import Fore, Back, Style

# Game Variables
WIDTH = 600 
HEIGHT = 800
APROXIMATE_PLAYER_DIMENSIONS = 70
BLACK = (0, 0, 0)
car_1_x = random.randint(-140, -70)
car_2_x = random.randint(-140, -70)
car_3_x = random.randint(-140, -70)

# Initialize pygame 
pygame.init()

# Making the display 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Frogger Game")

# Set the display icon 
icon = pygame.image.load("frog.png")
pygame.display.set_icon(icon)

# Making the player class
class Frog:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 

    def draw(self, surface):
        img = pygame.image.load("frog.png")
        surface.blit(img, (self.x, self.y))

# Making the right car class
class RightCar:
    def __init__(self, x, y, x_change):
        self.x = x 
        self.y = y
        self.x_change = x_change

    def draw(self, surface):
        img = pygame.image.load("baby-car.png")
        surface.blit(img, (self.x, self.y))

    def drive(self):
        self.x += self.x_change

    def check_boundary(self):
        global WIDTH

        if self.x > WIDTH + 70:
            self.x = -70

    def check_collisions(self, car_x, car_y, player_x, player_y):
        distance = math.sqrt((math.pow(player_x - car_x, 2) + math.pow(player_y - car_y, 2)))
        if distance < 27:
            return True 

        else: 
            return False 

# Making the left car class
class LeftCar:
    def __init__(self, x, y, x_change):
        self.x = x 
        self.y = y
        self.x_change = x_change

    def draw(self, surface):
        img = pygame.image.load("car.png")
        surface.blit(img, (self.x, self.y))

    def drive(self):
        self.x -= self.x_change

    def check_boundary(self):
        global WIDTH

        if self.x < 0:
            self.x = WIDTH + 70 

    def check_collisions(self, car_x, car_y, player_x, player_y):
        distance = math.sqrt((math.pow(player_x - car_x, 2) + math.pow(player_y - car_y, 2)))
        if distance < 27:
            return True 

        else: 
            return False

# Making the house class 
class House:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def draw(self, surface):
        img = pygame.image.load("house.png")
        surface.blit(img, (self.x, self.y))

    def isWin(self, player_x, player_y, house_x, house_y):
        distance = math.sqrt((math.pow(player_x - house_x, 2) + math.pow(player_y - house_y, 2)))
        if distance < 27:
            return True 

        else: 
            return False


# Making the player objects 
player = Frog(300, 730)

# Making the right car objects 
car_1 = RightCar(car_1_x, 600, 1.75)
car_2 = RightCar(car_2_x, 400, 1.75)
car_3 = RightCar(car_3_x, 100, 1.75)

# Making the left car objects 
left_car_1 = LeftCar(670, 500, 1.75)
left_car_2 = LeftCar(670, 300, 1.75)
left_car_3 = LeftCar(670, 150, 1.75)

# Making the house objects 
house = House(300, 50)

# Main Game Loop 
running = True 
while running:
    # Fill the screen 
    screen.fill((BLACK))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.x += 20

            if event.key == pygame.K_LEFT:
                player.x -= 20

            if event.key == pygame.K_DOWN:
                player.y += 20 

            if event.key == pygame.K_UP:
                player.y -= 20


    # Boundary checking 
    if player.x <= 0:
        player.x = 0 

    if player.y <= 0: 
        player.y = 0

    if player.x > WIDTH - APROXIMATE_PLAYER_DIMENSIONS:
        player.x = WIDTH - APROXIMATE_PLAYER_DIMENSIONS

    if player.y > HEIGHT - APROXIMATE_PLAYER_DIMENSIONS:
        player.y = HEIGHT - APROXIMATE_PLAYER_DIMENSIONS

    # Checking for the collisions 
    collision_1 = car_1.check_collisions(car_1.x, car_1.y, player.x, player.y)
    if collision_1:
        time.sleep(0.05)
        print(Back.RED + 'GAME OVER, YOU LOSE!!!!')
        break

    collision_2 = car_2.check_collisions(car_2.x, car_2.y, player.x, player.y)
    if collision_2:
        time.sleep(0.05)
        print(Back.RED + 'GAME OVER, YOU LOSE!!!!')
        break

    collision_3 = car_3.check_collisions(car_3.x, car_3.y, player.x, player.y)
    if collision_3:
        time.sleep(0.05)
        print(Back.RED + 'GAME OVER, YOU LOSE!!!!')
        break

    collision_4 = left_car_1.check_collisions(left_car_1.x, left_car_1.y, player.x, player.y)
    if collision_4:
        time.sleep(0.05)
        print(Back.RED + 'GAME OVER, YOU LOSE!!!!')
        break

    collision_5 = left_car_2.check_collisions(left_car_2.x, left_car_2.y, player.x, player.y)
    if collision_5:
        time.sleep(0.05)
        print(Back.RED + 'GAME OVER, YOU LOSE!!!!')
        break

    collision_6 = left_car_3.check_collisions(left_car_3.x, left_car_3.y, player.x, player.y)
    if collision_6:
        time.sleep(0.05)
        print(Back.RED + 'GAME OVER, YOU LOSE!!!!')
        break

    # Condition for winning the game 
    game_win_collision = house.isWin(player.x, player.y, house.x, house.y)
    if game_win_collision:
        print(Back.GREEN + 'YOU WON!!!!')
        time.sleep(0.05)
        break 

    # Update the display 
    player.draw(screen)
    car_1.draw(screen)
    car_1.drive()
    car_1.check_boundary()
    car_2.draw(screen)
    car_2.drive()
    car_2.check_boundary()
    car_3.draw(screen)
    car_3.drive()
    car_3.check_boundary()
    left_car_1.draw(screen)
    left_car_1.drive()
    left_car_1.check_boundary()
    left_car_2.draw(screen)
    left_car_2.drive()
    left_car_2.check_boundary()
    left_car_3.draw(screen)
    left_car_3.drive()
    left_car_3.check_boundary()
    house.draw(screen)
    pygame.display.update()