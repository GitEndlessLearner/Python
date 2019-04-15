import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""对飞船发射的子弹进行管理的类"""

	def __init__(self, ai_sittings, screen, ship):
		"""在飞船所处位置创造一个子弹"""
		super(Bullet, self).__init__()
		self.screen = screen

		# 在（0,0）处创建一个表示子弹的矩形，再设置正确的位置
		self