# ArtAPI

Simple Python library for beautiful animated ASCII banners in the terminal.

## Features

- ✨ Typing animation
- ⚡ Glitch effect
- 💡 Shine effect
- 🌈 RGB grayscale colors
- 🔁 Infinite animation loop
- 📍 Automatic terminal centering

## Installation

```bash
pip install artapi
```

## Usage

```python
from artapi import show

banner = r"""
    _         _   
   / \   _ __| |_ 
  / _ \ | '__| __|
 / ___ \| |  | |_ 
/_/   \_\_|   \__|
"""

show(banner)
```

## Options

```python
show(
    banner,
    typing=True,
    glitch=True,
    flash=True,
    shine=True,
    loop=False,
    speed=0.01
)
```

| Parameter | Description | Default |
|-----------|-------------|---------|
| typing | Typing animation | True |
| glitch | Glitch effect | True |
| flash | Flash effect | True |
| shine | Shine animation | True |
| loop | Infinite shine loop | False |
| speed | Shine animation speed | 0.01 |

## Example

```python
from artapi import show

banner = """
██╗  ██╗███████╗██╗     ██╗      ██████╗
██║  ██║██╔════╝██║     ██║     ██╔═══██╗
███████║█████╗  ██║     ██║     ██║   ██║
██╔══██║██╔══╝  ██║     ██║     ██║   ██║
██║  ██║███████╗███████╗███████╗╚██████╔╝
╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝
"""

show(banner)
```

## Requirements

- Python 3.8+

## License

MIT
