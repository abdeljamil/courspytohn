
# import pygame

# pygame.init()
# res = (640,480)
# screen = pygame.display.set_mode(res)
# print(type(screen))
# launched = True

# while launched:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             launched = False




# import pygame

# """
# pygame.FULLSCREEN
# pygame.RESIZABLE
# pygame.NOFRAME

# pygame.OPENGL
# pygame.HWSURFACE
# pygame.DOUBLEBUF
# """
# pygame.init()
# res = (640,480)
# screen = pygame.display.set_mode(res)
# screen = pygame.display.set_mode(res,pygame.NOFRAME | pygame.RESIZABLE)
# print(type(screen))
# launched = True

# while launched:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             launched = False







# import pygame

# """
# pygame.FULLSCREEN
# pygame.RESIZABLE
# pygame.NOFRAME

# pygame.OPENGL
# pygame.HWSURFACE
# pygame.DOUBLEBUF
# """

# res = (640,480)
# pygame.init()
# window_surface = pygame.display.set_mode(res)

# launched = True

# while launched:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             launched = False
#     res = (500,500)
#     window_surface = pygame.display.set_mode(res)        







# import pygame

# """
# pygame.FULLSCREEN
# pygame.RESIZABLE
# pygame.NOFRAME

# pygame.OPENGL
# pygame.HWSURFACE
# pygame.DOUBLEBUF
# """

# res = (640,480)

# pygame.init()
# window_surface = pygame.display.set_mode(res)

# print(pygame.display.Info())

# launched = True
# while launched:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             launched = False





# import pygame

# """
# pygame.FULLSCREEN
# pygame.RESIZABLE
# pygame.NOFRAME

# pygame.OPENGL
# pygame.HWSURFACE
# pygame.DOUBLEBUF
# """

# res = (640,480)

# pygame.init()
# window_surface = pygame.display.set_mode(res)

# print(pygame.get_sdl_version())

# launched = True
# while launched:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             launched = False





import pygame

"""
pygame.FULLSCREEN
pygame.RESIZABLE
pygame.NOFRAME

pygame.OPENGL
pygame.HWSURFACE
pygame.DOUBLEBUF
"""

res = (640,480)

pygame.init()
pygame.display.set_caption("Mon Programme PYGAME")
window_surface = pygame.display.set_mode(res)

print(pygame.get_sdl_version())

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

