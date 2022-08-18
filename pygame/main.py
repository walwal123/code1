from select import select
import pygame
import time
import sys
import random  # 랜덤 이벤트 할때 사용

pygame.init()

WHITE = (255, 255, 255)
screen_width = 1080
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

background_img = pygame.image.load("backgroundimg.png")
start_img = pygame.image.load("startimg.png")
# 화장실 버튼 이미지 정의 **
toilet_b = pygame.image.load("name.png")
# 확인 버튼 이미지 정의 **
ok_b = pygame.image.load("확인.png")
# 흡연실 버튼 이미지 정의 **
smoke_b = pygame.image.load("흡연실글자.png")

select_size = start_img.get_rect().size
w = select_size[0]
h = select_size[1]

clock = pygame.time.Clock()

drunk = 0
full = 0


# 버튼
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.bigimage = pygame.transform.scale(image, (int(w * 1.5), int(h * 1.5)))
        self.tempimage = image

    def draw(self):
        pos = pygame.mouse.get_pos()
        action = False

        if self.rect.collidepoint(pos):  # slef.rect 즉 버튼크기의 좌표 위로 마우스 좌표가 겹쳐지면
            self.image = self.bigimage  # 마우스가 버튼위로 올라왔을때 빅 이미지로 바꾸며 버튼이 커지는 이펙트 부여

            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:  # 0은 좌클릭 , 1은 휭클릭 2는 우클릭
                self.clicked = True
                action = True  # 눌리면 트루값 반납
                pygame.time.delay(500)  # 지연시간 설정**

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False  # 마우스를 때는순간 클릭은 거짓으로 바뀐다
        else:
            self.image = self.tempimage  # 마우스커서가 버튼 밖으로 나간다면 원래크기로 돌아간다

        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action


# 글씨쓰기
def draw_text(text, size, color, x, y):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)


# 게이지
def gauge():
    draw_text('Drunk: %d' % drunk, 40, WHITE, 80, 10)
    draw_text('Full: %d' % full, 40, WHITE, 75, 60)


pygame.display.set_caption("술자리 시뮬레이션")


# 시작화면
def mainmenu():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        screen.blit(background_img, (100, 90))
        start_button = Button(800, 500, start_img)

        if start_button.draw() == True:
            selectscreen()

        pygame.display.update()
        clock.tick(30)


# 화면전환(테이블)
def selectscreen():
    select = True
    while select:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        toilet_button = Button(100,500, toilet_b)  #화장실 버튼 생성 **
        smoke_button = Button(300,500, smoke_b)
        screen.blit(background_img, (100, 90))
        gauge()
        if smoke_button.draw() == True:
            smoke(drunk,full)

        if toilet_button.draw() == True: # 화장실 버튼눌림 **
            place_toilet(drunk,full)

        pygame.display.update()
        clock.tick(30)
# 이거 왜 에러;;
def event(p):
    random_p = random.randrange(1,100)
    occur = 100-(p+random_p)
    if occur < 0:
        a = 1
    return a

# 로딩을 거쳐서 장소이동을 하는 이유: 화장실 스크린과 메인화면 스크린은 크기를 비롯한 많은 변수들이 안맞으니 여기서 변해버린 변수들을 기존 값으로 초기화 하는 것이다
def loading():
    pygame.display.set_caption("술자리 시뮬레이션")
    screen = pygame.display.set_mode((screen_width, screen_height))

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0, 0, 0))
        ok_button = Button(900,500,ok_b)

        draw_text("Loading.....!!",150,(255,255,255),500,300)
        if ok_button.draw() == True:
            selectscreen()
        pygame.display.update()

