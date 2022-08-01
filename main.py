import pygame
pygame.init()

win = pygame.display.set_mode((400,700))
pygame.display.set_caption("space jumper")

bg = pygame.image.load("Images/space.png")
bg = pygame.transform.scale(bg,(400,700))
playerImage = pygame.image.load("Images/Alien.png")
clock = pygame.time.Clock()
score = 0

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.jumpCount = 10
        self.noMove = True
def redrawWindow():
    win.blit(bg,(0,0))
    text = font.render("Score" + str(score), 1, (0,0,0))
    win.blit

###main loop###
font = pygame.font.SysFont("comicsans",30,True)
run = True
character = player(200,600,64,64)


while run:
    win.blit(bg,(0,0))
    win.blit(character)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()