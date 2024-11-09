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
        self.right_p1 = False
        self.left_p1 = False
        self.up_p1 = False
        self.down1 = False
        self.nomal_attack_p1 = False
        self.skill_1_p1 = False
        self.skill_2_p1 = False
        self.skill_3_p1 = False


        self.right_p2 = False
        self.left_p2 = False
        self.up_p2 = False
        self.down_p2 = False
        self.nomal_attack_p2 = False
        self.skill_1_p2 = False
        self.skill_2_p2 = False
        self.skill_3_p2 = False

    def update(self):
        """Cập nhật trạng thái phím bấm"""
        key = pygame.key.get_pressed()
        self.right_p1 = key[GameConstants.RIGHT1]
        self.left_p1 = key[GameConstants.LEFT1]
        self.up_p1 = key[GameConstants.UP1]
        self.down1 = key[GameConstants.DOWN1]
        self.nomal_attack_p1 = key[GameConstants.NOMALATTACK1]
        self.skill_1_p1 = key[GameConstants.SKILL1_1]
        self.skill_2_p1 = key[GameConstants.SKILL2_1]
        self.skill_3_p1 = key[GameConstants.SKILL3_1]

        self.right_p2 = key[GameConstants.RIGHT2]
        self.left_p2 = key[GameConstants.LEFT2]
        self.up_p2 = key[GameConstants.UP2]
        self.down_p2 = key[GameConstants.DOWN2]
        self.nomal_attack_p2 = key[GameConstants.NOMALATTACK2]
        self.skill_1_p2 = key[GameConstants.SKILL1_2]
        self.skill_2_p2 = key[GameConstants.SKILL2_2]
        self.skill_3_p2 = key[GameConstants.SKILL3_2]

    @classmethod
    def get_instance(cls):
        """Phương thức truy cập instance duy nhất"""
        if cls._instance is None:
            cls._instance = GameInput()
        return cls._instance