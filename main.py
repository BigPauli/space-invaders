from turtle import Screen
from player_ship import PlayerShip
from bullet_manager import BulletManager
from cover_manager import CoverManager
from enemy_manager import EnemyManager
from lives import Lives

# -- screen setup -- #
screen = Screen()
screen.bgcolor('black')
screen.setup(width=1500, height=1000)
screen.title("Space Invaders")
screen.tracer(0)

# -- create an instance of every class from other files -- #
player_ship = PlayerShip()
bullet_manager = BulletManager()
cover_manager = CoverManager()
cover_manager.create_cover()
enemy_manager = EnemyManager()
enemy_manager.create_enemies()
lives = Lives()
lives.create_life_icons()

# ----- player controls ----- #
screen.listen()
screen.onkey(player_ship.move_left, 'Left')
screen.onkey(player_ship.move_right, 'Right')
screen.onkey(lambda: bullet_manager.player_shoot(player_ship), 'space')

# ----- game functionality ----- #
game_active = True

while game_active:
    screen.update()
    enemy_manager.enemies_move()
    enemy_manager.turn_enemies_around()
    bullet_manager.roll_enemy_shots(enemy_manager)
    bullet_manager.bullets_move()

    # detect enemy bullet collision with barriers, player, and floor
    for bullet in bullet_manager.enemy_bullets:
        for barrier_part in cover_manager.entities:
            if abs(bullet.xcor() - barrier_part.xcor()) <= 5 and abs(bullet.ycor() - barrier_part.ycor()) <= 20:
                if bullet not in bullet_manager.enemy_bullets:
                    continue
                bullet_manager.enemy_bullets.remove(bullet)
                bullet.ht()
                cover_manager.entities.remove(barrier_part)
                barrier_part.ht()
        if abs(bullet.xcor() - player_ship.xcor()) <= 25 and abs(bullet.ycor() - player_ship.ycor()) <= 25:
            bullet_manager.enemy_bullets.remove(bullet)
            bullet.ht()
            lives.lose_life()
            player_ship.back_to_start()
        if bullet.ycor() <= -500:
            bullet_manager.enemy_bullets.remove(bullet)
            bullet.ht()

    # detect player bullet collision with barriers, aliens, and ceiling
    for bullet in bullet_manager.player_bullets:
        for barrier_part in cover_manager.entities:
            if bullet not in bullet_manager.player_bullets:
                continue
            if abs(bullet.xcor() - barrier_part.xcor()) <= 10 and abs(bullet.ycor() - barrier_part.ycor()) <= 30:
                bullet_manager.enemy_bullets.remove(bullet)
                bullet.ht()
                cover_manager.entities.remove(barrier_part)
                barrier_part.ht()
        for enemy in enemy_manager.enemies:
            if abs(bullet.xcor() - enemy.xcor()) <= 30 and abs(bullet.ycor() - enemy.ycor()) <= 40:
                if bullet not in bullet_manager.player_bullets:
                    continue
                bullet_manager.player_bullets.remove(bullet)
                bullet.ht()
                enemy_manager.enemies.remove(enemy)
                enemy.ht()
        if bullet.ycor() >= 500:
            bullet_manager.player_bullets.remove(bullet)
            bullet.ht()

    # detect if game is lost or won
    if not enemy_manager.enemies:
        lives.win_game(enemy_manager)
        game_active = False

    for enemy in enemy_manager.enemies:
        if enemy.ycor() <= -300:
            lives.lose_game()
            game_active = False

    if lives.lives_left < 0:
        lives.lose_game()
        game_active = False


screen.mainloop()
