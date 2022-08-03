import pygame
import random
pygame.init()

#setting up window#
win = pygame.display.set_mode((1000,500))
pygame.display.set_caption("space jumper")

#seting up images and scaling them correclty#
bg = pygame.image.load("Images/space.png")
bg = pygame.transform.scale(bg,(1000,500))
playerImage = pygame.image.load("Images/Alien.png")
playerImage = pygame.transform.scale(playerImage,(64,64))
platform = pygame.image.load("Images/platform.png")
platform = pygame.transform.scale(platform,(100,50))

#setting up various variables#
clock = pygame.time.Clock()
score = 0
mouseX,mouseY = (0,0) #needed for menu screen, gets cusrsor position#
gameOn = False #variable used to start the game#
platformRandom = False
gameStart = True
gameOver = False

#limits for randomizer#
platformXLimitA = 0
platformXLimitB = 1000-300
platformYLimitA = 0
platformYLimitB = 500-100

#variables for platform detection and movement of character#
platform1Hit = True
platform2Hit = True
platform3Hit = True
platform4Hit = True
platform5Hit = True
platform6Hit = True
playerPos2 = 0
hitPlatform = False

#class for character#
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
        self.goingDown = False
    def draw(self,win):
        win.blit(playerImage,(self.x,self.y))

