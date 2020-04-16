from coldtype import *

class fontpreview(renderable):
    def __init__(self, font_dir, font_re, rect=(1200, 200), limit=25, **kwargs):
        super().__init__(rect=rect, **kwargs)
        self.dir = Path(font_dir).expanduser().resolve()
        self.re = font_re
        self.matches = []
        
        for font in self.dir.iterdir():
            if re.search(self.re, str(font)):
                if len(self.matches) < limit:
                    self.matches.append(font)
        
        self.matches.sort()
    
    def passes(self, action, layers, indices=[]):
        return [RenderPass(self, "{:s}".format(m.name), [self.rect, m]) for m in self.matches]


@fontpreview("~/Type/fonts/fonts", r"Civi", bg=1)
def preview(r, m):
    return [
        StyledString(str(m.stem), Style(str(m), 100)).pens().align(r).f(0),
        str(m.relative_to(preview.dir))
    ]