# Quiz) 하늘에서 떨어지는 똥피하기 게임

# [게임 조건]
# 1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
# 2. 똥은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정
# 3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
# 4. 캐릭터가 똥과 충돌하면 게임 종료
# 5. FPS는 30으로 고정

# [게임 이미지]
# 1. 배경 : 640 * 480 - background.png
# 2. 캐릭터 : 70 * 70 - character.png
# 3. 똥 : 70 * 70 - enemy.png


import pygame

###################################################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init() # 초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 크기 설정

# 화면 타이틀 설정
pygame.display.set_caption("똥 피하기")

# FPS 설정
clock = pygame.time.Clock()
###################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
background = pygame.image.load('./background.png')

character = pygame.image.load('./character.png')
character_width = 70
character_height = 70
character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height - character_height

enemy = pygame.image.load('./enemy.png')
enemy_width = 70
enemy_height = 70
enemy_x_pos = 0
enemy_y_pos = 0

to_x = 0.6
to_y = 0
speed = 0.6

#이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(30)     # 게임화면의 초당 프레임 수 설정
    
    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():    
        if event.type == pygame.QUIT :  
            running = False

        # 캐릭터 좌우 이동
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x = -(to_x)
            if event.key == pygame.K_RIGHT:
                to_x = -(to_x)

        # if event.type == pygame.KEYUP:
        #     to_x = 0
        print(event, to_x)
    character_x_pos += to_x*dt
    # 3. 게임 캐릭터 위치 정의
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update()
    
pygame.quit()