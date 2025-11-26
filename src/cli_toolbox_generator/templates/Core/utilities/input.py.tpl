"""
Cross-platform low-level key reader.

STANDARDIZED OUTPUT:
    "UP", "DOWN", "ENTER", "SPACE", "ESC", "debug", "OTHER"

NOTE:
    UIManager + navigation expect EXACT string:
        → "debug"   (lowercase)
"""

import os
import sys

IS_WINDOWS = os.name == "nt"

if IS_WINDOWS:
    import msvcrt
else:
    import termios
    import tty


# Important return values
UP = "UP"
DOWN = "DOWN"
ENTER = "ENTER"
SPACE = "SPACE"
ESC = "ESC"
DEBUG = "debug"
OTHER = "OTHER"


def read_key():
    """Return UP/DOWN/ENTER/SPACE/ESC/debug/OTHER"""
    try:
        if IS_WINDOWS:
            return _read_key_windows()
        else:
            return _read_key_unix()
    except KeyboardInterrupt:
        return ESC
    except Exception:
        return OTHER

def _read_key_windows():
    ch = msvcrt.getch()

    # ENTER
    if ch in (b"\r", b"\n"):
        return ENTER

    # SPACE
    if ch == b" ":
        return SPACE

    # ESC
    if ch == b"\x1b":
        return ESC

    # DEBUG (d/D) — match raw byte lowercase
    if ch.lower() == b"d":
        return DEBUG   # returns "debug"

    # Arrow keys arrive as two-byte sequences
    if ch in (b"\x00", b"\xe0"):
        ch2 = msvcrt.getch()
        if ch2 == b"H":
            return UP
        if ch2 == b"P":
            return DOWN
        return OTHER

    return OTHER

def _read_key_unix():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)

        # ENTER
        if ch == "\n":
            return ENTER

        # SPACE
        if ch == " ":
            return SPACE

        # DEBUG (d/D)
        if ch.lower() == "d":
            return DEBUG

        # ESC or arrow sequences
        if ch == "\x1b":
            ch2 = sys.stdin.read(1)
            if ch2 != "[":
                return ESC

            ch3 = sys.stdin.read(1)
            if ch3 == "A":
                return UP
            if ch3 == "B":
                return DOWN
            return OTHER

        return OTHER

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
