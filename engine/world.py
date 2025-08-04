"""Tile-based world map for the fantasy RPG engine.

The world is represented as a grid of integers. Each integer maps to a
simple 16-bit styled colour. This minimal approach keeps the engine
lightweight while evoking classic pixel-art aesthetics.
"""

from __future__ import annotations

from typing import List

import pygame

# Tile definitions: (r, g, b)
TILES = {
    0: (210, 180, 140),  # sand - Ganges riverbank
    1: (34, 139, 34),    # forest
    2: (70, 130, 180),   # water
}

SCALE = 3
TILE_SIZE = 16


class World:
    """Simple world composed of coloured tiles."""

    def __init__(self, data: List[List[int]]) -> None:
        self.data = data
        self.surface = pygame.Surface((len(data[0]) * TILE_SIZE, len(data) * TILE_SIZE))
        self.draw_world()

    def draw_world(self) -> None:
        for y, row in enumerate(self.data):
            for x, tile in enumerate(row):
                pygame.draw.rect(
                    self.surface,
                    TILES[tile],
                    pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE),
                )

    def render(self, screen: pygame.Surface) -> None:
        scaled = pygame.transform.scale(
            self.surface,
            (self.surface.get_width() * SCALE, self.surface.get_height() * SCALE),
        )
        screen.blit(scaled, (0, 0))
