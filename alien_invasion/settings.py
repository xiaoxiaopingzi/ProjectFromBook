# -*- coding: UTF-8 -*-
"""存储<<外星人入侵>>的所有设置的类"""
class Settings(object):
    def __init__(self):
        """ 初始化游戏的设置 """
        # 屏幕设置
        self.screen_width = 840
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 飞船每次移动距离大小的设置和玩家可用的飞船数量设置
        self.ship_limit = 3

        # 外星人设置
        self.fleet_drop_speed = 10  # 外星人下落的速度

        # 子弹设置
        # 创建宽3像素、高15像素的深灰色子弹。子弹的速度比飞船稍低
        self.bullet_width = 3
        self.bullet_height = 8
        self.bullet_color = (60, 60, 60)
        self.bullet_fire_constant = 20  # 每过20次循环就发射一颗子弹
        self.bullet_fire_interval = self.bullet_fire_constant  # 用于统计循环的次数

        # play按钮设置
        self.button_width = 200
        self.button_height = 50
        self.button_color = (0, 255, 0)
        self.button_text_color = (255, 255, 255)

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1

        # 外星人点数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    # 在游戏过程中，不断增大难度
    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 1

        # fleet_direction表示外星人移动的方向，1表示右移(x坐标要增大)，-1表示左移(x坐标要减少)
        self.fleet_direction = 1

        # 计分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
