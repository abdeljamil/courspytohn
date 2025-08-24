import pygame

pygame.init()
window_resolution = (900,700)
blank_color = (255,255,255)
black_color = (0,0,0)


pygame.display.set_caption("python #37")
window_surface = pygame.display.set_mode(window_resolution) # Images
cat_image = pygame.image.load("introduction_pygame/afficher_images/Sans titre.jpg")# Retourne une surface

cat_image.convert()
cat_image.set_colorkey(black_color)


launched = True

while launched:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            launched = False
    # corps du programme 
    window_surface.fill(blank_color)
    window_surface.blit(cat_image,[10,10])
    pygame.display.flip()        