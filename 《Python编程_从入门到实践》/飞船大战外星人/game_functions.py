import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""响应按键"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
	elif event.key == pygame.K_ESCAPE:
		sys.exit()

def check_keyup_events(event, ship):
	"""响应松开"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ai_settings, screen, stats, sb, ship, aliens,
		bullets, play_button):
	"""响应按键和鼠标事件"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings,screen, stats, sb, play_button,ship, aliens,
				bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens,
		bullets, mouse_x, mouse_y):
	"""单击play按钮时开始新游戏"""
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		# 重置游戏统计信息
		stats.reset_stats()
		stats.game_active = True
		pygame.mouse.set_visible(False)
		ai_settings.initialize_dynamic_settings()

		#重置记分牌图像
		sb.prep_score()
		sb.prep_high_score()
		sb.prep_level()
		sb.prep_ships()

		# 清空外星人列表和子弹列表
		aliens.empty()
		bullets.empty()

def update_screen(ai_settings, screen,stats, sb, ship, aliens, bullets, play_button):
	"""更新屏幕图像，并切换到新屏幕"""
	# 每次循环时重绘图像
	screen.fill(ai_settings.bg_color)
	# 重绘所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)

	# 显示得分
	sb.show_score()

	# 如果游戏处于非活动状态，就绘制Play按钮
	if not stats.game_active:
		play_button.draw_button()

	# 让最近绘制的屏幕可见
	pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
	"""更新子弹位置，并删除子弹"""
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

	check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship,
		aliens, bullets):
	# 击中外星人，则删除子弹和外星人
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

	if collisions:
		for aliens in collisions.values():
			stats.score += ai_settings.alien_points * len(aliens)
			sb.prep_score()
		check_high_score(stats, sb)

	if len(aliens) == 0:
		#删除现有的子弹并重新生产外星人,加快游戏节奏
		stats.level += 1
		sb.prep_level()
		bullets.empty()
		ai_settings.increase_speed()
		create_fleet(ai_settings, screen, ship, aliens)

def fire_bullet(ai_settings, screen, ship, bullets):
	"""子弹未耗尽前发射"""
	if len(bullets) < ai_settings.bullet_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)
	else:
		print('You have no fillings')

def get_number_aliens_x(ai_settings, alien_width):
	"""计算每行有多少个外星人"""
	avaliable_space_x = ai_settings.screen_width - 2 * alien_width
	number_alien_x = int(avaliable_space_x // (2 * alien_width))
	return number_alien_x

def get_number_rows(ai_settings, ship_height, alien_height):
	"""计算屏幕可以容纳多少外星人"""
	avaliable_space_y = (ai_settings.screen_height - 
							(3 * alien_height) - ship_height)
	number_rows = int(avaliable_space_y / (2 * alien_height))
	return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	"""创建外星人并加入当前行"""
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
	"""创建外星人群"""
	# 创建一个外星人
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

	# 创建外星人群
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number, row_number)

def ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets):
	"""响应被飞船撞到的外星人"""
	if stats.ships_left > 0:
		# 将ships_left减1
		stats.ships_left -= 1

		# 更新记分牌
		sb.prep_ships()

		# 清空外星人和子弹
		aliens.empty()
		bullets.empty()

		# 创建新的外星人，并把飞船放到底部中央
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()

		# 暂停
		sleep(0.5)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)

def update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets):
	"""更新所有外新人数量"""
	check_fleet_edges(ai_settings, aliens)
	aliens.update()

	check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets)
	
	# 检测外星人和飞船之间的碰撞
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)

def check_fleet_edges(ai_settings, aliens):
	"""外星人到边界时反应"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break

def change_fleet_direction(ai_settings, aliens):
	"""下移并改动方向"""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1

def check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets):
	"""检查外星人是否到达了低端"""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			# 同飞船被撞到处理
			ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)

def check_high_score(stats, sb):
	"""检查是否诞生了最高得分"""
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score() 