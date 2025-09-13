from __future__ import annotations
from dataclasses import dataclass
from typing import Dict

@dataclass
class Item:
    """Simple item that can modify stats or grant abilities.
    
    - stat_mods: mapping stat_name->delta (e.g., {'armor': +5})
    - abilities: list of ability names (strings) that the item grants
    """
    name: str
    stat_mods: Dict[str, int] = None
    abilities: list[str] = None

    def __post_init__(self):
        if self.stat_mods is None:
            self.stat_mods = {}
        if self.abilities is None:
            self.abilities = []
