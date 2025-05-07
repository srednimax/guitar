import numpy as np

from enums.sample_rate import SampleRateEnum
from helpers.midi_converter import MidiConverter
from services.microphone_service import MicrophoneService
from services.pitch_service import PitchService

if __name__ == "__main__":
    print("*** starting recording")
    microphone_service = MicrophoneService(sample_rate=SampleRateEnum.CD)
    pitch_service = PitchService()
    converter = MidiConverter()

    microphone_service.open_stream()
    pitch_service.setup_pitch()
    buffer_size = 1024
    while True:
        try:
            audio_buffer = microphone_service.microphone.read(buffer_size)
            signal = np.frombuffer(audio_buffer, dtype=np.float32)

            pitch = pitch_service.pitch(signal)[0]
            confidence = pitch_service.pitch.get_confidence()

            if confidence > .33:
               print(f'{pitch}')
        except KeyboardInterrupt:
            print("*** Ctrl+C pressed, exiting")
            break

    microphone_service.close_stream()
    print("*** done recording")
