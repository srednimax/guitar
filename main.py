import numpy as np

from services.microphone_service import MicrophoneService
from services.pitch_service import PitchService

if __name__ == "__main__":
    print("*** starting recording")
    microphone_service = MicrophoneService()
    pitch_service = PitchService()

    microphone_service.open_stream()
    pitch_service.setup_pitch()
    buffer_size = 1024
    while True:
        try:
            audio_buffer = microphone_service.microphone.read(buffer_size)
            signal = np.fromstring(audio_buffer, dtype=np.float32)

            pitch = pitch_service.pitch(signal)[0]
            confidence = pitch_service.pitch.get_confidence()

            print("{} / {}".format(pitch, confidence))
        except KeyboardInterrupt:
            print("*** Ctrl+C pressed, exiting")
        break

print("*** done recording")
