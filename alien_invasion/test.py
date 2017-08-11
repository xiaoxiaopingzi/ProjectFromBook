# -*- coding: UTF-8 -*-
"""外星人入侵的一些测试类"""
import pygame
import sys
try:
    from settings import Settings
except ImportError:
    raise ImportError('The file is not found. Please check the file name!')

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # 检测按下键盘事件
                print("事件为:%s，类型为：%s" % (event.key, type(event.key)))  # pygame中

        screen.fill(ai_settings.bg_color)
        pygame.display.flip()
run_game()

