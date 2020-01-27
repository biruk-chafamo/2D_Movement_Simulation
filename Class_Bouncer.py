import graphics as gr
class Bouncer():
    def __init__(self, game):
        self.game = game
    def make_bouncer(self):
        self.left_edge = gr.Line(gr.Point(100, 750), gr.Point(100, 750-100))
        self.right_edge = gr.Line(gr.Point(200, 750), gr.Point(200, 750-100))
        self.base = gr.Line(gr.Point(95, 750), gr.Point(205, 750))
        self.game.draw_anything(self.left_edge)
        self.game.draw_anything(self.right_edge)
        self.game.draw_anything(self.base)
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