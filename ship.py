import pygame
class Ship():
    def __init__(self, screen):
        # 初始化飞船及其位置
        self.screen = screen
        # 加载飞船的图像并获取其外接矩形
        # load 返回一个飞船的surface
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每个新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blit_me(self):
        # 指定位置绘制飞船
        self.screen.blit(self.image, self.rect)

