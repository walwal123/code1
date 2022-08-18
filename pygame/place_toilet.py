import pygame

pygame.init()

# 게임 내내 쓸 변수들
drunk = 0  # 플레이어 취기
turn = 0   # 턴 수
full = 0   # 포만감
chance = 0 # 랜덤 이벤트 발생할때 쓸 변수

screen_w = 800
screen_h = 800
run = True
screen = pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption("화장실")
background = pygame.image.load("C:/Users/PC/PycharmProjects/pythonTest/pygame/toilet.png")
place_name = pygame.image.load("C:/Users/PC/PycharmProjects/pythonTest/pygame/name.png")
select1_image = pygame.image.load("C:/Users/PC/PycharmProjects/pythonTest/pygame/table.png")
select2_image = pygame.image.load("C:/Users/PC/PycharmProjects/pythonTest/pygame/select2.png")
select3_image = pygame.image.load("C:/Users/PC/PycharmProjects/pythonTest/pygame/select3.png")
# 버튼의 크기는 250,50 이다
select_size = select1_image.get_rect().size
w = select_size[0]
h= select_size[1]
text_color = (255,255,255)
font = pygame.font.Font("C:/Users/PC/PycharmProjects/pythonTest/pygame/ARLRDBD.TTF",40)
font2 = pygame.font.Font("C:/Users/PC/PycharmProjects/pythonTest/pygame/HBIOS-SYS.ttf",20)
text_s1 = font2.render("테이블로 돌아갔습니다...".format(), True, (1, 1, 1))
text_s2 = font2.render("볼일을 봤습니다... 취기 하락".format(),True,(1,1,1))
text_s3 = font2.render("토를 했습니다... 취기 크게하락, 포만감 하락".format(),True,(1,1,1))

class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        self.bigimage = pygame.transform.scale(image, (int(w*1.5),int(h*1.5)))
        self.tempimage = image

    def draw(self):
        pos = pygame.mouse.get_pos()
        action = False

        if self.rect.collidepoint(pos): # slef.rect 즉 버튼크기의 좌표 위로 마우스 좌표가 겹쳐지면
            self.image = self.bigimage #마우스가 버튼위로 올라왔을때 빅 이미지로 바꾸며 버튼이 커지는 이펙트 부여

            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: # 0은 좌클릭 , 1은 휭클릭 2는 우클릭
                self.clicked = True
                action = True #눌리면 트루값 반납

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False #마우스를 때는순간 클릭은 거짓으로 바뀐다
        else:
            self.image = self.tempimage #마우스커서가 버튼 밖으로 나간다면 원래크기로 돌아간다

        screen.blit(self.image,(self.rect.x,self.rect.y))
        return action

select1_button = Button(100,500,select1_image)
select2_button = Button(100,610,select2_image)
select3_button = Button(100,710,select3_image)
button_click = 0

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        text_turn = font.render("Turn : {} ".format(turn), True, (1, 1, 1)) # 계속 업데이트 해줘야 하기 때문에 와일문 안에 있습니다.
        screen.blit(background,(0,0))
        screen.blit(place_name,(0,0))
        screen.blit(text_turn, (200, 30))

        if select1_button.draw() == True:
            print("테이블로 돌아갔습니다")
            turn +=1
            button_click =1

        if select2_button.draw() == True:
            print("볼일을 봤습니다... 취기 하락")
            turn +=1
            button_click =2
            drunk -=1
        if select3_button.draw() == True:
            print("토를 했습니다... 취기 크게하락, 포만감 하락")
            turn +=2
            button_click =3
            drunk -=2
            full -=1
        # 아래는 버튼클릭에 따라 다른 텍스트를 각각 게임화면에 전시한다
        if button_click == 1:
            screen.blit(text_s1, (200, 80))
        elif button_click ==2:
            screen.blit(text_s2, (200,80))
        elif button_click ==3:
            screen.blit(text_s3, (200,80))

        pygame.display.update()


pygame.quit()