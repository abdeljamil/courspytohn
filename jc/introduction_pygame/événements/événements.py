# import pygame

# pygame.init()

# window_resolution = (640, 480)

# while_color = (255, 255, 255)

# black_color = (0, 0, 0)

# pygame.display.set_caption("python #40 événements")

# window_surface = pygame.display.set_mode(window_resolution,pygame.RESIZABLE)

# arial_font = pygame.font.SysFont("arial",30)

# dimension_text = arial_font.render("{}".format(window_resolution), True, while_color)

# window_surface.blit(dimension_text, [10, 10])

# pygame.display.flip()


# launched = True

# while launched:

#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:

#             launched = False

#         elif event.type == pygame.VIDEORESIZE:

#             window_surface.fill(black_color)

#             dimension_text = arial_font.render("{} x {}".format(event.w, event.h), True, while_color)

#             window_surface.blit(dimension_text, [10, 10])

#             pygame.display.flip()






# import pygame

# window_resolution = (640, 480)

# pygame.init()

# pygame.display.set_caption("python #40 événements")

# window_surface = pygame.display.set_mode(window_resolution)

# pygame.display.flip()


# launched = True

# while launched:

#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:

#             launched = False

#         elif event.type == pygame.KEYDOWN:

#             if event.key == pygame.K_UP:

#                 print("Haut")

#             elif event.key == pygame.K_DOWN :
                  
#                 print("Bas")

#             elif event.key == pygame.K_LEFT:

#                  print("Gauche")
                
#             elif event.key == pygame.K_RIGHT:  

#                 print("Droit")
                
#             else :
#                 print("Autre touche....") 











import pygame

window_resolution = (640, 480)

pygame.init()

pygame.display.set_caption("python #40 événements")

window_surface = pygame.display.set_mode(window_resolution)

pygame.display.flip()


launched = True

while launched:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            launched = False

        if event.type == pygame.MOUSEMOTION:
            
            print("{}".format(event.pos))
