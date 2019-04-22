import pygame

class Ship():

	def __init__(self, ai_settings, screen):
		"""初始化飞船并设置其初始位置"""
		self.screen = screen
		self.ai_settings = ai_settings

		# 加载飞船图像并获取外接矩形
		self.image = pygame.image.load('images/cxk.jpg')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# 初始位置在屏幕中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# 在飞船的属性center中存储小数点
		self.center = float(self.rect.centerx)

		# 移动标志
		self.moving_right = False
		self.moving_left = False

		# 飞船的设置
		self.ship_speed_factor = 2

	def update(self):
		"""根据移动标志调整飞船的位置"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ship_speed_factor

		# 更新self.center至rect对象
		self.rect.centerx = self.center

	def blitme(self):
		"""在指定的地方绘制飞船"""
		self.screen.blit(self.image, self.rect)
