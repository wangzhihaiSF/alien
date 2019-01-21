import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """一个队飞创发射的子弹进行管理的类"""
    def __init__(self, ai_settings, screen, ship):
        """在飞船所处的位置创建一个子弹对象"""
        super(Bullet, super).__init__()
        self.screen = screen

        # 在（0,0）处创建一个表示子弹的矩形，在设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储小数表示子弹位置
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color