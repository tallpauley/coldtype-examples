#import math
import numpy as np
import soundfile as sf
from coldtype import *

"""
You'll need to `pip install soundfile` to get this to work

N.B. Though animating to audio _seems_ like a good idea, and can
be executed nicely, given the difference between how the human
brain processes sound and how the human brain processes images,
I’ve found it’s usually better to power an "audio" animation using
non-audio sources, like a MIDI file, or just frame-numbers, both
because actual audio data is rarely as clean as you’d like it to be,
but also because audio data is simply more difficult to understand
and work with. Using sparse non-audio data, you can ease-in
and ease-out of "hits" — this is important, because audio data
itself almost never "eases in," even though we crave "ease-in"
information when watching music; think of a drummer hitting a
drum, or a guitarist strumming — we’re seeing them ease-in to
the sounds, but there is no sound before the sound. (Also our
brains process sound wayyy faster than our eyeballs can process
site, which explains why we only need 24 images a second to be
fooled, but thousand and thousands of samples.)

This is why there’s not canonical class for reading audio data in
the coldtype library itself.

But!

Sometimes it is fun to read an actual audio file.
So here’s an example of that.
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