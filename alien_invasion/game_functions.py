# -*- coding: UTF-8 -*-
"""  """
import sys
import pygame
import time
try:
    from ship import Ship
    from bullet import Bullet
    from alien import Alien
except ImportError:
    raise ImportError('The file is not found. Please check the file name!')

def check_events(ai_settings, stats, screen, ship, aliens, bullets, play_button, sb):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # 检测按下键盘事件
            check_keydown_events(event, ai_settings, aliens, bullets, screen, ship, stats, sb)
        elif event.type == pygame.KEYUP:   # 检测松开键盘事件
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # pygame.mouse.get_pos() ，它返回一个元组，其中包含玩家单击时鼠标的x和y坐标
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, stats, screen, ship, aliens, bullets, play_button, mouse_x, mouse_y, sb)

def check_play_button(ai_settings, stats, screen, ship, aliens, bullets, play_button, mouse_x, mouse_y, sb):
    """在玩家单击play按钮时开始游戏"""
    # 使用collidepoint函数来检查鼠标单击的位置是否在Play按钮的rect内
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    # 只有游戏在非活动状态并且点击了Play按钮才会重新开始游戏游戏
    if button_clicked and not stats.game_active:
        start_game(ai_settings, aliens, bullets, screen, ship, stats, sb)


def start_game(ai_settings, aliens, bullets, screen, ship, stats, sb):
    # 重置游戏中关于速度的设置
    ai_settings.initialize_dynamic_settings()

    # 隐藏光标
    # 通过向set_visible()传递False ，让Pygame在光标位于游戏窗口内时将其隐藏起来
    pygame.mouse.set_visible(False)

    # 重置游戏统计信息
    stats.reset_stats()
    stats.game_active = True

    # 重置记分牌图像
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()

    # 清空外星人列表和子弹列表
    aliens.empty()
    bullets.empty()

    # 创建一群新的外星人, 将飞船放到屏幕底部中央
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()


# 键盘中的每个事件的event.key都是一个int类型的整数
def check_keydown_events(event, ai_settings, aliens, bullets, screen, ship, stats, sb):
    # 右移事件
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:  # 判断键盘按下是否是右箭头
        ship.moving_right = True
    # 使用else if来保证按下键盘的事件只与一个键相关联
    # 如果同时按下左右箭头，将检测到两个不同的事件，飞船将纹丝不动，
    # 这是因为这两个事件使得moving_right和moving_left同时为True，于是在update()方法中飞船的位置就会不变
    # 左移事件
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        ship.moving_upper = True
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:  # 按空格键连续发射子弹
        ship.fire_bullet = True
    elif event.key == pygame.K_q:    # 按q退出游戏
        sys.exit()
    elif event.key == pygame.K_p:    # 按p重新开始游戏
        start_game(ai_settings, aliens, bullets, screen, ship, stats, sb)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = False
    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        ship.moving_upper = False
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        ship.moving_down = False
    elif event.key == pygame.K_SPACE:
        ship.fire_bullet = False

def update_bullets(ai_settings, screen, ship, bullets, aliens, sb, stats):
    bullets.update()  # 子弹位置更新
    # 删除已消失的子弹
    # 在for 循环中，不应从列表或编组中删除条目，因此必须遍历编组的副本
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print("还剩%s颗子弹" % len(bullets))
    check_bullet_alien_collisions(ai_settings, aliens, bullets, screen, ship, sb, stats)

# 检查子弹和外星人是否有碰撞
def check_bullet_alien_collisions(ai_settings, aliens, bullets, screen, ship, sb, stats):
    """响应子弹和外星人的碰撞"""
    # 检查是否有子弹击中了外星人,如果是这样，就删除相应的子弹和外星人
    # 两个boolean类型的参数表示了发生碰撞后是否将对应的精灵删除
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    # collisions中的每一个value对应的就是一颗子弹撞到的外星人，所以需要遍历
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    # 检查编组aliens是否为空，如果为空就表示当前所有的外星人已经消灭，就重新创造一群外星人
    if len(aliens) == 0:
        # 如果整群的外星人都被消灭，玩家就提高一个等级
        bullets.empty()  # 清空子弹编组
        ai_settings.increase_speed()  # 加快游戏节奏

        # 提高等级
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)  # 创建一群新的外星人

