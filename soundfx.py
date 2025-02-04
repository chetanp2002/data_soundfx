import numpy as np
import simpleaudio as sa

class SoundFX:
    def generate_tone(self, frequency, duration=0.5, volume=0.5):
        sample_rate = 44100
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        wave = np.sin(2 * np.pi * frequency * t) * volume
        audio = (wave * 32767).astype(np.int16)
        play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
        play_obj.wait_done()

    def play_chime(self):
        self.generate_tone(880, 0.2)
