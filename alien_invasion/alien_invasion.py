# import sys  只在gf中使用，重构之后先注释掉
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group



def run_game():
        #初始化，并创建一个屏幕对象
        pygame.init()
        # screen = pygame.display.set_mode((1200,800))
        # pygame.display.set_caption("Alien Invasion")
        ai_settings = Settings()
        screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
        
        #创建一艘飞船
        ship = Ship(ai_settings, screen)

        #创建一个用于存储子弹的编组
        bullets = Group()


        #设置背景色
        bg_color = (230, 230, 230)
        #开始游戏的主循环
        while True:
                #监视键盘和鼠标事件
                # for event in pygame.event.get():
                #         if event.type == pygame.QUIT:
                #                 sys.exit()
                gf.check_events(ai_settings, screen, ship, bullets)

                ship.update()
                gf.update_bullet(bullets)

                #每次循环都重新绘制屏幕
                # # screen.fill(bg_color)
                # screen.fill(ai_settings.bg_color)
                # ship.blitme()

                # #让最近绘制的屏幕可见
                # pygame.display.flip()
                gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
