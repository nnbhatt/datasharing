"""Turn-based battle system for the fantasy RPG engine."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import pygame

from .entities import Entity, Player, Enemy


@dataclass
class BattleResult:
    winner: Optional[str]
    message: str


class Battle:
    """Simple one-on-one battle between a player and a single enemy."""

    def __init__(self, player: Player, enemy: Enemy, screen: pygame.Surface) -> None:
        self.player = player
        self.enemy = enemy
        self.screen = screen
        self.font = pygame.font.Font(None, 18)
        self.turn = "player"

    def draw(self) -> None:
        """Render player, enemy and their HP bars."""
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.player.sprite, (40, 100))
        self.screen.blit(self.enemy.sprite, (200, 100))

        player_hp = self.font.render(f"{self.player.name} HP: {self.player.hp}", True, (255, 255, 255))
        enemy_hp = self.font.render(f"{self.enemy.name} HP: {self.enemy.hp}", True, (255, 255, 255))
        self.screen.blit(player_hp, (20, 20))
        self.screen.blit(enemy_hp, (180, 20))

    def update(self) -> Optional[BattleResult]:
        """Carry out a single turn and return a result when finished."""
        if self.turn == "player":
            damage = self.player.deal_damage(self.enemy)
            result = f"{self.player.name} strikes for {damage} damage!"
            self.turn = "enemy"
        else:
            damage = self.enemy.deal_damage(self.player)
            result = f"{self.enemy.name} claws for {damage} damage!"
            self.turn = "player"

        if not self.player.is_alive():
            return BattleResult(winner=self.enemy.name, message=f"{self.player.name} has fallen!")
        if not self.enemy.is_alive():
            return BattleResult(winner=self.player.name, message=f"{self.enemy.name} is defeated!")

        self.message = self.font.render(result, True, (255, 255, 0))
        self.screen.blit(self.message, (20, 180))
        return None
