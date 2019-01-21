class Settings():
    """
    存储所有设置
    """
    def __init__(self):
        # 初始化设置
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # 飞船速度设置
        self.ship_speed_factor = 1.5