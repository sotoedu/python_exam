import random
from random import randrange

import pygame
import sys
from time import sleep

padWidth = 800
padHeight = 600

def initGame():
    global gamePad, player, clock
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('Test')

    # 이미지 로딩
    player = pygame.image.load('img/player.png')  #64x64 크기의 이미지
    clock = pygame.time.Clock()

def runGame():
    global player, clock

    isrun = False
    targetPoint = [0,0]
    currentPoint = [400, 300]
    while True:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

        if isrun == False:#움직임이 끝나면
            targetPoint[0] = randrange(0, padWidth - 64)
            targetPoint[1] = randrange(0, padHeight - 64)#목표 위치 만들기
            isrun = True
        else:
            if targetPoint[0] - currentPoint[0] > 0:#목표 위치로 이동
                currentPoint[0] += 1
            elif targetPoint[0] - currentPoint[0] < 0:
                currentPoint[0] -= 1

            if targetPoint[1] - currentPoint[1] > 0:#목표 위치로 이동
                currentPoint[1] += 1
            elif targetPoint[1] - currentPoint[1] < 0:
                currentPoint[1] -= 1

            if targetPoint[0] - currentPoint[0] == 0 and targetPoint[1] - currentPoint[1] == 0:
                isrun = False#목표 위치로 도착했다면

        gamePad.fill((0,0,0))
        gamePad.blit(player, (currentPoint[0], currentPoint[1]))  # 이미지 화면에 출력
        pygame.display.update()
        clock.tick(60)


# 게임 실행
initGame()
runGame()

