# import pygame

# """

# <Sound>.play(loop = 0, time = 0, fadein = 2000)
#        .stop()
#        .fadeout(ms)
#        .set_volume(0.0 -> 1.0)
#        .get_volume()
#        .get_length() 
# """
# pygame.init()

# window_resolution = (640, 480)

# launched = True

# pygame.display.set_caption("python #42 - jouer du son")

# window_surface = pygame.display.set_mode(window_resolution)

# celtic_song = pygame.mixer.Sound("celtic.ogg") # un fichier song à charge 

# #celtic_song.play()

# #celtic_song.play(0, 0, 5000)

# celtic = pygame.mixer.Sound("celtic.ogg")

# song = pygame.mixer.Sound("Song.ogg")

# celtic.play()

# song.play()

# pygame.display.flip()


# while launched:

#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:

#             launched = False







# import pygame

# """

# <Sound>.play(loop = 0, time = 0, fadein = 2000)
#        .stop()
#        .fadeout(ms)
#        .set_volume(0.0 -> 1.0)
#        .get_volume()
#        .get_length() 
# """
# pygame.init()

# window_resolution = (640, 480)

# launched = True

# pygame.display.set_caption("python #42 - jouer du son")

# window_surface = pygame.display.set_mode(window_resolution)

# celtic_song = pygame.mixer.Sound("celtic.ogg") # un fichier song à charge 

# #celtic_song.play()

# #celtic_song.play(0, 0, 5000)

# celtic = pygame.mixer.Sound("celtic.ogg")

# song = pygame.mixer.Sound("Song.ogg")

# celtic.play()

# song.play()

# pygame.display.flip()


# while launched:

#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:

#             launched = False
#         elif event.type == pygame.KEYDOWN:

#             if event.key == pygame.K_SPACE:

#                 song.stop()







# import pygame

# """

# <Sound>.play(loop = 0, time = 0, fadein = 2000)
#        .stop()
#        .fadeout(ms)
#        .set_volume(0.0 -> 1.0)
#        .get_volume()
#        .get_length() 
# """
# pygame.init()

# window_resolution = (640, 480)

# launched = True

# pygame.display.set_caption("python #42 - jouer du son")

# window_surface = pygame.display.set_mode(window_resolution)

# celtic_song = pygame.mixer.Sound("celtic.ogg") # un fichier song à charge 

# #celtic_song.play()

# #celtic_song.play(0, 0, 5000)

# celtic = pygame.mixer.Sound("celtic.ogg")

# song = pygame.mixer.Sound("Song.ogg")

# celtic.play()

# song.play()

# pygame.display.flip()


# while launched:

#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:

#             launched = False
#         elif event.type == pygame.KEYDOWN:

#             if event.key == pygame.K_SPACE:
                
#                 pygame.mixer.stop()









# import pygame

# """

# <Sound>.play(loop = 0, time = 0, fadein = 2000)
#        .stop()
#        .fadeout(ms)
#        .set_volume(0.0 -> 1.0)
#        .get_volume()
#        .get_length() 
# """
# pygame.init()

# window_resolution = (640, 480)

# launched = True

# pygame.display.set_caption("python #42 - jouer du son")

# window_surface = pygame.display.set_mode(window_resolution)

# celtic_song = pygame.mixer.Sound("celtic.ogg") # un fichier song à charge 

# #celtic_song.play()

# #celtic_song.play(0, 0, 5000)

# celtic = pygame.mixer.Sound("celtic.ogg")

# song = pygame.mixer.Sound("Song.ogg")

# celtic.play()

# song.play()

# pygame.display.flip()


# while launched:

#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:

#             launched = False
#         elif event.type == pygame.KEYDOWN:

#             if event.key == pygame.K_SPACE:
                
#                 pygame.mixer.pause()

#             elif event.key == pygame.K_P:

#                 pygame.mixer.unpause()













# import pygame

# """

# <Sound>.play(loop = 0, time = 0, fadein = 2000)
#        .stop()
#        .fadeout(ms)
#        .set_volume(0.0 -> 1.0)
#        .get_volume()
#        .get_length() 
# """
# pygame.init()

# window_resolution = (640, 480)

# launched = True

# pygame.display.set_caption("python #42 - jouer du son")

# window_surface = pygame.display.set_mode(window_resolution)


# pygame.mixer.music.load("celtic.ogg")

# pygame.mixer.music.play()

# pygame.display.flip()


# while launched:

#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:

#             launched = False
#         elif event.type == pygame.KEYDOWN:

#             pass
















import pygame

"""

<Sound>.play(loop = 0, time = 0, fadein = 2000)
       .stop()
       .fadeout(ms)
       .set_volume(0.0 -> 1.0)
       .get_volume()
       .get_length() 
"""
pygame.init()

window_resolution = (640, 480)

launched = True

pygame.display.set_caption("python #42 - jouer du son")

window_surface = pygame.display.set_mode(window_resolution)


pygame.mixer.music.load("celtic.ogg")

pygame.mixer.music.play()

pygame.display.flip()


while launched:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            launched = False
        elif event.type == pygame.KEYDOWN:

            #pygame.mixer.music.pause()

            pygame.mixer.music.rewind()