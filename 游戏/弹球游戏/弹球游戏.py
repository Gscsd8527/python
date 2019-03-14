import pygame
from pygame import *
import time

class small:
    def __init__(self,tep_screen):
        self.x=210
        self.y=400
        self.screen=tep_screen
        self.imger=pygame.image.load('./image/heng.png')
    def move_life(self):
        self.x-=10
    def move_right(self):
        self.x+=10
    def display(self):
        self.screen.blit(self.imger, (self.x, self.y))

# 将键盘获取到的值封装成一个函数
def key_control(temp_mysmall):
    for event in pygame.event.get():
        if event.type == QUIT:
            print('exit')
            exit()
        elif event.type==K_a or event.type==K_LEFT:
            print('left')
            temp_mysmall.move_life()
        elif event.type==K_d or event.type==K_RIGHT:
            print('right')
            temp_mysmall.move_right()
def main():
    # 1.创建窗口大小
    screen=pygame.display.set_mode((500,600),0,32)
    # 2.创建背景
    background=pygame.image.load('./image/bj1.png')
    mysmall=small(screen)
    while True:
        screen.blit(background,(0,0))
        mysmall.display()
        key_control(mysmall)
        time.sleep(0.01)
if __name__=='__main__':
    main()
