import pygame

pygame.init()

screen_w = 800
screen_h = 800
run = True
screen = pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption("화장실")


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()