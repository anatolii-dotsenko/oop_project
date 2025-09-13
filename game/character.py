from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List
from .item import Item
from .ability import Ability

@dataclass
class Character:
    """Base character class used in simple game simulation."""
    name: str
    hp: int
    armor: int
    attack: int
    abilities: List[Ability] = field(default_factory=list)
    inventory: List[Item] = field(default_factory=list)

    def is_alive(self) -> bool:
        return self.hp > 0

    def equip(self, item: Item) -> None:
        """Equip an item: apply stat modifiers and add abilities."""
        self.inventory.append(item)
        for stat, delta in item.stat_mods.items():
            if hasattr(self, stat):
                setattr(self, stat, getattr(self, stat) + delta)
        # Items may grant ability names; real system would resolve them to callable abilities.
        # For demo, we add string placeholders as simple ability-like objects.
        for ab_name in item.abilities:
            self.abilities.append(SimpleAbility(ab_name))

    def attack_target(self, target: 'Character') -> str:
        """Perform a basic attack against another character."""
        if not self.is_alive():
            return f"{self.name} cannot act (dead)."
        if not target.is_alive():
            return f"{target.name} is already down."
        # simple damage model: damage = max(0, attack - target.armor)
        damage = max(0, self.attack - target.armor)
        target.hp -= damage
        return f"{self.name} attacks {target.name} for {damage} damage. ({target.name} HP: {max(0,target.hp)})"

    def heal(self, amount: int) -> str:
        """Heal the character by amount."""
        if not self.is_alive():
            return f"{self.name} cannot be healed (dead)."
        self.hp += amount
        return f"{self.name} heals for {amount}. (HP: {self.hp})"

    def use_ability(self, ability_name: str, target: 'Character' | None = None) -> str:
        """Find ability by name and use it. Returns log string."""
        for ab in self.abilities:
            if getattr(ab, 'name', None) == ability_name:
                return ab.use(self, target)
        return f"{self.name} does not have ability '{ability_name}'."

class SimpleAbility:
    """Small in-file ability wrapper used by Item grants in demo.
    Real projects would use separate ability classes/modules.
    """
    def __init__(self, name: str):
        self.name = name

    def use(self, user: Character, target: Character | None) -> str:
        if name_equals(self.name, 'heal'):
            if target is None:
                target = user
            return user.heal(10)
        if name_equals(self.name, 'power_strike'):
            if target is None:
                return f"{user.name} tries to use power_strike but no target provided."
            # stronger attack bypassing some armor
            damage = max(0, (user.attack * 2) - max(0, target.armor - 2))
            target.hp -= damage
            return f"{user.name} uses Power Strike on {target.name} for {damage} damage. ({target.name} HP: {max(0,target.hp)})"
        return f"{user.name} uses {self.name}, but nothing special happens."

def name_equals(a: str, b: str) -> bool:
    return a.lower() == b.lower()
