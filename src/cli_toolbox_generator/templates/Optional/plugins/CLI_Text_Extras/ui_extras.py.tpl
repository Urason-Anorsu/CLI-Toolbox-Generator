# Extra UI and Input Helpers

import sys

# Display Helpers
def hr(char='-'):
    print(char * 40)


def banner(text):
    text = str(text)
    width = len(text) + 6
    print('*' * width)
    print(f"*  {text}  *")
    print('*' * width)


def title_block(text):
    text = str(text)
    width = len(text) + 8
    print("=" * width)
    print(f"=== {text} ===")
    print("=" * width)


def section(text):
    print(f"-- {text} --")


def pad(text, width=20):
    return str(text).ljust(width)


# Input Helpers
def ask_yes_no(prompt):
    while True:
        ans = input(prompt + " (y/n): ").strip().lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("Please enter 'y' or 'n'.")

def ask_int(prompt):
    while True:
        val = input(prompt + ": ").strip()
        if val.isdigit() or (val.startswith("-") and val[1:].isdigit()):
            return int(val)
        print("Please enter a valid integer.")

def ask_choice(prompt, choices):
    print(prompt)
    for idx, item in enumerate(choices, 1):
        print(f"  {idx}) {item}")
    while True:
        sel = input("> ").strip()
        if sel.isdigit():
            sel = int(sel)
            if 1 <= sel <= len(choices):
                return choices[sel - 1]
        print("Invalid choice. Try again.")

def select_from_list(items):
    if not items:
        print("No items available.")
        return None
    for i, item in enumerate(items, 1):
        print(f"{i}) {item}")
    while True:
        sel = input("> ").strip()
        if sel.isdigit():
            sel = int(sel)
            if 1 <= sel <= len(items):
                return items[sel - 1]
        print("Invalid selection. Try again.")

# Progress Bar Utilities
def _render_progress_bar(percent, width=30):
    if percent < 0:
        percent = 0
    if percent > 1:
        percent = 1

    filled = int(percent * width)
    empty = width - filled

    bar = "█" * filled + "░" * empty
    pct = int(percent * 100)

    return f"[{bar}] {pct:3d}%"


def progress(percent, width=30):
    """Draw a static progress bar for 0.0 → 1.0."""
    bar = _render_progress_bar(percent, width)
    sys.stdout.write("\r" + bar)
    sys.stdout.flush()

    if percent >= 1:
        sys.stdout.write("\n")
        sys.stdout.flush()


def progress_bar(iterable, width=30):
    total = len(iterable) if hasattr(iterable, "__len__") else None

    if total is None:
        for item in iterable:
            yield item
        return

    for i, item in enumerate(iterable, 1):
        percent = i / total
        bar = _render_progress_bar(percent, width)
        sys.stdout.write("\r" + bar)
        sys.stdout.flush()
        yield item

    sys.stdout.write("\n")
    sys.stdout.flush()
