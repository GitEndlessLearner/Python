import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""对飞船发射的子弹进行管理的类"""

	def __init__(self, ai_sittings, screen, ship):
		"""在飞船所处位置创造一个子弹"""
		super(Bullet, self).__init__()
		self.screen = screen

		# 加载飞船图像并获取外接矩形
		self.image = pygame.image.load('images/ball.jpg')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		# 存储用小数表示的子弹位置
		self.y = float(self.rect.y)



		self.speed_factor = ai_sittings.bullet_speed_factor

	def update(self):
		"""向上移动子弹"""
		# 更新表示子弹位置的小数值
		self.y -= self.speed_factor
		# 更新表示子弹的react的位置
		self.rect.y = self.y

	def draw_bullet(self):
		"""在屏幕上绘制子弹"""
		self.screen.blit(self.image, self.rect)