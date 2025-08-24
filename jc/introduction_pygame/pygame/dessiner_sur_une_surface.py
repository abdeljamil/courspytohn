# import pygame

# pygame.init()
# window_resolution = (640,480)
# blue_color = (89,152,255)
# back_color = (0,0,0)

# pygame.display.set_caption("python #36")
# window_surface = pygame.display.set_mode(window_resolution) # Surface
# window_surface.fill(blue_color)
# pygame.draw.line(window_surface,back_color,[10,10],[100,100])

# pygame.display.flip()
# launched = True

# while launched:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             launched = False





# import pygame

# # Objet Surface,rect
# #Rect(left,top,width,reft)
# pygame.init()
# window_resolution = (640,480)
# blue_color = (89,152,255)
# back_color = (0,0,0)

# pygame.display.set_caption("python #36")
# window_surface = pygame.display.set_mode(window_resolution) # Surface
# window_surface.fill(blue_color)
# rect_form = pygame.Rect(10,10,150,65)
# pygame.draw.rect(window_surface,back_color,rect_form)

# pygame.display.flip()
# launched = True

# while launched:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             launched = False










# import pygame

# # Objet Surface,rect
# #Rect(left,top,width,reft)
# pygame.init()
# window_resolution = (640,480)
# blue_color = (89,152,255)
# back_color = (0,0,0)

# pygame.display.set_caption("python #36")
# window_surface = pygame.display.set_mode(window_resolution) # Surface
# window_surface.fill(blue_color)
# rect_form = pygame.Rect(10,10,150,65)
# pygame.draw.rect(window_surface,back_color,rect_form,5)

# pygame.display.flip()
# launched = True

# while launched:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             launched = False






# import pygame

# # Objet Surface,rect
# #Rect(left,top,width,height)
# pygame.init()
# window_resolution = (640,480)
# blue_color = (89,152,255)
# back_color = (0,0,0)

# pygame.display.set_caption("python #36")
# window_surface = pygame.display.set_mode(window_resolution) # Surface
# window_surface.fill(blue_color)
# #rect_form = pygame.Rect(10,10,150,65)
# pygame.draw.circle(window_surface,back_color,[150,100],50,2)

# pygame.display.flip()
# launched = True

# while launched:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             launched = False









import pygame

# Objet Surface,rect
#Rect(left,top,width,height)
pygame.init()
window_resolution = (640,480)
blue_color = (89,152,255)
back_color = (0,0,0)

pygame.display.set_caption("python #36")
window_surface = pygame.display.set_mode(window_resolution) # Surface
window_surface.fill(blue_color)
coords = [(10,10),(100,10),(30,50),(40,60)]
pygame.draw.polygon(window_surface,back_color,coords,2)

pygame.display.flip()
launched = True

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
