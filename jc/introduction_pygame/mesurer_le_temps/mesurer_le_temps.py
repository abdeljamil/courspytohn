# import pygame

# pygame.init()

# window_resolution = (640, 480)

# blue_color = (132, 180, 255)

# red_color = (255, 0, 0)

# pygame.display.set_caption("python #41 - mesurer le temps")

# window_surface = pygame.display.set_mode(window_resolution)

# arail_font = pygame.font.SysFont("arial",30)

# hello_text_surface = arail_font.render("Bonjour à tous !!" ,False ,blue_color)

# print(pygame.time.get_ticks())

# window_surface.blit(hello_text_surface,[50, 50])

# pygame.display.flip()

# pygame.time.wait(5000)

# hello_text_surface = arail_font.render("Bonjour à tous !!" ,False ,red_color)

# print(pygame.time.get_ticks())

# window_surface.blit(hello_text_surface,[50, 50])

# pygame.display.flip()



# launched = True

# while launched:

#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:

#             launched = False










# import pygame

# pygame.init()

# window_resolution = (640, 480)

# blue_color = (132, 180, 255)

# red_color = (255, 0, 0)

# pygame.display.set_caption("python #41 - mesurer le temps")

# window_surface = pygame.display.set_mode(window_resolution)

# arail_font = pygame.font.SysFont("arial",30)

# hello_text_surface = arail_font.render("Bonjour à tous !!" ,False ,blue_color)

# print(pygame.time.get_ticks())

# window_surface.blit(hello_text_surface,[50, 50])

# pygame.display.flip()

# pygame.time.delay(5000)

# hello_text_surface = arail_font.render("Bonjour à tous !!" ,False ,red_color)

# print(pygame.time.get_ticks())

# window_surface.blit(hello_text_surface,[50, 50])

# pygame.display.flip()



# launched = True

# while launched:

#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:

#             launched = False










# import pygame

# pygame.init()

# clock = pygame.time.Clock()

# window_resolution = (640, 480)

# blue_color = (132, 180, 255)


# pygame.display.set_caption("python #41 - mesurer le temps")

# window_surface = pygame.display.set_mode(window_resolution)

# arail_font = pygame.font.SysFont("arial",30)

# hello_text_surface = arail_font.render("Bonjour à tous !!" ,False ,blue_color)


# window_surface.blit(hello_text_surface,[50, 50])

# pygame.display.flip()

# launched = True

# while launched:

#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:

#             launched = False

#     #clock.tick(60) #30 images par seconde (30 fps)
#     print(f"{clock.get_fps()} FPS")
  






# import pygame

# pygame.init()

# clock = pygame.time.Clock()

# window_resolution = (640, 480)

# black_color = (0, 0,0)

# blue_color = (132, 180, 255)


# pygame.display.set_caption("python #41 - mesurer le temps")

# window_surface = pygame.display.set_mode(window_resolution)

# arail_font = pygame.font.SysFont("arial",30)


# pygame.display.flip()

# launched = True

# while launched:

#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:

#             launched = False

#     clock.tick(60) #30 images par seconde (30 fps)

#     window_surface.fill(black_color)

#     hello_text_surface = arail_font.render(f"{clock.get_fps()} FPS" ,True ,blue_color)

#     window_surface.blit(hello_text_surface,[50, 50])

#     pygame.display.flip()

  







import pygame

pygame.init()

clock = pygame.time.Clock()

pygame.time.set_timer(pygame.USEREVENT,2000)

window_resolution = (640, 480)

black_color = (0, 0,0)

blue_color = (132, 180, 255)


pygame.display.set_caption("python #41 - mesurer le temps")

window_surface = pygame.display.set_mode(window_resolution)

arail_font = pygame.font.SysFont("arial",30)


pygame.display.flip()

launched = True

while launched:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            launched = False
        elif event.type == pygame.USEREVENT:
                window_surface.fill(black_color)

                hello_text_surface = arail_font.render(f"{clock.get_fps():.2f} FPS" ,True ,blue_color)

                window_surface.blit(hello_text_surface,[50, 50])

                pygame.display.flip()    

    clock.tick(60) #30 images par seconde (30 fps)



  