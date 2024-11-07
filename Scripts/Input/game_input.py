import pygame
from Scripts.game_constants import GameConstants

class GameInput:
    _instance = None  # Biến giữ instance duy nhất

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(GameInput, cls).__new__(cls)
            cls._instance._initialize()  # Khởi tạo các thuộc tính instance một lần duy nhất
        return cls._instance

    def _initialize(self):
        """Phương thức khởi tạo các thuộc tính chỉ một lần"""
        self.right1 = False
        self.left1 = False
        self.up1 = False
        self.down1 = False


        self.right2 = False
        self.left2 = False
        self.up2 = False
        self.down2 = False

    def update(self):
        """Cập nhật trạng thái phím bấm"""
        key = pygame.key.get_pressed()
        self.right1 = key[GameConstants.RIGHT1]
        self.left1 = key[GameConstants.LEFT1]
        self.up1 = key[GameConstants.UP1]
        self.down1 = key[GameConstants.DOWN1]
        self.right2 = key[GameConstants.RIGHT2]
        self.left2 = key[GameConstants.LEFT2]
        self.up2 = key[GameConstants.UP2]
        self.down2 = key[GameConstants.DOWN2]

    @classmethod
    def get_instance(cls):
        """Phương thức truy cập instance duy nhất"""
        if cls._instance is None:
            cls._instance = GameInput()
        return cls._instance