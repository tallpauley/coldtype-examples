from coldtype import *
from coldtype.pens.datpen import DPR
from functools import partial

Style.RegisterShorthandPrefix("≈", "~/Type/fonts/fonts")

BLOCK = 350

def show_body(glyph, dps):
    box = DPR(glyph.box)
    clip = glyph.clip
    clipped_box = clip(box.copy(), box.copy())
    main = dps.f(None).s(0).sw(1)#.pen().removeOverlap()
    lines = DATPenSet()
    for idx, b in enumerate(glyph.box.subdivide(9, "mny")):
        if idx%2 == 1:
            line = DPR(b.inset(-50, 0))
            lines.append(clip(line.f(0, 0.5, 1), box.copy()))
    
    pt_labels = DATPenSet()
    def labeller(idx, x, y):
        pt_labels.append(StyledString(str(idx), Style("≈/AdobeHandwriting-Frank.otf", 72)).pen().translate(x, y))
    main.map_points(labeller)

    return [
        DATPenSet([
            DPR(glyph.body).f(0.5, 0.75, 0.8, 1).s(0, 1).sw(5),
            main.copy().s(0, 1).sw(1),
            box.copy().f(None).s(1, 0, 0.5).sw(5),
            pt_labels.f(0)
        ]).translate(-400, 0),
        DATPenSet([
            main.copy().f(0).s(None).difference(clipped_box.copy()),
            #clipped_box.copy().f(1,0.35,0.75),
            clipped_box.copy().f(None).s(0).sw(3),
            lines.f(0)
        ]).translate(400, 0)
    ]

sinaloa = partial(glyph, postfn=show_body, rect=(1900, 1000), width=750)

@sinaloa("G")
def _G():
    b = _G.body
    _G.clip = lambda p, bp: p.rotate(-30, point=_G.box.point("C")).translate(0, -35).intersection(DPR(r).translate(0, -b.h/10))
    _G.box = b.take(BLOCK, "mdy").inset(-200, 0)
    r, l = b.divide(0.5, "mxx")
    full_g = DPR(r).semicircle(l, "mxx", 0)
    return full_g.copy()\
        .difference(DPR(r.take(BLOCK/2, "mdy")))\
        .rect(r.take(BLOCK/2, "mny").offset(0, -50))\
        .removeOverlap()

@sinaloa("U")
def _U():
    b = _U.body
    full_u = DPR(b.take(0.5, "mxy")).semicircle(b.take(0.5,"mny"), "mxy", 35).removeOverlap()
    _U.clip = lambda p, bp: p.rotate(-30, point=_U.box.point("C")).intersection(full_u.copy().nudge({7:(0,100),8:(0,100)}))
    _U.box = b.take(BLOCK, "mdy").inset(-200, 0)
    return full_u.copy().copy().difference(DPR(b.take(0.35,"mxy").take(0.5,"mnx")))

@sinaloa("I")
def _I():
    b = _I.body
    _I.clip = lambda p, bp: p.intersection(bp)
    _I.box = b.take(BLOCK, "mxy")
    return DATPen().rect(b.take(0.5, "mdx"))\
        .rect(b.take(BLOCK, "mxy"))\
        .rect(b.take(BLOCK, "mny"))

@sinaloa("T")
def _T():
    b = _T.body
    _T.clip = lambda p, bp: p.intersection(bp)
    _T.box = b.take(BLOCK, "mxy")
    return DATPen().rect(b.take(0.5, "mdx"))\
        .rect(b.take(BLOCK, "mxy"))

@sinaloa("A")
def _A():
    b = _A.body
    n, e, s, w = b.cardinals()
    ne, se, sw, nw = b.intercardinals()
    _A.clip = lambda p, bp: p.intersection(triangle.copy().translate(-b.w/2+20, 0)).intersection(triangle)
    _A.box = b.take(BLOCK, "mny").inset(-100, 0)
    triangle = DATPen().moveTo(se.offset(100, 0))\
        .lineTo(n.offset(0, 30))\
        .lineTo(sw.offset(-100, 0))\
        .closePath()
    return triangle

@sinaloa("R")
def _R():
    b = _R.body
    _R.box = b.take(BLOCK, "mny").inset(-100, 0).offset(100, -40)
    _R.clip = lambda p, bp: p.rotate(-30, point=_R.box.point("C")).intersection(DPR(b.take(0.7, "mxx").inset(0, -300)))
    return DPR(b.take(0.7, "mnx"))\
        .semicircle(b.take(0.3, "mxx").take(0.6, "mxy"), "mnx", -35)\
        .removeOverlap()\
        .nudge({7:(20,0),8:(-150,0)})