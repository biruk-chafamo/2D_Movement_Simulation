import graphics as gr
import numpy as np
class Bouncer():
    def __init__(self, game):
        self.game = game
        self.list_of_bricks = []
    def make_bouncer(self):
        for j in range(6):
            level = 20 + j*20
            for i in range(13):
                start = i*110
                end = start + 100
                self.brick = gr.Line(gr.Point(start, level), gr.Point(end, level))
                self.list_of_bricks.append(self.bouncer_details(self.brick))
                self.game.draw_anything(self.brick, gr.color_rgb(190, 60, 30))
        self.left_edge = gr.Line(gr.Point(650, 750), gr.Point(650, 750-100))
        self.right_edge = gr.Line(gr.Point(750, 750), gr.Point(750, 750-100))
        self.base = gr.Line(gr.Point(645, 750), gr.Point(755, 750))

        self.game.draw_anything(self.left_edge, 'green')
        self.game.draw_anything(self.right_edge, 'green')
        self.game.draw_anything(self.base, 'green')

    def bouncer_details(self, object):
        mid_y = object.getCenter().getY()
        mid_x = object.getCenter().getX()
        width = object.getP2().getX() - object.getP1().getX()
        length = object.getP2().getY() - object.getP1().getY()
        angle = np.arctan(length/width)
        return [object, mid_x, mid_y, angle]
    def linked_bouncers_move(self, dx, dy):
        self.right_edge.move(dx, dy)
        self.left_edge.move(dx, dy)
        self.base.move(dx,dy)
    def undraw_bouncer(self):
        self.right_edge.undraw()
        self.left_edge.undraw()
        self.base.undraw()
    def move_bouncer(self, dx, dy):
        key = self.game.win.checkKey()
        if key == "d":
            self.linked_bouncers_move(dx, 0)
        if key == "a":
            self.linked_bouncers_move(-dx, 0)
        if key == "w":
            self.linked_bouncers_move(0, -dy)
        if key == "s":
            self.linked_bouncers_move(0, dy)