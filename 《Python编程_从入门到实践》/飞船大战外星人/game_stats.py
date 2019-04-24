class GameStats():
	"""跟踪游戏的统计信息"""

	def __init__(self, ai_sittings):
		"""初始化统计信息"""
		self.ai_sittings = ai_sittings
		self.reset_stats()

		# 游戏刚启动时处于活动状态
		self.game_active = True

	def reset_stats(self):
		"""初始化运行期间可能变化的统计信息"""
		self.ships_left = self.ai_sittings.ship_limit