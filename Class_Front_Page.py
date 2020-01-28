import graphics as gr
from Class_game import Game
class Front_Page():
    def __init__(self, win):
        self.win = win
        self.draw_start_button(700,425,50)
        self.check_start_button()
    def draw_start_button(self, x, y, r):
        self.start = gr.Circle(gr.Point(x, y), r)
        self.go = gr.Text(gr.Point(x, y),'Start')
        self.go.setStyle('bold')
        self.go.setSize(18)
        self.start.setFill('green')
        self.start.draw(self.win)
        self.go.draw(self.win)
    def check_start_button(self):
        point_location = self.win.getMouse()
        if point_location.getY() > 375 and point_location.getY() < 475 and point_location.getX() > 650 and point_location.getX() < 750:
            self.go.undraw()
            self.start.undraw()
            Game(self.win)
            win.getMouse()