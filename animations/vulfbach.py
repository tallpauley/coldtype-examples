from coldtype import *

@animation()
def render(f):
    return DATPen().oval(f.a.r.inset(50)).f(hsl(0.8, 0.6, 0.5))