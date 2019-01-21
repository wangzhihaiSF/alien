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
        gf.update_screen(ai_settings, screen, ship)
        gf.check_events()

run_game()