import pygame
import random
pygame.init()

win = pygame.display.set_mode((1000,500))
pygame.display.set_caption("space jumper")

bg = pygame.image.load("Images/space.png")
bg = pygame.transform.scale(bg,(1000,500))
playerImage = pygame.image.load("Images/Alien.png")
playerImage = pygame.transform.scale(playerImage,(64,64))
platform = pygame.image.load("Images/platform.png")

clock = pygame.time.Clock()
score = 0
mouseX,mouseY = (0,0)
gameOn = False

class pcharacter(object):

    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.jumpCount = 12
        self.jumpMax =12
        self.still = True
    def draw(self,win):
        win.blit(playerImage,(self.x,self.y))

###functions for different screens###

def redrawGameWindow():
    clock.tick(30)
    win.blit(bg,(0,0))
    text = gameFont.render("Score: " + str(score),1,(0,0,0))
    win.blit(text,(800,25))
    player.draw(win)
    pygame.display.update()

def menuWindow():
    global button_rect
    global mouseX
    global mouseY
    global gameOn
    win.blit(bg,(0,0))
    button_text_color = (0,0,0)
    title_text_color = (25,40,156)
    button_color = (25,40,156)
    button_over_color = (6,17,99)
    button_width = 200
    button_height = 100
    button_rect = [(win.get_width() - button_width) / 2,
                   win.get_height() / 2 - button_height / 2,
                   button_width, button_height]
    button_font = pygame.font.SysFont("comicsans",20)
    button_text = button_font.render("PLAY", True, button_text_color)
    title_font = pygame.font.SysFont("impact", 50)
    title_text = title_font.render("SPACE JUMPER", True, title_text_color)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX,mouseY = event.pos
            if(button_rect[0] <= mouseX <= button_rect[0] + button_rect[2] and
            button_rect[1] <= mouseY <= button_rect[1] + button_rect[3]):
                gameOn = True
        if event.type == pygame.MOUSEMOTION:
            mouseX,mouseY = event.pos
    if (button_rect[0] <= mouseX <= button_rect[0] + button_rect[2] and
            button_rect[1] <= mouseY <= button_rect[1] + button_rect[3]):
        pygame.draw.rect(win, button_over_color, button_rect)
    else:
        pygame.draw.rect(win, button_color, button_rect)
    win.blit(button_text, (button_rect[0] + (button_width - button_text.get_width()) / 2,
                              button_rect[1] + (button_height / 2 - button_text.get_height() / 2)))
    win.blit(title_text,(356.625,100))

    pygame.display.update()

gameFont = pygame.font.SysFont("comicsans",20,True)
run = True
player = pcharacter(500,400,64,64)

def gameScreen():
    global keys
    global score

    if keys[pygame.K_LEFT] and player.x > player.vel:
        player.x -= player.vel
    if keys[pygame.K_RIGHT] and player.x < 1000 - player.width - player.vel:
        player.x += player.vel
    if not(player.isJump):
        if (player.y + player.height) >= 400:
            player.isJump = True
            print("cum")
    else:
        if player.jumpCount >= -player.jumpMax:
            player.y -= (player.jumpCount*abs(player.jumpCount))*0.5
            print("jump grav", player.y)
            player.jumpCount -= 1
            print("player position",(player.jumpCount-player.y))
        else:
            player.jumpCount = player.jumpMax
            player.isJump = False
            score += 1


    redrawGameWindow()


###main loop###
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if gameOn == True:
        gameScreen()
    else:
        menuWindow()