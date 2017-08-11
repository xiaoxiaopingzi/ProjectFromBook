# -*- coding: UTF-8 -*-
"""根据Python编程：从入门到实践的外星人入侵写的项目"""
import pygame
from pygame.sprite import Group
try:
    import game_functions as gf
    from settings import Settings
    from ship import Ship
    from game_stats import GameStats
    from button import Button
    from scoreboard import Scoreboard
except ImportError:
    raise ImportError('The file is not found. Please check the file name!')

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    # 创建一个1200 X 800 像素的窗口
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")  # 设置窗口的标题

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建得分牌
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建一个空编组，用于存储外星人群
    aliens = Group()

    # 创造外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, stats, screen, ship, aliens, bullets, play_button, sb)  # 事件检查(检查玩家输入)
        if stats.game_active:
            ship.update()     # 飞船位置更新
            gf.fire_bullet(ai_settings, bullets, screen, ship)   # 发射子弹
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens, sb, stats)  # 子弹位置更新
            gf.update_aliens(ai_settings, ship, aliens, stats, screen, bullets, sb)  # 外星人位置更新
        gf.update_screen(ai_settings, stats, screen, ship, bullets, aliens, play_button, sb)  # 游戏窗口更新

run_game()