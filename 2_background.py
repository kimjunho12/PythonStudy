import pygame

pygame.init() # 초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 크기 설정



# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# 배경 이미지 불러오기
background = pygame.image.load("./background.png")

#이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get():    # 필수 부분 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT :  # 창 닫기 버튼 눌렀을 때
            running = False

    #screen.blit(background, (0,0))      # 배경 그리기
    screen.fill((0, 0, 255))

    pygame.display.update()             # 게임 화면 다시 그리기! 반복 호출

# 게임 종료 시 
# pygame 종료

pygame.quit()