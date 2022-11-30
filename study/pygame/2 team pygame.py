
from tkinter import W
import pygame
import sys
import random
from time import sleep
padWidth = 750 #화면 가로 크기
padHeight = 772 #게임화면의 세로크기
rockImage = ["./picture/zombie1.png",
"./picture/zombie2.png",
"./picture/zombie3.png",
"./picture/zombie4.png",
"./picture/zombie5.png"]
explosinsound = ["./picture/zombiesound1.wav",
"./picture/zombiesound1.wav",
"./picture/zombiesound2.",
"./picture/zombiesound3.wav"]

#아이콘 변경
pygame.display.set_caption("zombie Invaders")
icon = pygame.image.load("./picture/zombie_icon.png")
pygame.display.set_icon(icon)


#게임에 등장하는 객체를 드로잉
def drawObject(obj,x,y):
    global gamePad
    gamePad.blit(obj,(x,y))
    
def initGame():
    global gamePad, clock,background,fighter,missile,explosion,stage,mas,missileSound,gameOverSound
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth,padHeight))
    pygame.display.set_caption('zomb World') #게임 이름
    background = pygame.image.load("./picture/stage.png")#배경 그림
    fighter = pygame.image.load("./picture/fighter.png")#전투기 그림
    missile = pygame.image.load("./picture/bullet.png")#미사일
    explosion = pygame.image.load("./picture/blood.png")#폭발
    stage = pygame.image.load("./picture/city.png")
    mas =  pygame.image.load("./picture/start_screen.png") #게임 오버 화면
    #pygame.mixer.music.load("C:/Users/KOREAIT/Desktop/pygame/picture/backsound.wav")#배경음악
    #pygame.mixer.music.play(-1)
    #missileSound = pygame.mixer.Sound("C:/Users/KOREAIT/Desktop/pygame/picture/권총소리2.wav")
    #gameOverSound = pygame.mixer.Sound("C:/Users/KOREAIT/Desktop/pygame/picture/gameoversound.wav")
    clock = pygame.time.Clock()





#운석을 맞춘 개수 계산
def writeScore(count):
    global gamePad
    font = pygame.font.Font("./picture/NanumGothic.ttf",20)
    text = font.render('죽인 좀비 수 : '+str(count),True,(255,255,255))
    gamePad.blit(text,(10,0))
#운석이 화면 아래로 통과 한 개
def writePassed(count):
    global gamePad, useammcont
    font =pygame.font.Font("./picture/NanumGothic.ttf",20)
    text = font.render('남은 탄약 : '+str(useammcont),True,(255,0,0))
    gamePad.blit(text,(600,0))