###set of classes for platforms###
class platform_1(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.isContact = False
    def draw(self,win):
        win.blit(platform,(self.x,self.y))

class platform_2(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.isContact = False
    def draw(self, win):
        win.blit(platform, (self.x, self.y))


class platform_3(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.isContact = False
    def draw(self,win):
        win.blit(platform,(self.x,self.y))

class platform_4(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.isContact = False
    def draw(self,win):
        win.blit(platform,(self.x,self.y))

class platform_5(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.isContact = False
    def draw(self,win):
        win.blit(platform,(self.x,self.y))

class platform_6(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.isContact = False
    def draw(self,win):
        win.blit(platform,(self.x,self.y))
#######################################

###functions for different screens###

def redrawGameWindow():
    clock.tick(30)
    win.blit(bg,(0,0))
    text = gameFont.render("Score: " + str(score),1,(0,0,0))
    win.blit(text,(800,25))
    player.draw(win)
    platform1.draw(win)
    platform2.draw(win)
    platform3.draw(win)
    platform4.draw(win)
    platform5.draw(win)
    platform6.draw(win)
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

def platformReset():
    global platformRandom
    global platform1Hit
    global platform2Hit
    global platform3Hit
    global platform4Hit
    global platform5Hit
    global platform6Hit
    platformRandom = True
    platform1Hit = True
    platform2Hit = True
    platform3Hit = True
    platform4Hit = True
    platform5Hit = True
    platform6Hit = True

def gameOverWindow():
    win.blit(bg, (0, 0))
    button_text_color = (0, 0, 0)
    title_text_color = (25, 40, 156)
    title_font = pygame.font.SysFont("impact", 50)
    title_text = title_font.render("GAME OVER", True, title_text_color)
    win.blit(title_text, (356.625, 100))

    pygame.display.update()

gameFont = pygame.font.SysFont("comicsans",20,True)
run = True
player = pcharacter(500,500,64,64)
platform1 = platform_1(100,100,100,50)
platform2 = platform_2(100,200,100,50)
platform3 = platform_3(100,300,100,50)
platform4 = platform_4(200,100,100,50)
platform5 = platform_5(200,200,100,50)
platform6 = platform_6(200,300,100,50)

def platformRandomizer():
    global xRandom
    global yRandom
    global platform1
    global platform2
    global platform3
    global platform4
    global platform5
    global platform6
    global platformRandom
    global platform1Hit
    global platform2Hit
    global platform3Hit
    global platform4Hit
    global platform5Hit
    global platform6Hit

    if platform1Hit == True:
        xRandom = random.randint(platformXLimitA, platformXLimitB)
        yRandom = random.randint(platformYLimitA, platformYLimitB)
        platform1 = platform_1(xRandom,yRandom,100,50)
        platform1Hit = False
    elif platform2Hit == True:
        xRandom = random.randint(platformXLimitA, platformXLimitB)
        yRandom = random.randint(platformYLimitA, platformYLimitB)
        platform2 = platform_2(xRandom,yRandom,100,50)
        platform2Hit = False
    elif platform3Hit == True:
        xRandom = random.randint(platformXLimitA, platformXLimitB)
        yRandom = random.randint(platformYLimitA, platformYLimitB)
        platform3 = platform_3(xRandom,yRandom,100,50)
        platform3Hit = False
    elif platform4Hit == True:
        xRandom = random.randint(platformXLimitA, platformXLimitB)
        yRandom = random.randint(platformYLimitA, platformYLimitB)
        platform4 = platform_4(xRandom,yRandom,100,50)
        platform4Hit = False
    elif platform5Hit == True:
        xRandom = random.randint(platformXLimitA, platformXLimitB)
        yRandom = random.randint(platformYLimitA, platformYLimitB)
        platform5 = platform_5(xRandom,yRandom,100,50)
        platform5Hit = False
    elif platform6Hit == True:
        xRandom = random.randint(platformXLimitA, platformXLimitB)
        yRandom = random.randint(platformYLimitA, platformYLimitB)
        platform6 = platform_6(xRandom,yRandom,100,50)
        platform6Hit = False
    else:
        platformRandom = True
#checks if character is moving downwards on screen#
def downCheck():
    global playerPos2
    global goingDown
    playerPos1 = player.y
    if playerPos1 >= playerPos2:
        goingDown = True
        print("going down")
        hitCheck()
    playerPos2 = player.y
##

##checks if the charcter hits the platform while going down##
def hitCheck():
    global hitPlatform
    global platformRandom
    global platform1Hit
    global platform2Hit
    global platform3Hit
    global platform4Hit
    global platform5Hit
    global platform6Hit
    if player.y + player.height >= platform1.y and player.y + player.height <= platform1.y + platform1.height and player.x + player.width <= platform1.x + platform1.width and player.x >= platform1.x:
        hitPlatform = True
        platform1Hit = True
        print("hit platform1")
    elif player.y + player.height >= platform2.y and player.y + player.height <= platform2.y + platform2.height and player.x + player.width <= platform2.x + platform2.width and player.x >= platform2.x:
        hitPlatform = True
        platform2Hit = True
        print("hit platform2")
    elif player.y + player.height >= platform3.y and player.y + player.height <= platform3.y + platform3.height and player.x + player.width <= platform3.x + platform3.width and player.x >= platform3.x:
        hitPlatform = True
        platform3Hit = True
        print("hit platform3")
    elif player.y + player.height >= platform4.y and player.y + player.height <= platform4.y + platform4.height and player.x + player.width <= platform4.x + platform4.width and player.x >= platform4.x:
        hitPlatform = True
        platform4Hit = True
        print("hit platform4")
    elif player.y + player.height >= platform5.y and player.y + player.height <= platform5.y + platform5.height and player.x + player.width <= platform5.x + platform5.width and player.x >= platform5.x:
        hitPlatform = True
        platform5Hit = True
        print("hit platform5")
    elif player.y + player.height >= platform6.y and player.y + player.height <= platform6.y + platform6.height and player.x + player.width <= platform6.x + platform6.width and player.x >= platform6.x:
        hitPlatform = True
        platform6Hit = True
        print("hit platform6")
    else:
        platformRandom = False
######



def gameScreen():
    global keys
    global score
    global hitPlatform
    global goingDown
    global gameStart
    global gameOver
    global gameOn
    global platformRandom

    if platformRandom == False:
        platformRandomizer()
    if keys[pygame.K_LEFT] and player.x > player.vel:
        player.x -= player.vel
    if keys[pygame.K_RIGHT] and player.x < 1000 - player.width - player.vel:
        player.x += player.vel
    if not(player.isJump):
        if (player.y + player.height) >= 500 and gameStart == True:
            player.isJump = True
            print("jump!")
            gameStart = False
    else:
        if player.jumpCount + 5 >= -player.jumpMax:
            player.y -= (player.jumpCount*abs(player.jumpCount))*0.5
            print("jump grav", player.y)
            player.jumpCount -= 1
            print(player.jumpCount,"jumpcount")
            print("player position",(player.jumpCount-player.y))
            downCheck()
            if hitPlatform == True:
                player.jumpCount = player.jumpMax
                hitPlatform = False
                score += 1
            elif player.y >= 550:
                gameOver = True
                gameOn = False
                gameOverWindow()
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
    elif gameOver == True:
        gameOverWindow()
    else:
        menuWindow()
###################
pygame.quit()