# import time

# import pygame

# pygame.init()

# window_resolution = (640, 480)

# pygame.display.set_caption("python #39")

# window_surface = pygame.display.set_mode(window_resolution) # Surface

# pygame.display.flip()

# print(pygame.font.get_fonts())

# launched = True

# while launched:

#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:

#             launched = False





# import time

# import pygame

# pygame.init()

# window_resolution = (640, 480)

# blue = (0, 75, 255)

# pygame.display.set_caption("python #39")

# window_surface = pygame.display.set_mode(window_resolution)

# arail_font = pygame.font.SysFont("arial",30)

# hello_text_surface = arail_font.render("Bonjour à tous" ,False ,blue)

# window_surface.blit(hello_text_surface,[10, 10])

# pygame.display.flip()


# launched = True

# while launched:

#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:

#             launched = False






import pygame

"""
arial_font.set_bold()
arial_font.set_italic()
arial_font.set_underline()
"""

pygame.init()

window_resolution = (640, 480)

blank = (255, 255, 255)

pygame.display.set_caption("python #39")

window_surface = pygame.display.set_mode(window_resolution)

arial_font = pygame.font.Font("introduction_pygame/afficher_du_texte/Roze Belinda - Regular.ttf",30)

hello_text_surface = arial_font.render("Bonjour à tous" ,True ,blank)

window_surface.blit(hello_text_surface,[10, 10])

pygame.display.flip()


launched = True

while launched:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            launched = False
