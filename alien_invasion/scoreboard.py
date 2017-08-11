# -*- coding: UTF-8 -*-
"""显示分数信息"""
import pygame.font
from pygame.sprite import Group
try:
    from ship import Ship
except ImportError:
    raise ImportError('The file is not found. Please check the file name!')

class Scoreboard(object):
    """显示分数信息的类"""
    def __init__(self,  ai_settings, screen, stats):
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.ai_settings = ai_settings

        # 显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 36)

        # 准备初始得分图像
        self.prep_score()

        # 最高得分
        self.prep_high_score()

        # 玩家等级
        self.prep_level()

        # 创建一个飞船编组
        self.prep_ships()

    def prep_score(self):
        """将得分转化为一幅渲染的图像"""
        rounded_score = round(self.stats.score, -1)
        score_str = "Score:{:,}".format(rounded_score)  # 数字值 stats.score 转换为字符串
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将得分放在最高分和等级之间
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx + 150
        self.score_rect.top = 10

    def prep_high_score(self):
        """将最高得分渲染为图像"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "High Score:{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将最高得分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx - 80
        self.high_score_rect.top = 10

    def prep_level(self):
        """将等级转化为图像"""
        level_str = "Level:" + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.ai_settings.bg_color)

        # 将等级放在屏幕的右上角
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 10
        self.level_rect.top = 10

    def prep_ships(self):
        """显示还余下多少艘飞船"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 1
            self.ships.add(ship)

    def show_score(self):
        """在屏幕上显示当前得分和最高得分"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # 绘制飞船
        self.ships.draw(self.screen)