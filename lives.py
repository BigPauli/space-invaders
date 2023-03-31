from turtle import Turtle


class Lives(Turtle):
    def __init__(self):
        super(Lives, self).__init__()
        self.life_icons = []
        self.lives = 3
        self.speed('fastest')
        self.up()
        self.ht()
        self.goto(525, 465)
        self.color('white')
        self.lives_left = 3
        self.write("LIVES", font=('Courier', 20, 'bold'))

    def create_life_icons(self):
        for i in range(3):
            life_icon = Turtle()
            life_icon.up()
            life_icon.speed('fastest')
            life_icon.setheading(90)
            life_icon.goto(675 - 25*i, 485)
            life_icon.color('white')
            self.life_icons.append(life_icon)

    def lose_life(self):
        self.lives_left -= 1
        if self.lives_left >= 0:
            self.life_icons[self.lives_left].ht()
        print(self.lives_left)

    def lose_game(self):
        self.goto(0, 0)
        self.write("YOU LOSE", font=('Courier', 50, 'bold'), align='center')

    def win_game(self, enemy_manager):
        self.goto(0, 0)
        self.write("YOU WIN", font=('Courier', 50, 'bold'), align='center')
