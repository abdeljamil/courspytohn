# import pygame

# pygame.init()
# screen = pygame.display.set_mode((640,480))

# launched = True

# while launched:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             launched = False




import pygame

pygame.init()
res = (640,480)
screen = pygame.display.set_mode(res)

launched = True

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False