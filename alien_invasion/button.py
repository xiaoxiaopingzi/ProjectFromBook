# -*- coding: UTF-8 -*-
import pygame.font

"""play按钮"""
class Button(object):
    def __init__(self, ai_settings, screen, msg):
        """初始化按钮的属性"""
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮的尺寸和其他属性
        self.width = self.ai_settings.button_width
        self.height = self.ai_settings.button_height
        self.button_color = self.ai_settings.button_color
        self.text_color = self.ai_settings.button_text_color
        # 指定使用默认字体(None表示默认字体)来渲染文本，文本的字号为48
        self.font = pygame.font.SysFont(None, 48)

        # 创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 按钮内的文本只需要创建一次,msg是要在按钮中显示的文本
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """绘制一个用颜色填充的按钮，再绘制文本"""
        # 调用screen.fill()来绘制表示按钮的矩形
        self.screen.fill(self.button_color, self.rect)
        # 调用screen.blit()，向他传递一幅图像以及与该图像相关联的rect对象
        self.screen.blit(self.msg_image, self.msg_image_rect)