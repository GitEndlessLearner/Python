

class Settings():
	"""存储外星人所有的设置类"""

	def __init__(self):
		"""初始化游戏的设置"""
		# 屏幕设置
		self.screen_width = 1200
		self.screen_height = 600
		self.bg_color = (255, 255, 255)

		# 子弹设置
		self.bullet_speed_factor = 0.3
		self.bullet_width = 1400
		self.bullet_height = 15
		self.bullet_color = 0, 0, 0
		self.bullet_allowed = 3

		# 外星人设置
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		# fleet_direction为1 表示向右移， 为-1表示向左移
		self.fleet_direction = 1

		# 飞船设置
		self.ship_speed_factor = 2
		self.ship_limit = 3