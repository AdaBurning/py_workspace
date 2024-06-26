import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
        """表示单个外星人的类"""
        def __init__(self, ai_settings, screen):
                """初始化外星人的设置及其起始位置"""
                super().__init__()
                self.screen = screen
                self.ai_settings = ai_settings

                #加载外星人的图像，并设置其rect
                self.image = pygame.image.load('images/plane.bmp')
                self.rect = self.image.get_rect()
                
                #每个外星人最初都在屏幕左上角附近
                self.rect.x = self.rect.width
                self.rect.y = self.rect.height

                #存储外星人的准确位置
                self.x = float(self.rect.x)
        
        def blitme(self):
                """在指定位置绘制"""
                self.screen.blit(self.image, self.rect)
