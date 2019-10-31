import pygame
from pygame.locals import *
import sys, random

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("弹力球")

white = 255, 255, 255
myfont = pygame.font.SysFont('arial', 60)  # None表示为系统自带字体
myfont1 = pygame.font.SysFont('SimHei', 20)
textImage1 = myfont1.render("红色为加速能量绿色为减速能量", True, white)
textImage = myfont.render("PlasticBall", True, white)


class Energy(object):
    def __init__(self):
        self.radius = 10
        self.pos_x1, self.pos_y1 = random.randint(10, 590), random.randint(10, 490)
        self.width = 0
        self.color = 255, 0, 0

    def draw(self):
        pos = self.pos_x1, self.pos_y1
        pygame.draw.circle(screen, self.color, pos, self.radius, self.width)


class SlowDown(object):
    def __init__(self):
        self.radius = 10
        self.pos_x2, self.pos_y2 = random.randint(10, 590), random.randint(10, 490)
        self.width = 0
        self.color = 0, 255, 0

    def draw1(self):
        pos = self.pos_x2, self.pos_y2
        pygame.draw.circle(screen, self.color, pos, self.radius, self.width)


class Circle(object):
    # 设置Circle类属性
    def __init__(self):
        self.vel_x = 1
        self.vel_y = 1
        self.radius = 20
        self.pos_x, self.pos_y = random.randint(20, 580), random.randint(20, 480)
        self.width = 0  # 填充圆
        self.color = 0, 0, 0

    def circle_run(self):
        # 防止球体超出游戏界面框体
        if self.pos_x > 580 or self.pos_x < 20:
            self.vel_x = -self.vel_x

        if self.pos_y > 480 or self.pos_y < 20:
            self.vel_y = -self.vel_y
        self.pos_x += self.vel_x  # 通过判断球体碰到界面框体后vel_x（速度变量取反）加上位置变量pos_x从而实现球的位置的实时变化
        self.pos_y += self.vel_y
        if enr.pos_x1 - 10 <= self.pos_x <= enr.pos_x1 + 10 and enr.pos_y1 - 10 <= self.pos_y <= enr.pos_y1 + 10:
            self.vel_x = 2
            self.vel_y = 2
        if sd.pos_x2 - 10 <= self.pos_x <= sd.pos_x2 + 10 and sd.pos_y2 - 10 <= self.pos_y <= sd.pos_y2 + 10:
            self.vel_x = 1
            self.vel_y = 1
        pos = self.pos_x, self.pos_y
        pygame.draw.circle(screen, self.color, pos, self.radius,
                           self.width)  # 绘制圆形（传入需要在该Surface对象上绘制圆形的Surface对象，颜色，圆心坐标，半径，绘圆的线的宽度（0时圆内被填充））


# Circle实例
cir = Circle()
enr = Energy()
sd = SlowDown()

while True:  # 为了让窗口能长时间显示，将程序启动的位置放入循环之中
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:  # 通过键盘键来控制小球自由弹动的位置
            if event.key == K_LEFT:
                if cir.vel_x > 0:
                    cir.vel_x = -cir.vel_x
                elif cir.pos_x >= 30:
                    cir.pos_x -= 10
            elif event.key == K_RIGHT:
                if cir.vel_x < 0:
                    cir.vel_x = -cir.vel_x
                elif cir.pos_x <= 570:
                    cir.pos_x += 10
            elif event.key == K_UP:
                if cir.vel_y > 0:
                    cir.vel_y = -cir.vel_y
                elif cir.pos_y >= 30:
                    cir.pos_y -= 10
            elif event.key == K_DOWN:
                if cir.vel_y < 0:
                    cir.vel_y = -cir.vel_y
                elif cir.pos_y <= 570:
                    cir.pos_y += 10

    screen.fill((20, 20, 69))  # 背景颜色
    screen.blit(textImage, (200, 200))  # 使其显示出来
    screen.blit(textImage1, (160, 140))
    cir.circle_run()
    enr.draw()
    sd.draw1()
    # space = pygame.image.load("you.jpg").convert_alpha()
    pygame.display.update()  # 通过此函数让绘制的东西显示在屏幕上
