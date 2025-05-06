import aubio

from enums.sample_rate import SampleRateEnum


class PitchService:
    def __init__(
        self,
        tolerance=0.8,
        win_s=4096,
        buffer_size=1024,
        sample_rate=SampleRateEnum.DVD,
    ):
        self.tolerance = tolerance
        self.win_s = win_s
        self.hop_s = buffer_size
        self.sample_rate = sample_rate
        self.pitch = None

    def setup_pitch(self):
        self.pitch = aubio.pitch("default", self.win_s, self.hop_s, self.sample_rate)
        self.pitch.set_unit("midi")
        self.pitch.set_tolerance(self.tolerance)
