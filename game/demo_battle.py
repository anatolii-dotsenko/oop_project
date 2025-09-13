from .character import Character
from .item import Item

def run_demo():
    # Create characters
    alice = Character(name='Alice', hp=50, armor=2, attack=8)
    brute = Character(name='Brute', hp=70, armor=5, attack=10)

    # Items and equipment
    light_amulet = Item(name='Amulet of Vigor', stat_mods={'hp': +10, 'attack': +2}, abilities=['heal'])
    heavy_shield = Item(name='Kite Shield', stat_mods={'armor': +3}, abilities=[])

    log = []
    log.append(alice.equip(light_amulet) or f"{alice.name} equips {light_amulet.name}.")
    log.append(brute.equip(heavy_shield) or f"{brute.name} equips {heavy_shield.name}.")

    # Use ability (heal)
    log.append(alice.use_ability('heal', alice))

    # Attack sequence
    log.append(alice.attack_target(brute))
    log.append(brute.attack_target(alice))
    # Alice uses power_strike without having it (demonstrates missing ability)
    log.append(alice.use_ability('power_strike', brute))
    # Grant power_strike to Alice via ad-hoc item and use
    power_sword = Item(name='Sword of Might', stat_mods={'attack': +5}, abilities=['power_strike'])
    log.append(alice.equip(power_sword) or f"{alice.name} equips {power_sword.name}.")
    log.append(alice.use_ability('power_strike', brute))
    return '\n'.join(log)

if __name__ == '__main__':
    print(run_demo())
