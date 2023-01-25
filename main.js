class Queen {}
class King {}
class Troll {}
class Knight {}
class WeaponBehavior {}
class KnifeBehavior extends WeaponBehavior {
  useWeapon() {
    console.log("cutting with a knife");
  }
}
class AxeBehavior extends WeaponBehavior {
  useWeapon() {
    console.log("chopping with a axe");
  }
}
class BowAndArrowBehavior extends WeaponBehavior {
  useWeapon() {
    console.log("shooting an arrow with a bow");
  }
}
class SwordBehavior extends WeaponBehavior {
  useWeapon() {
    console.log("swinging a sword");
  }
}

class Character {
  fight() {
    this._weapon.useWeapon();
  }0
  set weapon(w) {
    this._weapon = w;
  }
}

function main() {
  let hero = new Character();
  hero.weapon = new SwordBehavior();
  hero.fight();
}

if (require.main === module) {
  main();
}
