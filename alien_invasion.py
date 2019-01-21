import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    """
    初始化 pygame，设置和屏幕对象
    """
    pygame.init()
    ai_settings = Settings()
    # set_mode() 的参数数元组
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建一艘飞船
    ship = Ship(screen)

    # 开始游戏主循环
    while True:
        # 每次循环时都重新绘制屏幕
        screen.fill(ai_settings.bg_color)
        # 绘制飞船
        ship.blit_me()
        # 让最近绘制的屏幕可见
        pygame.display.flip()
        gf.check_events()



run_game()