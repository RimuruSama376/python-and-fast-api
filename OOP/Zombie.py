from Enemy import *


class Zombie(Enemy):
    def __init__(self):
        super().__init__('Zombie')

    def talk(self):
        print('Zombie sees you and is grumbling!!!!!!!')\
