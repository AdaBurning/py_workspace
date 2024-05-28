import pygame

class Ship():
        def __init__(self, ai_settings, screen):
                #初始化设置和位置
                self.screen = screen
                self.aisettings = ai_settings


                #加载图像，并获取其外接矩形
                self.image = pygame.image.load('images/plane.bmp')
                self.rect = self.image.get_rect()
                self.screen_rect = screen.get_rect()

                #将每艘飞船放在屏幕底部中央
                self.rect.centerx = self.screen_rect.centerx
                self.rect.bottom = self.screen_rect.bottom

                #在飞船的属性center中存储小数值
                self.center = float(self.rect.centerx)


                #移动标志
                self.moving_right = False
                self.moving_left = False

        def update(self):
                #更新飞船的cneter值。
                if self.moving_right and self.rect.right < self.screen_rect.right:
                        self.center += self.aisettings.ship_speed_factor
                if self.moving_left and self.rect.left > self.screen_rect.left:
                        self.center -= self.aisettings.ship_speed_factor

                self.rect.centerx = self.center
        def blitme(self):
                """在指定位置绘制飞创"""
                self.screen.blit(self.image, self.rect)
