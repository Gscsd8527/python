# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import time
import pygame
class HeroPlane(object):
    def __init__(self,screen_temp):
        self.x=210
        self.y=550
        self.screen=screen_temp
        self.image = pygame.image.load('./imger/hero.png')
        # 存储发射出去的子弹对象引用
        self.bullet_list=[]
    def display(self):
        self.screen.blit(self.image,(self.x, self.y))

        for bullt in self.bullet_list:
            bullt.dispaly()
            bullt.move()
    def move_left(self):
        self.x-=10
    def move_right(self):
        self.x+=10
    # 开火 发射子弹
    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))
# 将子弹封装成一个类
class Bullet(object):
    def __init__(self,screen_temp,x,y):
        self.x= x+40
        self.y= y-20
        self.screen=screen_temp
        self.image = pygame.image.load('./imger/bullet.png')
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    def move(self):
        self.y-=20
# 将获取键盘封装成一个方法
def key_control(hero_temp):
    # 获取事件，比如按键等
    for event in pygame.event.get():
        # 判断是否是点击了退出按钮
        if event.type == QUIT:
            print('exit')
            exit()
            # 判断是否是按下了键
        elif event.type == KEYDOWN:
            # 检测按键是否为a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                # x-=10
                hero_temp.move_left()
                # 检测按键是否是d或者right
                # 把他封装为方法
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                # x+=10
                hero_temp.move_right()
            # 检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                hero_temp.fire()
def main():
    # 1.创建窗口
    screen=pygame.display.set_mode((500,660),0,32)

    # 2.创建一个图片背景
    background=pygame.image.load('./imger/bj.png')

    # 创建一个飞机图片,
    # 控制飞机的坐标
    # x=210
    # y=550
    #3. 创建一个飞机对象
    hero=HeroPlane(screen)
    while True:
        screen.blit(background,(0,0))
        # 这里是飞机的坐标，将它封装到类方法中
        # screen.blit(hero,(x, y))
        hero.display()
        pygame.display.update()
        key_control(hero)
        # 让程序延时
        time.sleep(0.01)
if __name__=='__main__':
    main()