# 检查是否诞生了最高得分
def check_high_score(stats, sb):
    """检查是否诞生了新的最高得分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


# 如果ship.fire_bullet为True并且到了发射间隔，就将一颗子弹添加到编组bullets
def fire_bullet(ai_settings, bullets, screen, ship):
    if ship.fire_bullet:
        if ai_settings.bullet_fire_interval > ai_settings.bullet_fire_constant - 1:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
    update_fire_interval(ai_settings)

# 更新发射间隔
def update_fire_interval(ai_settings):
    if ai_settings.bullet_fire_interval == 0:
        ai_settings.bullet_fire_interval += ai_settings.bullet_fire_constant
    else:
        ai_settings.bullet_fire_interval -= 1


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算一行可以容纳多少个外星人
    # 外星人间距为外星人的宽度
    alien = Alien(ai_settings, screen)  # 这个外星人不是外星人群的成员，因此没有将它加入到编组 aliens 中
    # 外星人的 rect 属性中获取外星人宽度，并将这个值存储到 alien_width 中，以免反复访问属性 rect
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # 创建外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)  # 创建一个外星人
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_number  # 用alien.x存储小数值
    alien.rect.x = alien.x  # 用 alien.x 更新 alien.rect.x
    alien.rect.y = alien_height + 2 * alien_height * row_number
    aliens.add(alien)  # 将创建的外星人加入到编组中


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可以容纳多少行外星人"""
    available_space_y = ai_settings.screen_height - ship_height - (3 * alien_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def get_number_aliens_x(ai_settings, alien_width):
    """计算屏幕每行可容纳的外星人数量"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    # 使用了 int() 来确保计算得到的外星人数量为整数
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def check_fleet_edges(ai_settings, aliens):
    """有外星人达到屏幕边缘时采取相应的措施"""
    for alien in aliens.sprites():
        # 只要有一个外星人到达屏幕边缘所有外星人就下移并改变方向
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移，并改变它们的方向"""
    # 将所有的外星人下移
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    # 改变所有外星人的方向
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, ship, aliens, stats, screen, bullets, sb):
    """检查是否有外星人到达屏幕边缘，然后更新外星人群中所有外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    # 对编组aliens调用方法update() ，这将自动对每个外星人调用方法update()
    aliens.update()
    # 方法spritecollideany()遍历编组aliens，并返回它找到的第一个与飞船发生了碰撞的外星人
    # 如果没有发生碰撞，spritecollideany()会返回None，如果找到了与飞船发生碰撞的外星人，就返回这个外星人
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)
    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb)

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:  # 检测玩家是否还剩下飞船
        # 将ships_left减1
        stats.ships_left -= 1

        # 更新记分牌
        sb.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()  # 将飞船放到屏幕中央

        # 暂停0.5秒，屏幕将暂时停止变化，让玩家能够看到外星人撞到了飞船
        time.sleep(0.5)
    else:
        # 玩家的飞船用光，将游戏的活动标志设为False并显示光标
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb):
    """检查外星人是否到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样处理
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)
            break


def update_screen(ai_settings, stats, screen, ship, bullets, aliens, play_button, sb):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    aliens.draw(screen)

    # 在飞船和外星人后面重绘所有子弹
    # bullets.sprites() 返回一个列表，其中包含编组 bullets 中的所有精灵
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 显示得分
    sb.show_score()

    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见，在每次执行while循环时都绘制一个空屏幕，并擦去旧屏幕
    pygame.display.flip()