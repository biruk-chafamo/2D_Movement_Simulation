from Class_game import *
import graphics as gr
def main():
    height=850
    width=1400
    win=gr.GraphWin("projectile",width,height, autoflush=True)
    win.setBackground(gr.color_rgb(30, 60, 30))
    Front_Page(win)
    # win.getMouse()
main()
