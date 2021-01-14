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

# 캐릭터 불러오기
character = pygame.image.load("./character.png")
character_size = character.get_rect().size  # 이미지의 크기를 구해옴
character_width = character_size[0]         # 캐릭터의 너비
character_height = character_size[1]        # 캐릭터의 높이
character_x_pos = screen_width / 2  -character_width / 2    # 화면 가로의 절반 크기에 해당하는 곳에 위치    (가로위치)
character_y_pos = screen_height - character_height          # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로위치)

# 이동할 좌표
to_x = 0
to_y = 0

#이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get():    # 필수 부분 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT :  # 창 닫기 버튼 눌렀을 때
            running = False

        if event.type == pygame.KEYDOWN:    # 키가 눌러 졌는지 확인
            if event.key == pygame.K_LEFT:      # 캐릭터를 왼쪽으로
                to_x -= 0.5 # 5위치만큼 왼쪽으로
            elif event.key == pygame.K_RIGHT:   # 캐릭터를 오른쪽으로
                to_x += 0.5 # 5위치만큼 오른쪽으로
            elif event.key == pygame.K_UP:      # 캐릭터를 위로
                to_y -= 0.5 # 5위치만큼 위쪽으로
            elif event.key == pygame.K_DOWN:    # 캐릭터를 아래로
                to_y += 0.5 # 5위치만큼 아래쪽으로

        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    # 가로 경계 값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0,0))      # 배경 그리기
    
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기

    pygame.display.update()             # 게임 화면 다시 그리기! 반복 호출

# 게임 종료 시 
# pygame 종료

pygame.quit()