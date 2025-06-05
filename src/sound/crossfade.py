import pygame

class Crossfade:
    def __init__(self):
        pygame.mixer.pre_init(frequency=48000, buffer=4096)
        pygame.mixer.init()
        self.current_channel = pygame.mixer.Channel(0)
        self.next_channel = pygame.mixer.Channel(1)
        self.current_sound = None
        self.current_file = None
        self.sounds = {}
        
    def preload_sounds(self, sound_files):
        """Preload all sound files into memory"""
        for file in sound_files:
            if file not in self.sounds:
                self.sounds[file] = pygame.mixer.Sound(file)

    def play_sound(self, sound_file):
        if self.current_file == sound_file:
            return
        sound = self.sounds.get(sound_file)
        if sound is None:
            sound = pygame.mixer.Sound(sound_file)
            self.sounds[sound_file] = sound
        self.current_channel.play(sound, fade_ms=500)
        self.current_sound = sound
        self.current_file = sound_file

    def crossfade(self, sound_file_1, sound_file_2, duration):
        if self.current_file != sound_file_1:
            self.play_sound(sound_file_1)
        next_sound = self.sounds.get(sound_file_2)
        if next_sound is None:
            next_sound = pygame.mixer.Sound(sound_file_2)
            self.sounds[sound_file_2] = next_sound
        fade_ms = int(duration * 1000)
        self.current_channel.fadeout(fade_ms)
        self.next_channel.play(next_sound, fade_ms=fade_ms)
        self.current_channel, self.next_channel = self.next_channel, self.current_channel
        self.current_sound = next_sound
        self.current_file = sound_file_2