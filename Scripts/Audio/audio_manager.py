import pygame

class AudioManager:
    _instance = None  # Biến giữ instance duy nhất

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(AudioManager, cls).__new__(cls)
            cls._instance._initialize()  # Khởi tạo các thuộc tính instance một lần duy nhất
        return cls._instance

    def _initialize(self):
        """Phương thức khởi tạo các thuộc tính chỉ một lần"""
        pygame.mixer.init()
        self.sfxs = {}  # Dictionary to store sfx
        self.background_music = {}  # Dictionary to store background music
        self.sfx_volume = 0.5
        self.music_volume = 0.5

    #sfx
    def load_sfx(self, name, path):
        sfx = pygame.mixer.Sound(path)
        sfx.set_volume(self.sfx_volume)
        self.sfxs[name] = sfx
    def play_sfx(self, name, loops=0): # 0: lặp 1 lần, 1: 2 lần, -1, vô hạn
        if name in self.sfxs:
            self.sfxs[name].play(loops=loops)
    def stop_sfx(self, name):
        if name in self.sfxs:
            self.sfxs[name].stop()
    def set_sfx_volume(self, volume):
        self.sfx_volume = volume
        for sfx in self.sfxs.values():
            sfx.set_volume(volume)

    #background music
    def load_music(self, name, path):
        music = pygame.mixer.Sound(path)
        music.set_volume(self.music_volume)
        self.background_music[name] = music
    def play_music(self, name, loops=-1):
        print("play",name)
        if name in self.background_music:
            self.background_music[name].play(loops=loops)
    def stop_music(self, name):
        print("stop",name)
        if name in self.background_music:
            self.background_music[name].stop()
    def set_music_volume(self, volume):
        self.music_volume = volume
        for music in self.background_music.values():
            music.set_volume(volume)

    @classmethod
    def get_instance(cls):
        """Phương thức truy cập instance duy nhất"""
        if cls._instance is None:
            cls._instance = AudioManager()
        return cls._instance