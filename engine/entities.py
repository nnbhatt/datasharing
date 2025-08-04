"""Game entity definitions for the fantasy RPG engine.

This module defines base :class:`Entity` objects as well as specific
player and enemy classes. These are simple data containers that hold
basic statistics used during battle. Sprites are represented using
:Pygame:`pygame.Surface` objects so the engine can draw them using a
16-bit inspired aesthetic.
"""
from __future__ import annotations

import pygame


class Entity:
    """A base game object with combat statistics.

    Parameters
    ----------
    name:
        Display name of the entity.
    hp:
        Hit points; when this reaches zero the entity is defeated.
    attack:
        Base attack strength.
    defense:
        Base defensive power.
    sprite:
        Pygame surface used when rendering the entity.
    """

    def __init__(self, name: str, hp: int, attack: int, defense: int, sprite: pygame.Surface) -> None:
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sprite = sprite

    def is_alive(self) -> bool:
        """Return ``True`` if the entity has remaining hit points."""
        return self.hp > 0

    def take_damage(self, amount: int) -> None:
        """Reduce hit points by ``amount`` accounting for defense."""
        damage = max(0, amount - self.defense)
        self.hp = max(0, self.hp - damage)

    def deal_damage(self, target: "Entity") -> int:
        """Inflict damage on ``target`` and return the amount dealt."""
        damage = self.attack
        target.take_damage(damage)
        return damage


class Player(Entity):
    """Hero controlled by the player.

    The default stats evoke a heroic warrior from ancient Indian epics.
    """

    def __init__(self, sprite: pygame.Surface) -> None:
        super().__init__("Kshatriya", hp=30, attack=8, defense=3, sprite=sprite)


class Enemy(Entity):
    """Simple enemy inspired by mythological rakshasa."""

    def __init__(self, sprite: pygame.Surface) -> None:
        super().__init__("Rakshasa", hp=20, attack=6, defense=1, sprite=sprite)
