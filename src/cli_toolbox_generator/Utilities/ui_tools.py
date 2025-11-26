import os
import time

# ANSI colors
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"

COLORS = {
    "reset": RESET,
    "red": RED,
    "green": GREEN,
    "yellow": YELLOW,
    "blue": BLUE,
    "magenta": MAGENTA,
    "cyan": CYAN,
}


def color(text, color_code):
    return f"{color_code}{text}{RESET}"


def print_error(msg):
    print(color(msg, RED))


def print_success(msg):
    print(color(msg, GREEN))


def print_warning(msg):
    print(color(msg, YELLOW))


def print_info(msg):
    print(color(msg, CYAN))


def print_highlight(msg):
    print(color(msg, MAGENTA))


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def builder_header(title, parent=None, width=50):
    clear_screen()
    line = "-" * width
    print(line)
    print(f" MENU BUILDER — {title}")
    if parent:
        print(f" Parent: {parent}")
    print(line)


def print_title(text):
    line = "=" * len(text)
    print_info(f"{line}\n{text}\n{line}\n")


def loading(text, duration=1.2):
    print(text, end="", flush=True)
    for _ in range(3):
        time.sleep(duration / 3)
        print(".", end="", flush=True)
    print()
