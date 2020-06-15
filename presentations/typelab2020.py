from coldtype import *
from functools import partial

Style.RegisterShorthandPrefix("≈", "~/Type/fonts/fonts")

taters = Font("≈/Taters0.2-Baked.otf")
obvs = Font("≈/ObviouslyVariable.ttf")

class slide(renderable):
    def __init__(self, **kwargs):
        super().__init__(rect=(1920, 1080), bg=0, **kwargs)

def simple_text(rect, string):
    return StyledString(string, Style(obvs, 250, wght=0.75, wdth=1, slnt=1)).fit(1200).pens().align(rect).f(1)

#@slide()
def hello(r):
    return simple_text(r, "Hello!")

#@slide()
def welcome(r):
    return simple_text(r, "Welcome to this presentation!")

def label(s, pt, xalign, yalign):
    sp = StyledString(s, Style(obvs, 50, wght=0.25, wdth=0.25, slnt=1)).pens().f(1)
    sf = sp.getFrame()
    r = Rect(pt.x, pt.y, 0, 0)
    sp.align(r, x=xalign, y=yalign)
    return sp

@slide()
def circle(r):
    c = r.take(500, "mdx").square()
    co = r.take(550, "mdx").square()

    return DATPenSet([
        DATPen().oval(c).f(None).s(1).sw(5),
        label("Premiere Pro", co.point("N"), "mdx", "mny"),
        label("Coldtype", co.point("E"), "mnx", "mdy"),
        label("DrawBot", co.point("S"), "mdx", "mxy"),
        label("After Effects", co.point("W"), "mxx", "mdy")
    ])