import pyaudio
from enums.sample_rate import SampleRateEnum


class MicrophoneService:
    def __init__(
        self,
        audio=pyaudio.PyAudio(),
        record_duration=0,
        buffer_size=1024,
        audio_format=pyaudio.paFloat32,
        sample_rate=SampleRateEnum.DVD,
        n_channels=1,
    ):
        self.buffer_size = buffer_size
        self.audio_format = audio_format
        self.n_channels = n_channels
        self.sample_rate = sample_rate
        self.audio = audio
        self.record_duration = record_duration
        self.microphone = None

    def open_stream(self):
        self.microphone = self.audio.open(
            format=self.audio_format,
            channels=self.n_channels,
            rate=self.sample_rate,
            input=True,
            frames_per_buffer=self.buffer_size,
        )

    def close_stream(self):
        self.microphone.stop_stream()
        self.microphone.close()
        self.audio.terminate()
