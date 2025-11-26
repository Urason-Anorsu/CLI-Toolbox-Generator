import os
import sys

IS_WINDOWS = os.name == "nt"

if IS_WINDOWS:
    import msvcrt
else:
    import termios
    import tty

# Normalized return values
UP = "UP"
DOWN = "DOWN"
ENTER = "ENTER"
SPACE = "SPACE"
ESC = "ESC"
CHAR = "CHAR"
OTHER = "OTHER"


def read_key():
    if IS_WINDOWS:
        return _read_key_windows()
    return _read_key_unix()


def _read_key_windows():
    ch = msvcrt.getch()  # type: ignore

    # ENTER
    if ch in (b"\r", b"\n"):
        return ENTER

    # SPACE
    if ch == b" ":
        return SPACE

    # ESC
    if ch == b"\x1b":
        return ESC

    # Arrow prefix
    if ch in (b"\xe0", b"\x00"):
        ch2 = msvcrt.getch()  # type: ignore
        if ch2 == b"H":
            return UP
        if ch2 == b"P":
            return DOWN
        return OTHER

    # Normal printable characters
    try:
        return (CHAR, ch.decode("utf-8"))
    except Exception:
        return OTHER


def _read_key_unix():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)  # type: ignore
    try:
        tty.setraw(fd)  # type: ignore
        ch = sys.stdin.read(1)

        if ch == "\n":
            return ENTER
        if ch == " ":
            return SPACE

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

        return (CHAR, ch)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)  # type: ignore
