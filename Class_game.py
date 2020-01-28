import time
import numpy as np
import graphics as gr
from Class_Bouncer import Bouncer
from Class_physics import Physics
from Class_Position import Position
from Class_Velocity import Velocity

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
class Game():
    def __init__(self, win):
        self.win = win
        self.initial_x = 100
        self.initial_y = 600
        self.initial_time = 0
        self.rules = Physics(20, 0, 0.3)
        self.initial_velocity = None
        self.bouncer = Bouncer(self)
        self.bouncer.make_bouncer()
        self.collect_input()
        self.allign_screen()
        self.draw_projectile()

    def draw_anything(self, object, color):
        object.setWidth(10)
        object.setFill(color)
        object.draw(self.win)

    def draw_markers(self, x, y, r, undraw):
        self.ball_drawing = gr.Circle(gr.Point(x, y), r)
        self.ball_drawing.setFill('red')
        self.ball_drawing.draw(self.win)
        if undraw == True:
            self.ball_drawing.undraw()

    def draw_start_button(self, x, y, r):
        start = gr.Circle(gr.Point(x, y), r)
        go = gr.Text(gr.Point(x, y),'GO')
        go.setStyle('bold')
        go.setSize(18)
        start.setFill('green')
        start.draw(self.win)
        go.draw(self.win)

    def check_start_button(self):
        point_location = self.win.getMouse()
        if point_location.getY() > 370 and point_location.getY() < 430 and point_location.getX() > 1270 and point_location.getX() < 1330:
            return True
        else:
            return False

    def collect_input(self):
        Angle = gr.Text(gr.Point(1230, 300),'Angle = ')
        Angle.setTextColor('white')
        Angle.setSize(20)
        Angle.draw(self.win)
        input_box_angle = gr.Entry(gr.Point(1300, 300), 5).draw(self.win)
        velocity = gr.Text(gr.Point(1220, 200), 'Velocity = ')
        velocity.setTextColor('white')
        velocity.setSize(20)
        velocity.draw(self.win)
        input_box_velocity = gr.Entry(gr.Point(1300, 200), 5).draw(self.win)
        input_box_angle.setText('1.3')
        input_box_velocity.setText('200')
        self.draw_start_button(1300,400,30)
        if self.check_start_button() == True:
            initial_angle = float(input_box_angle.getText())
            initial_v_x = float(input_box_velocity.getText())* np.cos(initial_angle)
            initial_v_y = float(input_box_velocity.getText())* np.sin(initial_angle)
            self.initial_velocity = Velocity(initial_v_x, initial_v_y, self.initial_time, self.rules)

    def allign_screen(self):
        if self.initial_velocity.v_x < 0:
            self.initial_x = 1300
        if self.initial_velocity.v_y > 0:
            self.initial_y = 250

    def draw_projectile(self):
        instant_time = self.initial_time
        interval = Time_step(0.1)
        ball_initial_position = Position(self.initial_x, self.initial_y, instant_time, self.initial_velocity, self.rules)
        self.inst_x, self.inst_y = ball_initial_position.x, ball_initial_position.y
        self.draw_markers(self.inst_x, self.inst_y, 20, True)
        while self.inst_y < 800:
            self.draw_markers(self.inst_x, self.inst_y, 15, True)
            instant_time += interval.step_size
            ball_instantaneous_velocity = Velocity(self.initial_velocity.v_x, self.initial_velocity.v_y, instant_time, self.rules)
            self.inst_v_x, self.inst_v_y = ball_instantaneous_velocity.instantaneous_velocity()
            print(self.inst_v_x, self.inst_v_y)
            ball_inst_position = Position(self.initial_x, self.initial_y, instant_time, self.initial_velocity, self.rules)
            self.inst_x, self.inst_y = ball_inst_position.instantaneous_position()
            self.bouncer.move_bouncer(70, 70)
            self.check_collision()
        self.bouncer.undraw_bouncer()
        for i in range(len(self.bouncer.list_of_bricks)):
            self.bouncer.list_of_bricks[i][0].undraw()
        Game(self.win)

    def check_too_slow(self):
        print('checking if too slow')
        print(self.initial_velocity.v_x, self.initial_velocity.v_y)
        if self.initial_velocity.v_x> -2 and self.initial_velocity.v_x < 2 and self.initial_velocity.v_y> -8 and self.initial_velocity.v_x < 8:
            print('too slow')
            self.bouncer.undraw_bouncer()
            self.ball_drawing.undraw()
            for i in range(len(self.bouncer.list_of_bricks)):
                self.bouncer.list_of_bricks[i][0].undraw()
            Game(self.win)


    def check_collision(self):
        left_edge = self.bouncer.left_edge.getP1()
        right_edge = self.bouncer.right_edge.getP1()
        base = self.bouncer.base.getP1()
        if self.inst_y < 140:
            for i in range(len(self.bouncer.list_of_bricks)):
                mid_x = self.bouncer.list_of_bricks[i][1]
                mid_y = self.bouncer.list_of_bricks[i][2]
                if self.inst_x > mid_x - 50 and self.inst_x < mid_x + 50 and self.inst_y > mid_y - 10 and self.inst_y < mid_y + 10:
                    self.collision("brick", i)
                    break

        if self.inst_x > base.getX()-5 and self.inst_x < base.getX() + 105 and self.inst_y > base.getY() - 10 and self.inst_y < base.getY() + 10:
            self.collision("base",0)
        if self.inst_x > left_edge.getX()-5 and self.inst_x < left_edge.getX() + 5 and self.inst_y > left_edge.getY() - 105 and self.inst_y < left_edge.getY()+5:
            self.collision("left_edge",0)
        if self.inst_x > right_edge.getX()-5 and self.inst_x < right_edge.getX() + 5 and self.inst_y > left_edge.getY() - 105 and self.inst_y < left_edge.getY()+5:
            self.collision("right_edge",0)

    def collision(self, side, i):
        if side == "base":
            self.bouncer.base.setFill('red')
            self.initial_x = self.inst_x
            if self.inst_v_y < 0:
                self.initial_y = self.inst_y + 3
            else:
                self.initial_y = self.inst_y - 3
            initial_v_y = self.inst_v_y  # it was 0.8
            if self.inst_v_x > 0:
                initial_v_x = self.inst_v_x #- self.rules.friction
            else:
                initial_v_x = self.inst_v_x #+ self.rules.friction
            self.initial_velocity = Velocity(initial_v_x, initial_v_y, self.initial_time, self.rules)
            self.check_too_slow()
            self.bouncer.base.setFill('green')
            self.draw_projectile()
        if side == "brick":
            self.initial_x = self.inst_x
            if self.inst_v_y < 0:
                self.initial_y = self.inst_y + 3
                initial_v_y = 1 * self.inst_v_y  # it was 0.8
                if self.inst_v_x > 0:
                    initial_v_x = self.inst_v_x #- self.rules.friction
                else:
                    initial_v_x = self.inst_v_x #+ self.rules.friction
                self.initial_velocity = Velocity(initial_v_x, initial_v_y, self.initial_time, self.rules)
                print('undraw', self.bouncer.list_of_bricks[i][0])
                self.bouncer.list_of_bricks[i][0].undraw()
                self.bouncer.list_of_bricks.pop(i)
                print('finished')
                self.check_too_slow()
                self.draw_projectile()

        if side == "right_edge" or "left_edge":
            if side == "right_edge":
                self.bouncer.right_edge.setFill('red')
                self.bouncer.left_edge.setFill('green')
            else:
                self.bouncer.left_edge.setFill('red')
                self.bouncer.right_edge.setFill('green')
            self.initial_y = self.inst_y
            if self.inst_v_x > 0:
                self.initial_x = self.inst_x - 3
                initial_v_x = -1 * self.inst_v_x #+ self.rules.friction
            else:
                self.initial_x = self.inst_x + 3
                initial_v_x = -1 * self.inst_v_x # -self.rules.friction
            initial_v_y = -1 * self.inst_v_y  # it was -0.8
            self.initial_velocity = Velocity(initial_v_x, initial_v_y, self.initial_time, self.rules)
            self.check_too_slow()
            self.bouncer.left_edge.setFill('green')
            self.bouncer.right_edge.setFill('green')
            self.draw_projectile()


class Time_step():
    def __init__(self, step_size):
        self.step_size = step_size
    def time_step(self):
        time.sleep(self.step_size)

