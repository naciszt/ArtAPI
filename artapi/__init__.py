import shutil
import time
import math
import random
import sys
import re

from pystyle import Colors, Colorate

RESET = "\033[0m"
GLITCH = "@#$%&▓▒░/\\|<>ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

_ANSI_RE = re.compile(r'\033\[[0-9;]*m')


def _strip_ansi(s: str) -> str:
    return _ANSI_RE.sub("", s)


def rgb(v):
    return f"\033[38;2;{v};{v};{v}m"


def _draw(lines, top, left):
    pad = " " * left
    # Move cursor to top row of banner area
    print(f"\033[{top + 1};1H", end="")
    for line in lines:
        print(pad + line + RESET)
    sys.stdout.flush()

def xcenter(text: str) -> str:
    width = shutil.get_terminal_size((120, 30)).columns
    return "\n".join(line.center(width) for line in text.strip("\n").splitlines())


def gradient(text: str) -> str:
    return Colorate.Vertical(Colors.white_to_black, text, 1)

def show(
    ascii,
    typing=True,
    glitch=True,
    flash=True,
    shine=True,
    loop=False,
    speed=0.01
):
    lines = ascii.strip("\n").splitlines()
    width = max((len(line) for line in lines), default=0)

    size = shutil.get_terminal_size((120, 30))
    top  = max((size.lines - len(lines)) // 2, 0)
    left = max((size.columns - width) // 2, 0)

    # Clear screen once at the start
    print("\033[2J\033[H", end="")
    print("\033[?25l", end="")  # hide cursor
    sys.stdout.flush()

    try:
        # ---------------- Typing ----------------
        if typing:
            for i in range(width + 1):
                frame = []
                for y, line in enumerate(lines):
                    base = max(90, 255 - y * 25)
                    out = ""
                    for ch in line[:i]:
                        out += rgb(base) + ch
                    frame.append(out)
                _draw(frame, top, left)
                time.sleep(0.002)

        # ---------------- Glitch ----------------
        if glitch:
            for _ in range(10):
                frame = []
                for y, line in enumerate(lines):
                    base = max(90, 255 - y * 25)
                    out = ""
                    for ch in line:
                        if ch != " " and random.random() < 0.08:
                            ch = random.choice(GLITCH)
                        out += rgb(base) + ch
                    frame.append(out)
                _draw(frame, top, left)
                time.sleep(0.03)

        # ---------------- Flash ----------------
        if flash:
            frame = ["\033[97;1m" + line for line in lines]
            _draw(frame, top, left)
            time.sleep(0.06)

        # ---------------- Shine ----------------
        if shine:
            pos = -10
            while True:
                frame = []
                for y, line in enumerate(lines):
                    base = max(90, 255 - y * 25)
                    out = ""
                    for x, ch in enumerate(line):
                        glow = int(130 * math.exp(-((x - pos) ** 2) / 5))
                        c = min(255, base + glow)
                        out += rgb(c) + ch
                    frame.append(out)
                _draw(frame, top, left)
                pos += 1
                if pos > width + 10:
                    if loop:
                        pos = -10
                    else:
                        break
                time.sleep(speed)

    finally:
        # Move cursor just below the banner so menu prints right under it
        banner_bottom = top + len(lines) + 1
        print(f"\033[{banner_bottom};1H", end="")
        print("\033[?25h", end="")  # show cursor
        print(RESET, end="")
        sys.stdout.flush()