#게임 메시지 출력
def writeMessage(text):
    global gamePad
    stop1 = True
    textfont = pygame.font.Font("./picture/NanumGothic.ttf",80)
    text = textfont.render(text,True,(255,0,0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2)
    gamePad.blit(text,textpos)
    pygame.display.update()
def writeMessage1(text):
    global gamePad
    stop1 = True
    textfont = pygame.font.Font("./picture/NanumGothic.ttf",30)
    text = textfont.render(text,True,(255,0,0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2)
    gamePad.blit(text,textpos)
    pygame.display.update()
    #pygame.mixer.music.stop()#배경음악 정지
    #gameOverSound.play(-1)
    #전투기가 운석과 충돌 했을 때 메시지 출력
def writeammocnt():
    global gamePad
    writeMessage1('탄약이 없습니다 r 키를 눌러 장전을 하십시오')
    sleep(1)
 
def crash():
    global gamePad
    writeMessage('Player Die!')
    #게임 오버 메시지 보이기
    sleep(2)
    runGame()
def gameOver():
    global gamePad
    writeMessage('Game Over!')
    sleep(2)
    runGame()
global stop1
stop1 = False  
  
# 생성자 초기화
pygame.init() 
  
# 화면 해상
res = (720,720) 
  
# 창을 연다
screen = pygame.display.set_mode(res) 
  
# 흰색
color = (255,255,255) 
  
# 마우스 올리면 생기는 기늘
color_light = (170,170,170) 
  
# 어두은 그늘 
color_dark = (100,100,100) 
  
#너비 저장 화면 변수 
width = screen.get_width() 
  


# 높이를 저장
# 화면을 변수로
height = screen.get_height() 
  
# 글꼴 정의
smallfont = pygame.font.SysFont('Corbel',35) 
smallfont1 = pygame.font.SysFont('Corbel',35) 
#이 글로 렌더링
text = smallfont1.render('start' , True , color) 
text1 = smallfont.render('quit' , True , color) 
  
while True: 
      
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
              
        #마우스 클릭 확인
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #마우스를 클릭 하면 게임 시작
             
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:


                def runGame():
                    global gamePad,clock,background,fighter,missile,explosion,stop1,mas,useammcont,ammocnt
                    escbutton = 0
                
                    count1 = 2
                    ammocnt = 7
                    useammcont = 7
                    

                    #무기 좌표 리스트
                    missileXY = []
                    #운석 랜덤 생성
                    rock = pygame.image.load(random.choice(rockImage))
                    rockSize = rock.get_rect().size #운석크기
                    rockWidth = rockSize[0]
                    rockHeight = rockSize[1]
                    #destroySound = pygame.mixer.Sound(random.choice(explosinsound))
                    #운석 초기 위치 설정
                    rockX = random.randrange(0,padWidth - rockWidth)
                    rockY = 0
                    rockSpeed = 2
                    fighterSpeed = 5
                    # 전투기 크기
                    fighterSize = fighter.get_rect().size
                    fighterWidth = fighterSize[0]
                    fighterHeight = fighterSize[1]
                    #전투기 초기 위치 (x,y)
                    x = padWidth * 0.45
                    y = padHeight * 0.9
                    fighterX = 0
                    #전투기가 운석과 충돌했는지 체크
                    #전투기 미사일에 운석이 맞았을 경우 True
                    isShot = False
                    shotCount = 0
                    rockPassed =0
                    onGame = False
                    while not onGame:
                        for event in pygame.event.get():
                            if event.type in [pygame.QUIT]: #게임 프로그램 종료
                                pygame.quit()
                                sys.exit()

                            if event.type in [pygame.KEYDOWN]:
                                if event.key == pygame.K_LEFT: #전투기 왼쪽으로 이동
                                    fighterX -= fighterSpeed
                                elif event.key == pygame.K_RIGHT: #전투기 오른쪽으로 이동
                                    fighterX += fighterSpeed
                                elif event.key == pygame.K_SPACE: #미사일 발사
                                    if escbutton != 1 :
                                        #  missileSound.play() #미사일 사운드 재생
                                        if useammcont > 0 :
                                            missileX = x + fighterWidth/2
                                            missileY = y - fighterHeight
                                            missileXY.append([missileX,missileY])
                                            useammcont -= 1
                                        else :
                                            writeammocnt()
                            if event.type in [pygame.KEYUP]: #방향키를 때면 전투기 멈춤
                                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                                    fighterX = 0
                            if event.type in [pygame.KEYDOWN]:
                                if event.key == pygame.K_d: #필살기
                                
                                    if count1 != 0 and rockSpeed >= 4 :
                                        rockSpeed -= 3
                                        count1 -= 1
                                elif event.key == pygame.K_r: #총알 장전
                                    pygame.time.delay(1000) 
                                    useammcont = 7
                            if event.type in [pygame.KEYDOWN]:
                                if event.key == pygame.K_ESCAPE:
                                    escbutton += 1
                                    if escbutton %2 == 0:
                                        escbutton = 0
                                        rockSpeed = stoprock
                                        fighterSpeed = stopfighter
                                        print(escbutton)
                                    if escbutton %2 != 0:
                                        stoprock = rockSpeed
                                        stopfighter = fighterSpeed
                                        rockSpeed = 0
                                        fighterSpeed = 0
                                        print(escbutton)

                        
                            


                        drawObject(background,0,0)#배경 화면 그리기
                        #전투기 위치 재조정
                        x += fighterX
                        if x < 0:
                            x = 0
                        elif x > padWidth - fighterWidth:
                            x = padWidth - fighterWidth
                        #전투기가 운석과 충돌했는지 체크
                        if y < rockY + rockHeight:
                            if(rockX > x and rockX < x + fighterWidth) or (rockX + rockWidth > x and rockX + rockWidth < x + fighterWidth):
                                crash()
                        drawObject(fighter,x,y) #비행기를 게임화면의 (x,y) 좌표에 그림
                        #미사일 발사 화면에 그리기
                        if len(missileXY) != 0:
                            for i,bxy in enumerate(missileXY): #미사일 요소에 대해 반복함
                                bxy[1] -= 18 #총알의 y 좌표 - 10(위로 이동)
                                missileXY[i][1] = bxy[1]
                                #미사일이 운석을 맞추었을 경우
                                if bxy[1] < rockY:
                                    if bxy[0] > rockX and bxy[0] < rockX + rockWidth:
                                        missileXY.remove(bxy)
                                        isShot = True
                                        shotCount += 1
                                if bxy[1] <= 0: #미사일이 화면 밖을 벗어나면
                                    try:
                                        missileXY.remove(bxy) #미사일 제거
                                    except:
                                        pass
                        if len(missileXY) != 0:
                            for bx,by in missileXY:
                                drawObject(missile,bx,by)
                        #운석 맞춘 점수 표시
                        writeScore(shotCount)
                        rockY += rockSpeed #운석 아래로 움직임
                        #좀비가 떨어지는 경우
                        if rockY > padHeight:
                            #새로운 좀비 (랜덤)
                            rock = pygame.image.load(random.choice(rockImage))
                            rockSize = rock.get_rect().size
                            rockWidth = rockSize[0]
                            rockHeight = rockSize[1]
                            rockX = random.randrange(0,padWidth - rockWidth)
                            rockY = 0
                            rockPassed +=1
                        if rockPassed == 1: #좀비 3개 놓치면 게임오버
                            gameOver()
                        #놓친 좀비
                        writePassed(rockPassed)
                        #운석을 맞춘 경우
                        if isShot:
                            #운석 폭발
                            drawObject(explosion,rockX,rockY) #운석 폭발 그리기
                            # destroySound.play()#운석 폭발 사운드
                            #새로운 운석(랜덤) 
                            rock = pygame.image.load(random.choice(rockImage))
                            rockSize = rock.get_rect().size
                            rockWidth = rockSize[0]
                            rockHeight = rockSize[1]
                            rockX = random.randrange(0,padWidth - rockWidth)
                            rockY = 0
                            # destroySound = pygame.mixer.Sound(random.choice(explosinsound))
                            isShot = False
                            #좀비 맞추면 속도 증가
                            rockSpeed += 0.1
                            fighterSpeed += 0.05
                            if rockSpeed >= 15:
                                rockSpeed = 15
                            if fighterSpeed >= 10:
                                fighterSpeed = 10
                        drawObject(rock,rockX,rockY) #운석 그리기




                        
                        

                        pygame.display.update() #게임화면을 다시그림
                        clock.tick(60) #게임화면의 초당 프레임수를 60으로 설정
                    pygame.quit() #pygame 종료
                initGame()
                runGame()
            if width/2 <= mouse[0] <= width/10+140 and height/2 <= mouse[1] <= height/10+40:
                pygame.quit()
    # 화면을 색상으로 채운다
    screen.fill((60,25,60)) 
      
    # (x,y) 좌표를 다음 위치에 저장합니다.
    # 튜플로서의 변수
    mouse = pygame.mouse.get_pos() 
  
    # 버튼 위에 마우스를 올려놓으면
    # 밝은 그늘로 변경
    if width/2 <= mouse[0] <= width/2+70 and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(screen,color_light,[width/2,height/2,140,40]) 
          
    else: 
        pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40]) 
      
    if width/2 <= mouse[0] <= width/10+140 and height/2 <= mouse[1] <= height/10+40: 
        pygame.draw.rect(screen,color_light,[width/10,height/2,140,40]) 
          
    else: 
        pygame.draw.rect(screen,color_dark,[width/10,height/2,140,40])
     
           
    # # 버튼에 텍스트를 겹쳐 놓기
    screen.blit(text1 , (width/10+50,height/2)) 
    screen.blit(text , (width/2+50,height/2)) 
      
    #   게임의 프레임을 업데이트합니다.
    pygame.display.update() 