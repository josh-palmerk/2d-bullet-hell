import sys
from game.point import Point
import raylibpy

class AudioService:
    """Handles all the audio in the game.

    Stereotype: 
        Service Provider

    Attributes:
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        self._sounds = {}
        
    def play_sound(self, filename):
        """
        Plays the sound file provided. Make sure to call start_audio before this is called.
        """
        if filename not in self._sounds.keys():
            loaded = raylibpy.load_sound(filename)
            self._sounds[filename] = loaded

        sound = self._sounds[filename]
        raylibpy.play_sound(sound)

    def start_audio(self):
        """
        Initializes the audio device so that sounds can be played.
        """
        raylibpy.init_audio_device()

    def stop_audio(self):
        """
        Closes the audio device at the end of the program.
        """
        raylibpy.close_audio_device()