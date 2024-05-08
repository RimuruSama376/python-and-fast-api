class Enemy:

    def __init__(self, type_of_enemy, health_points=10, attack_damage=1):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def talk(self):
        print(f'I am a {self.__type_of_enemy}. Be prepared to fight')
        return

    def move_forward(self):
        print(f'{self.__type_of_enemy} moves closer to you!.')

    def attack(self):
        print(f'{self.__type_of_enemy} attacks for {self.attack_damage} damage')

    def get_type_of_enemy(self):
        return self.__type_of_enemy

    def print_info(self):
        print('===================')
        print(f'Type of Enemy: {self.__type_of_enemy}\n'
              f'Health points: {self.health_points}\n'
              f'Attack Damage: {self.attack_damage}')
