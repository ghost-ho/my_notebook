from manim import *
import numpy as np

class Anim1(Scene):
    def construct(self):
        # 群同态基本定理的交换图
        # 坐标系
        plane = Axes(
            x_range=[-3, 3],
            y_range=[-3, 3]
        )

        G = Tex(r"$G$").set_color(WHITE).move_to(LEFT * 2 + UP * 1.5)
        f = Tex(r"$f$").set_color(RED)
        Image_f = Tex(r"$\mathrm{Im}f$").set_color(RED)
        Ker_f = Tex(r"$G/\ker f$").set_color(GREEN_A)
        pi = Tex(r"$\pi$").set_color(GREEN_A)
        arrow1 = Arrow(G.get_coord, Image_f.get_coord).set_color(RED)
        arrow2 = Arrow(G.get_coord, Image_f.get_coord).set_color(RED)
        arrow3 = Arrow(G.get_coord, Image_f.get_coord).set_color(RED)






