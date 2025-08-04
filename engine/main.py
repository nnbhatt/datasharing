"""Entry point for the fantasy RPG engine demonstration."""
from __future__ import annotations

import time

import pygame

from .battle import Battle
from .entities import Player, Enemy
from .world import World


WIDTH, HEIGHT = 320, 240


def create_sprite(color: tuple[int, int, int]) -> pygame.Surface:
    surf = pygame.Surface((32, 32))
    surf.fill(color)
    return surf


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Epic of Bharat")

    # World map: simple cross-section of sand, forest and water.
    data = [
        [0, 0, 1, 1, 2, 2],
        [0, 0, 1, 1, 2, 2],
        [0, 0, 1, 1, 2, 2],
        [0, 0, 1, 1, 2, 2],
    ]
    world = World(data)

    player = Player(create_sprite((255, 215, 0)))
    enemy = Enemy(create_sprite((178, 34, 34)))
    battle = Battle(player, enemy, screen)

    clock = pygame.time.Clock()
    running = True
    result = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        world.render(screen)
        battle.draw()
        if result is None:
            result = battle.update()
        else:
            msg = pygame.font.Font(None, 24).render(result.message, True, (255, 255, 255))
            screen.blit(msg, (20, 200))

        pygame.display.flip()
        clock.tick(2)  # slow tick to emulate turn-based pacing

    pygame.quit()


if __name__ == "__main__":
    main()
