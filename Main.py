from Class_game import Game
import graphics as gr
def main():
    height=850
    width=1400
    win=gr.GraphWin("projectile",width,height, autoflush=True)
    Game(win)
    win.getMouse()
main()
