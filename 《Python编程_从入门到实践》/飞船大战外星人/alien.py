import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""表示单个外星人的类"""

	def __init__(self, ai_settings, screen):
		"""初始化外星人"""
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		# 加载外星人图像，并设置rect属性
		self.image = pygame.image.load('images/alien.jpg')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# 外星人初始位置
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# 存储外星人的准确位置
		self.x = float(self.rect.x)

	def  blitme(self):
		"""在制定位置绘制外星人"""
		self.screen.blit(self.image, self.rect)
