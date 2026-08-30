# SNAKGAME

This project contains two small Python programs: a classic terminal Snake game and a simple Iron Man-inspired drawing made with `turtle`.

## Project Contents

### 1. Snake Game

A classic terminal-based Snake game built with Python and the `curses` library.

Features:
- Arrow-key controls
- Random food spawning
- Snake growth when eating food
- Wall and self-collision detection
- Simple terminal-based gameplay

Run it with:

```bash
python3 SnakeGame.py
```

Controls:
- Up Arrow: move up
- Down Arrow: move down
- Left Arrow: move left
- Right Arrow: move right

### 2. Iron Man Drawing

A Python script that draws an Iron Man-inspired face using the `turtle` graphics library.

Features:
- Colored background and face design
- Polygon-based drawing
- Lightweight, standalone graphics demo

Run it with:

```bash
python3 ironman.py
```

## Requirements

- Python 3
- `curses` support for the Snake game (works best in a terminal)
- Standard Python `turtle` module for the Iron Man drawing

## Project Structure

```text
SNAKGAME/
├── SnakeGame.py
├── ironman.py
├── README.md
```

## Notes

- `SnakeGame.py` is intended for terminal use and is best run in a terminal window.
- `ironman.py` opens a graphical window using Python's `turtle` module.
- Both scripts are lightweight examples and can be run independently.
