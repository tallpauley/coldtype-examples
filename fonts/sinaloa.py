from coldtype import *

BLOCK = 350

@glyph("I")
def _I():
    b = _I.body
    _I.clip = lambda p: p.intersection(DATPen().rect(box))
    return DATPenSet([
        DATPen().rect(b.take(0.5, "mdx"))\
            .rect(b.take(BLOCK, "mxy"))
            .rect(b.take(BLOCK, "mny")).removeOverlap().tag("main").f(None).s(0).sw(5),
        DATPen().rect(b.take(350, "mxy")).tag("cutout").f(0, 0.15)
    ])