

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
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 0, 0, 0
		self.bullet_allowed = 3

