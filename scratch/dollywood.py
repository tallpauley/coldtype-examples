from coldtype import *

dw = Font("scratch/dollywood.ufo")
palatino = Font("/System/Library/Fonts/Palatino.ttc", 2)

@renderable((1200, 1200))
def dollywood(r):
    pens = StyledString("Dolywud", Style(dw, 500, r=0, ro=1)).pens().f(hsl(0.05, s=0.7, l=0.65)).align(r)
    butterfly = pens.copy().pfilter(lambda idx, p: p.glyphName == "w")[0].explode()
    pens = pens.copy().pfilter(lambda idx, p: p.glyphName != "w")

    butterfly[0].f(0)
    butterfly[3].f(hsl(0, s=0.7, l=0.6)).s(0).sw(2)
    butterfly[4].f(hsl(0, s=0.7, l=0.6)).s(0).sw(2)
    butterfly[5].f(hsl(0.2, s=0.7, l=0.8)).s(0).sw(2)
    butterfly[6].f(hsl(0.2, s=0.7, l=0.8)).s(0).sw(2)
    butterfly[7].f(hsl(0.55, s=0.7, l=0.5)).s(0).sw(2)
    butterfly[8].f(hsl(0.55, s=0.7, l=0.5)).s(0).sw(2)
    butterfly[9].f(hsl(0.65, s=0.5, l=0.6)).s(0).sw(2)
    butterfly[10].f(hsl(0.65, s=0.5, l=0.6)).s(0).sw(2)

    hello = StyledString("Hello,", Style("~/Type/fonts/fonts/BrushScriptStd.otf", 300)).pens()#.align(r).translate(0, 350).scale(0.8, 1)
    semi = DATPen().oval(r).scale(5, center=r.point("N")).translate(0, -350).intersection(DATPen().rect(r)).reverse()
    hello.scale(0.8, 1).distributeOnPath(semi, offset=230).f(hsl(0.6,0.7,0.6))
    pigeon = StyledString("PigeonForge,Tenn.", Style(palatino, 50)).pens().align(r).f(0).scale(0.9, 1)
    return hello, pens.understroke(sw=8), butterfly, hello, pigeon.translate(0, -200)