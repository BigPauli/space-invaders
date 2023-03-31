from turtle import Turtle


class CoverManager():
    def __init__(self):
        self.size = (0.25, 0.5)
        self.entities = []

    def create_cover(self):
        for k in range(0, 5):
            for i in range(1, 5):
                for j in range(1, 5):
                    block = Turtle()
                    block.up()
                    block.speed('fastest')
                    block.shape('square')
                    block.shapesize(stretch_len=self.size[0], stretch_wid=self.size[1])
                    block.goto(-612.5 + 5*i + 300*k, -300 + 10*j)
                    block.color('white')
                    self.entities.append(block)