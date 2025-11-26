import os
from utilities.navigation import (
    highlight,
    arrow_select_core,
    arrow_multiselect_core,
    parse_number_multiselect,
)

class UIManager:

    def __init__(
        self,
        navigation_mode="numbers",
        style="clean",
        use_color=True,
        arrow_style="pointer",
        debug_enabled=True,
    ):
        self.navigation_mode = navigation_mode
        self.style = style
        self.use_color = use_color
        self.arrow_style = arrow_style
        self.debug_enabled = True

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    def pause(self, msg="Press Enter to continue..."):
        input(msg)

    def header(self, text: str | None):
        if not text:
            return

        if self.style == "minimal":
            print(text + "\n")
            return

        if self.style == "clean":
            print(f"== {text} ==")
            print()
            return

        if self.style == "box":
            pad = len(text) + 4
            line = "─" * pad
            print("┌" + line + "┐")
            print(f"│  {text}  │")
            print("└" + line + "┘\n")
            return

        print(text + "\n")

    def _render_rows_number(self, labels):
        rows = [f"{i}) {label}" for i, label in enumerate(labels, start=1)]
        rows.append("0) Back")
        return rows

    def _render_rows_arrow(self, labels, index):
        rows = []
        for i, label in enumerate(labels):
            if i == index:
                rows.append(
                    highlight(
                        label,
                        style=self.arrow_style,
                        use_color=self.use_color,
                    )
                )
            else:
                rows.append(label)
        return rows

    def _print_rows(self, rows):
        for r in rows:
            print(r)

    def _num_single(self, labels, title=None):
        self.clear()

        if title:
            self.header(title)

        rows = self._render_rows_number(labels)
        self._print_rows(rows)

        choice = input("> ").strip()

        # DEBUG Hotkey
        if choice == "d":
            return "-1"

        if choice == "0":
            return "__back__"

        if not choice.isdigit():
            return None

        idx = int(choice) - 1
        if 0 <= idx < len(labels):
            return labels[idx]

        return None

    def _arrow_single(self, labels, title=None):
        gen = arrow_select_core(
            len(labels),
            debug_enabled=self.debug_enabled,
        )

        state, index = next(gen)

        while True:
            self.clear()

            if title:
                self.header(title)
                print()

            rows = self._render_rows_arrow(labels, index)
            self._print_rows(rows)

            state, index = next(gen)

            if state == "move":
                continue

            if state == "esc":
                return "__back__"

            if state == "debug":
                return "-1"

            if state == "enter":
                return labels[index]

    def choose(self, labels, title=None):
        if self.navigation_mode == "arrows":
            return self._arrow_single(labels, title=title)
        return self._num_single(labels, title=title)

    def _num_multi(self, labels, title=None):
        self.clear()

        if title:
            self.header(title)
            print()

        print("Multi-select (example: 1,3-5)\n")

        for i, label in enumerate(labels, start=1):
            print(f"{i}) {label}")
        print("0) Cancel\n")

        raw = input("> ").strip()

        if raw == "-1":
            return "-1"

        if raw == "0":
            return []

        idxs = parse_number_multiselect(raw, len(labels))
        return [labels[i] for i in idxs]

    def _arrow_multi(self, labels, title=None):
        gen = arrow_multiselect_core(
            len(labels),
            debug_enabled=self.debug_enabled,
        )

        state, index, selected = next(gen)

        while True:
            self.clear()

            if title:
                self.header(title)
                print()

            rows = []
            for i, label in enumerate(labels):
                box = "[x]" if i in selected else "[ ]"
                line = f"{box} {label}"

                if i == index:
                    rows.append(
                        highlight(
                            line,
                            style=self.arrow_style,
                            use_color=self.use_color,
                        )
                    )
                else:
                    rows.append(line)

            self._print_rows(rows)

            state, index, selected = next(gen)

            if state == "move":
                continue

            if state == "esc":
                return []

            if state == "debug":
                return "-1"

            if state == "enter":
                return [labels[i] for i in selected]

    def choose_multi(self, labels, title=None):
        if self.navigation_mode == "arrows":
            return self._arrow_multi(labels, title=title)
        return self._num_multi(labels, title=title)
