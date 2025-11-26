"""Auto-generated menu for {{menu_name}}"""

from typing import Optional, List
from utilities.display import print_error   # ensure this exists

class {{class_name}}:

    BACK_LABEL = "← Back"

    def __init__(self, ui):
        self.ui = ui

    # Build (key, label, kind) option list
    def _build_options(self):
        options = []

{{submenu_prints}}

{{command_prints}}

        return options

    # Display
    def display(self):
        self.ui.clear()

        options = self._build_options()

        labels = [label for (_, label, kind) in options]

        if self.ui.navigation_mode == "arrows":
            labels.append(self.BACK_LABEL)

        selected = self.ui.choose(labels, title="{{menu_name}}")

        if selected in ("__back__", self.BACK_LABEL):
            return "__back__", "back"

        if selected == "-1":
            return "-1", "debug"

        for (key, label, kind) in options:
            if label == selected:

                if kind == "multi":
                    return key, "multi"

                return key, kind

        return None, None

    def handle(self) -> Optional[str]:
        choice, kind = self.display()

        if choice == "__back__":
            return "__back__"

        if choice == "-1":
            return "-1"

{{submenu_handlers}}

{{command_handlers}}

        print_error("Invalid choice.")
        input()
        return None

{{command_methods}}
