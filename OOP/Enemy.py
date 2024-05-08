class Enemy:
    type_of_enemy: str
    health_points: int = 10
    attack_damage: int = 1

    def __init__(self, type_of_enemy, health_points=10, attack_damage=1):
        self.type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage
        print(f'Creating a new {type_of_enemy}')

    def talk(self):
        print(f'I am a {self.type_of_enemy}. Be prepared to fight')
        return

    def move_forward(self):
        print(f'{self.type_of_enemy} moves closer to you!.')

    def attack(self):
        print(f'{self.type_of_enemy} attacks for {self.attack_damage} damage')

    def print_info(self):
        print(f'Type of Enemy: {self.type_of_enemy}\n'
              f'Health points: {self.health_points}\n'
              f'Attack Damage: {self.attack_damage}')
