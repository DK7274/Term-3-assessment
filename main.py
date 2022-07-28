import pygame
pygame.init()

win = pygame.display.set_mode((400,700))

bg = pygame.image.load("Images/space.png")
bg = pygame.transform.scale(bg,(400,700))

clock = pygame.time.Clock()

###main loop###
run = True
while run:
    win.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()