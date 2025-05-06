from enum import IntEnum


class SampleRateEnum(IntEnum):
    CD = 44100
    DVD = 48000
    STUDIO = 96000
    STUDIO_MAX = 192000
