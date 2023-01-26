def main():
    heros: list[Character] = [Queen(), King(), Troll(), Knight()]

    for hero in heros:
        hero.fight()


class WeaponBehavior():
    '''Interface for weapon behaviors'''

    def useWeapon(self):
        pass


class Character():
    '''abstract character class'''

    def __init__(self):
        self._weapon = WeaponBehavior()

    def fight(self):
        self._weapon.useWeapon()

    def setWeapon(self, w: WeaponBehavior):
        self._weapon = w


class KnifeBehavior(WeaponBehavior):
    def useWeapon(self):
        print("cutting with a knife")


class AxeBehavior(WeaponBehavior):
    def useWeapon(self):
        print("chopping with an axe")


class BowAndArrowBehavior(WeaponBehavior):
    def useWeapon(self):
        print("shooting an arrow with a bow")


class SwordBehavior(WeaponBehavior):
    def useWeapon(self):
        print("swinging a sword")
    pass


class Queen(Character):
    def __init__(self):
        self.setWeapon(BowAndArrowBehavior())


class King(Character):
    def __init__(self):
        self.setWeapon(KnifeBehavior())


class Troll(Character):
    def __init__(self):
        self.setWeapon(AxeBehavior())


class Knight(Character):
    def __init__(self):
        self.setWeapon(SwordBehavior())


if __name__ == "__main__":
    main()
