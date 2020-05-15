#import math
import numpy as np
import soundfile as sf
from coldtype import *

"""
You'll need to `pip install soundfile` to get this to work
"""

class Wavfile():
    """
    This is not good code, but it is enough code
    """
    def __init__(self, path, fps=30):
        self.sf, self.sf_fs = sf.read(str(path))
        self.fps = fps
        self.hz = self.sf_fs
        self.samples_per_frame = self.hz / fps
        self.path = path
        self.peaks = self.sf
        self.framelength = int(round(len(self.peaks) / self.samples_per_frame))

        max_frame_amp = 0
        for i in range(0, self.framelength):
            amp = self.amp(i)
            if amp > max_frame_amp:
                max_frame_amp = amp
        self.max_frame_amp = max_frame_amp

    def calc_peaks(self):
        snd = self.sf / (2.**15)
        s1 = snd[:, 0]
        return s1

    def samples_for_frame(self, i):
        start_sample = math.floor(i * self.samples_per_frame)
        end_sample = math.floor(start_sample + self.samples_per_frame)
        return self.peaks[start_sample:end_sample]

    def amp(self, i):
        return np.average(np.fabs(self.samples_for_frame(i)))


audio = Wavfile("animations/media/coldtype.wav")
obvs = Font("fonts/ColdtypeObviously.designspace")

@animation(duration=audio.framelength, storyboard=[13])
def render(f):
    amp = audio.amp(f.i)
    return StyledString("COLDTYPE", Style(obvs, 700, tu=-50+150*(0.2+pow(amp,2)*5), r=1, ro=1, rotate=5+10*amp, wdth=0)).pens().align(f.a.r).f(hsl(0.9, l=0.7)).s(0).sw(5)