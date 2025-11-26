import os
from cli_toolbox_generator.Utilities.input import read_key, UP, DOWN, SPACE, ENTER, ESC, CHAR


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def select(title, options):
    index = 0

    while True:
        clear()
        print(title)
        print("-" * len(title))
        print("Use ↑/↓, ENTER to confirm, Q or ESC to cancel.\n")

        for i, opt in enumerate(options):
            pointer = "➤" if i == index else " "
            print(f"{pointer} {opt}")

        key = read_key()

        if key == UP:
            index = (index - 1) % len(options)

        elif key == DOWN:
            index = (index + 1) % len(options)

        elif key == ENTER:
            return options[index]

        elif key == ESC:
            return None

        elif isinstance(key, tuple) and key[0] == CHAR:
            if key[1].lower() == "q":
                return None


def multi_select(title, options_dict):
    keys = list(options_dict.keys())
    labels = list(options_dict.values())

    index = 0
    selected = set()

    while True:
        clear()
        print(title)
        print("-" * len(title))
        print("Use ↑/↓, SPACE to toggle, ENTER to confirm, Q or ESC to cancel.\n")

        for i, label in enumerate(labels):
            pointer = "➤" if i == index else " "
            mark = "[x]" if keys[i] in selected else "[ ]"
            print(f"{pointer} {mark}  {label}")

        key = read_key()

        if key == UP:
            index = (index - 1) % len(labels)

        elif key == DOWN:
            index = (index + 1) % len(labels)

        elif key == SPACE:
            k = keys[index]
            selected.remove(k) if k in selected else selected.add(k)

        elif key == ENTER:
            return list(selected)

        elif key == ESC:
            return None

        elif isinstance(key, tuple) and key[0] == CHAR:
            if key[1].lower() == "q":
                return None
