import pygame

class Ship():
        def __init__(self, screen):
                #初始化设置和位置
                self.screen = screen

                #加载图像，并获取其外接矩形
                self.image = pygame.image.load('images/plane.bmp')
                self.rect = self.image.get_rect()
                self.screen_rect = screen.get_rect()

                #将每艘飞船放在屏幕底部中央
                self.rect.centerx = self.screen_rect.centerx
                self.rect.bottom = self.screen_rect.bottom

                #移动标志
                self.moving_right = False

        def update(self):
                if self.moving_right:
                        self.rect.centerx +=1
        
        def blitme(self):
                """在指定位置绘制飞创"""
                self.screen.blit(self.image, self.rect)
