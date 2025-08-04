# Fantasy India RPG Engine

This prototype demonstrates a tiny turn-based role playing engine
inspired by 16-bit classics. It uses [Pygame](https://www.pygame.org/)
for rendering a pixel-art world and battle scenes set in a fantasy
interpretation of ancient India.

## Running

```
python -m engine.main
```

A small window will open displaying a tile-based world and an automated
battle between a heroic *Kshatriya* and a fearsome *Rakshasa*. The
visuals are intentionally simple to illustrate the engine structure.

## Structure

* `engine/entities.py` – data classes for the player and enemies.
* `engine/battle.py` – small turn-based combat loop.
* `engine/world.py` – tile map rendering utilities.
* `engine/main.py` – entry point combining the components.

The engine is intentionally lightweight but serves as a starting point
for building richer mechanics, story, and artwork.
