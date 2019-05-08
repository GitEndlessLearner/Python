

class Settings():
	"""存储外星人所有的设置类"""

	def __init__(self):
		"""初始化游戏的静态设置"""
		# 屏幕设置
		self.screen_width = 1200
		self.screen_height = 600
		self.bg_color = (255, 255, 255)

		# 飞船设置
		self.ship_limit = 3

		# 子弹设置
		self.bullet_width = 1400
		self.bullet_height = 15
		self.bullet_color = 0, 0, 0
		self.bullet_allowed = 3

		# 外星人设置
		self.fleet_drop_speed = 10

		# 加快游戏节奏的速度
		self.speedup_scale = 1.1

		# 外星人点数提高
		self.score_scale = 1.50

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		self.ship_speed_factor = 2
		self.bullet_speed_factor = 0.3
		self.alien_speed_factor = 1
		self.alien_points = 50
		# fleet_direction为1 表示向右移， 为-1表示向左移
		self.fleet_direction = 1

	def increase_speed(self):
		"""提高游戏设置"""
		self.ship_speed_factor += self.speedup_scale
		self.bullet_speed_factor += self.speedup_scale
		self.alien_speed_factor += self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)
		print(self.alien_points)