# 화면전환 (화장실)
def place_toilet(d,f):

    turn = 1  # 임시 턴값
    chance = 0  # 랜덤이벤트 변수값

    toiletscreen_w = 800
    toiletscreen_h = 800
    run = True
    screen = pygame.display.set_mode((toiletscreen_w, toiletscreen_h))
    pygame.display.set_caption("화장실")
    background_t = pygame.image.load("toilet.png")
    place_name_t = pygame.image.load("name.png")
    select1_image = pygame.image.load("table.png")
    select2_image = pygame.image.load("select2.png")
    select3_image = pygame.image.load("select3.png")

    text_color = (255, 255, 255)
    font1 = pygame.font.Font("ARLRDBD.TTF", 40)
    font2 = pygame.font.Font("HBIOS-SYS.ttf", 20)  # 한글용 폰트
    text_s1 = font2.render("테이블로 돌아갔습니다...".format(), True, (1, 1, 1))
    text_s2 = font2.render("볼일을 봤습니다... 취기 하락".format(), True, (1, 1, 1))
    text_s3 = font2.render("토를 했습니다... 취기 크게하락, 포만감 하락".format(), True, (1, 1, 1))

    select1_button = Button(100, 500, select1_image)
    select2_button = Button(100, 610, select2_image)
    select3_button = Button(100, 710, select3_image)
    button_click = 0

    while run:
        random_p = random.randrange(1, 100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

            text_turn = font1.render("Turn : {} ".format(turn), True, (1, 1, 1))  # 계속 업데이트 해줘야 하기 때문에 와일문 안에 있습니다.
            text_d = font1.render("Drunk : {} ".format(d), True, (1, 1, 1))  # 게이지 함수 나오면 없어짐 1
            text_f = font1.render("full : {} ".format(f), True, (1, 1, 1))   # 없어짐 2
            screen.blit(background_t, (0, 0))
            screen.blit(place_name_t, (0, 0))
            screen.blit(text_turn, (200, 30))
            screen.blit(text_d, (200, 65))  # 없어짐 3
            screen.blit(text_f, (200, 100))  # 없어짐 4

            if select1_button.draw() == True:
                print("테이블로 돌아갔습니다")
                button_click = 1
                loading()

            if select2_button.draw() == True:
                print("볼일을 봤습니다... 취기 하락")
                occur = 100 - (chance + random_p)
                button_click = 2
                d -=1
                turn +=1
                chance += 25
                if occur < 0:
                    print("친구 이벤트 발생!!")

            if select3_button.draw() == True:
                print("토를 했습니다... 취기 크게하락, 포만감 하락")
                occur = 100 - (chance + random_p)
                button_click = 3
                d -=2
                turn +=2
                f -=2
                chance += 50
                if occur < 0:
                    print("친구 이벤트 발생!!")

            # 아래는 버튼클릭에 따라 다른 텍스트를 각각 게임화면에 전시한다
            if button_click == 1:
                screen.blit(text_s1, (200, 150))
            elif button_click == 2:
                screen.blit(text_s2, (200, 150))
            elif button_click == 3:
                screen.blit(text_s3, (200, 150))

            pygame.display.update()

    pygame.quit()
# 화면전환(흡연실) **
def smoke(d,f):
    turn =1
    pygame.display.set_caption("흡연실")
    screen = pygame.display.set_mode((800, 800))
    background_s = pygame.image.load("흡연실배경.png")
    name_s = pygame.image.load("흡연실글자.png")
    select1 = pygame.image.load("table.png")
    select2 = pygame.image.load("흡연실선택1.png")
    font1 = pygame.font.Font("ARLRDBD.TTF", 40)
    font2 = pygame.font.Font("HBIOS-SYS.ttf", 20)
    text_s1 = font2.render("담배를 피웠습니다... 취기 하락".format(), True, (1, 1, 1))
    run = True

    s1_button = Button(100,500,select1)
    s2_button = Button(100,610,select2)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            text_turn = font1.render("Turn : {} ".format(turn), True, (1, 1, 1))
            text_d = font1.render("Drunk : {} ".format(d), True, (1, 1, 1))  # 게이지 함수 나오면 없어짐 1
            text_f = font1.render("full : {} ".format(f), True, (1, 1, 1))  # 없어짐 2
            screen.blit(background_s, (0, 0))
            screen.blit(name_s, (0, 0))
            if s1_button.draw() == True:
                loading()
            if s2_button.draw() == True:
                button_click =1

        pygame.display.update()

# 화면전환(게임오버)
def gameover():
    g_o = True
    while g_o:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        draw_text('Game Over', 100, WHITE, 500, 300)
        restart_button = Button(500, 500, start_img)

        if restart_button.draw() == True:
            mainmenu()

        pygame.display.update()
        clock.tick(30)


gameover()