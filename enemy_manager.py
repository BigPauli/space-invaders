from turtle import Turtle


class EnemyManager():
    def __init__(self):
        self.enemy_size = (1.5, 1.5)
        self.enemies = []
        self.turns = 500
        self.enemy_direction = 180

    def create_enemies(self):
        for i in range(4):
            for j in range(11):
                enemy = Turtle()
                enemy.speed('fastest')
                enemy.shape('turtle')
                enemy.up()
                enemy.setheading(270)
                enemy.shapesize(stretch_len=self.enemy_size[0], stretch_wid=self.enemy_size[1])
                enemy.goto(-357.5 + 65 * j, 400 - 50 * i)
                enemy.color('green')
                self.enemies.append(enemy)

    def enemies_move(self):
        if self.turns % 50 == 0:
            for dude in self.enemies:
                dude.setheading(self.enemy_direction)
                dude.forward(20)
                dude.setheading(270)

                if self.turns % 400 == 0:
                    dude.forward(10)

        self.turns += 1

    def turn_enemies_around(self):
        if self.turns % 1000 == 0 and self.enemy_direction == 180:
            self.enemy_direction = 0
        elif self.turns % 1000 == 0 and self.enemy_direction == 0:
            self.enemy_direction = 180
