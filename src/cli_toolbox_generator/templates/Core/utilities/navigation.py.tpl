from utilities.input import read_key

# Feature basic color support in-case of failure to render color helper
RESET = "\033[0m"
CYAN = "\033[36m"

def color_text(text, color="cyan"):
    if color == "cyan":
        return f"{CYAN}{text}{RESET}"
    return text

def highlight(label: str, style: str = "pointer", use_color: bool = True) -> str:
    L = color_text(label) if use_color else label

    if style == "pointer":
        return f"➤ {L}"
    if style == "underline":
        return f"{L}\n" + ("─" * len(label))
    if style == "bracket":
        return f"[ {L} ]"
    if style == "bar":
        return f"【 {L} 】"

    return L

def arrow_select_core(count: int, *, debug_enabled: bool = False):
    """
    States:
        ("move", idx)
        ("enter", idx)
        ("esc", idx)
        ("debug", idx)
    """
    index = 0
    yield ("move", index)

    while True:
        key = read_key()

        if key == "UP":
            index = (index - 1) % count
            yield ("move", index)

        elif key == "DOWN":
            index = (index + 1) % count
            yield ("move", index)

        elif key == "ENTER":
            yield ("enter", index)
            return

        elif key == "ESC":
            yield ("esc", index)
            return

        elif debug_enabled and key == "debug":
            yield ("debug", index)
            return

        else:
            continue

def arrow_multiselect_core(count: int, *, debug_enabled: bool = False):
    index = 0
    selected = set()

    yield ("move", index, selected)

    while True:
        key = read_key()

        if key == "UP":
            index = (index - 1) % count
            yield ("move", index, selected)

        elif key == "DOWN":
            index = (index + 1) % count
            yield ("move", index, selected)

        elif key == "SPACE":
            if index in selected:
                selected.remove(index)
            else:
                selected.add(index)
            yield ("move", index, selected)

        elif key == "ENTER":
            yield ("enter", index, selected)
            return

        elif key == "ESC":
            yield ("esc", index, selected)
            return

        elif debug_enabled and key == "debug":
            yield ("debug", index, selected)
            return

        else:
            continue

def parse_number_multiselect(raw, max_index):
    raw = raw.replace(" ", "")
    selections = set()

    for part in raw.split(","):
        if "-" in part:
            try:
                a, b = part.split("-", 1)
                a, b = int(a), int(b)
                for n in range(a, b + 1):
                    if 1 <= n <= max_index:
                        selections.add(n - 1)
            except:
                pass
        else:
            try:
                n = int(part)
                if 1 <= n <= max_index:
                    selections.add(n - 1)
            except:
                pass

    return sorted(selections)
