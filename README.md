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

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

## Author

Ismail - [@Imismail18](https://github.com/Imismail18)

## License

MIT License

Copyright (c) 2026 Ismail

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

- `SnakeGame.py` is intended for terminal use and is best run in a terminal window.
- `ironman.py` opens a graphical window using Python's `turtle` module.
- Both scripts are lightweight examples and can be run independently.
