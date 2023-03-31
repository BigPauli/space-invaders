from turtle import Turtle
import random


class BulletManager():
    def __init__(self):
        #TODO: change this around to be more like cover manager
        self.player_bullets = []
        self.enemy_bullets = []

    def roll_enemy_shots(self, enemy_manager):
        for enemy in enemy_manager.enemies:
            if random.randint(0, 9000) == 9000:
                self.enemy_shoot(enemy)

    def enemy_shoot(self, enemy):
        bullet = Turtle()
        bullet.up()
        bullet.shape('square')
        bullet.shapesize(stretch_wid=0.25, stretch_len=1)
        bullet.setheading(270)
        bullet.goto(enemy.xcor(), enemy.ycor())
        bullet.color('green')
        self.enemy_bullets.append(bullet)

    def player_shoot(self, player_ship):
        if len(self.player_bullets) < 3:
            bullet = Turtle()
            bullet.up()
            bullet.shape('square')
            bullet.shapesize(stretch_wid=0.25, stretch_len=1)
            bullet.setheading(90)
            bullet.goto(player_ship.xcor(), player_ship.ycor())
            bullet.color('white')
            self.player_bullets.append(bullet)

    def bullets_move(self):
        for bullet in self.player_bullets:
            bullet.forward(1.5)
        for bullet in self.enemy_bullets:
            bullet.forward(1.5)