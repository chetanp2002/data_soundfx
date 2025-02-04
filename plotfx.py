import matplotlib.pyplot as plt
from .soundfx import SoundFX

class SoundPlot:
    def __init__(self):
        self.soundfx = SoundFX()

    def plot_with_sound(self, data, plot_type='line', sound_type='chime'):
        # Plot the data
        plt.figure(figsize=(8, 4))
        if plot_type == 'line':
            plt.plot(data, marker='o')
        plt.title('Data Plot with Sound Effects')
        plt.show()

        # Play sound effects for each data point
        for value in data:
            if sound_type == 'chime':
                self.soundfx.generate_tone(200 + value * 10)
