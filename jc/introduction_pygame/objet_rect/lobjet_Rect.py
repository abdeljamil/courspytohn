# import time

# import pygame

# """
# pygame.Rect(x,y,width,height)
# Rect.copy()
# Rect.move() | Rect.move_ip()
# Rect.inflate()
# Rect.colliderect()

# """

# pygame.init()

# window_resolution = (640, 480)

# black = (0, 0, 0)

# red = (255, 0, 0)

# i = 0 

# pygame.display.set_caption("python #38 - l'objet Rect")

# window_surface = pygame.display.set_mode(window_resolution) # Surface

# my_rect = pygame.Rect(10, 10, 250, 80)

# pygame.draw.rect(window_surface, red, my_rect)

# pygame.display.flip()

# while i < 10 :

#     time.sleep(.0800)

#     window_surface.fill(black)

#     my_rect.x += 10

#     my_rect.y += 10

#     pygame.draw.rect(window_surface, red, my_rect)

#     pygame.display.flip()

#     i += 1

# launched = True

# while launched:

#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:

#             launched = False




import time

import pygame

"""
pygame.Rect(x,y,width,height)
Rect.copy()
Rect.move() | Rect.move_ip()
Rect.inflate()
Rect.colliderect()

"""

pygame.init()

window_resolution = (640, 480)

black = (0, 0, 0)

red = (255, 0, 0)

blue = (0, 75, 255)

i = 0 

pygame.display.set_caption("python #38 - l'objet Rect")

window_surface = pygame.display.set_mode(window_resolution) # Surface

my_rect = pygame.Rect(10, 100, 25, 25)

my_block = pygame.Rect(600 ,50, 20, 300)

pygame.draw.rect(window_surface, red, my_rect)

pygame.draw.rect(window_surface, blue, my_block)

pygame.display.flip()

launched = True

while launched:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            launched = False

    while not my_rect.colliderect(my_block):
        
        time.sleep(.010)

        window_surface.fill(black)

        my_rect.x += 1

        pygame.draw.rect(window_surface, red, my_rect)

        pygame.draw.rect(window_surface, blue, my_block)

        pygame.display.flip()


