import pygame
import time
import sys


pygame.init()

white = (255, 255, 255)

titleImg = pygame.image.load("C:/Users/PC/PycharmProjects/pythonTest/pygame/table.png")
startImg = pygame.image.load("C:/Users/PC/PycharmProjects/pythonTest/pygame/select2.png")
quitImg = pygame.image.load("C:/Users/PC/PycharmProjects/pythonTest/pygame/select3.png")
clickStartImg = pygame.image.load("C:/Users/PC/PycharmProjects/pythonTest/pygame/select2.png")
clickQuitImg = pygame.image.load("C:/Users/PC/PycharmProjects/pythonTest/pygame/select3.png")


display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("헝그리  댕댕이")

clock = pygame.time.Clock()



class Button:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            gameDisplay.blit(img_act,(x_act, y_act))
            if click[0] and action != None:
                time.sleep(1)
                action()
        else:
            gameDisplay.blit(img_in,(x,y))

def quitgame():
    pygame.quit()
    sys.exit()


def mainmenu():

    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(white)
        
        titletext = gameDisplay.blit(titleImg, (220,150))
        startButton = Button(startImg,280,260,60,20,clickStartImg,273,258,None)
        quitButton = Button(quitImg,445,260,60,20,clickQuitImg,440,258,quitgame)
        pygame.display.update()
        clock.tick(15)
        

mainmenu()
game_loop()
