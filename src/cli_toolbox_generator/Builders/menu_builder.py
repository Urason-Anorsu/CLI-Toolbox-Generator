from cli_toolbox_generator.Models.menu_model import MenuNode
from cli_toolbox_generator.Utilities.selector import select
from cli_toolbox_generator.Utilities.ui_tools import (
    builder_header,
    print_title,
    print_warning,
    color,
    CYAN,
    MAGENTA,
)


class MenuTreeBuilder:
    # Generic input helpers
    def ask(self, question, default=None, color_code=None):
        if color_code:
            question = color(question, color_code)
        answer = input(f"{question} ").strip()
        return answer or default

    def ask_int(self, question, default="1", color_code=None):
        while True:
            val = self.ask(question, default, color_code)
            try:
                return int(val)  # type: ignore
            except ValueError:
                print_warning("Please enter a valid number.\n")

    def _select_with_context(
        self,
        menu_name,
        parent_name,
        question,
        color_code,
        options,
    ):
        header = []
        header.append(color(f"Editing menu: {menu_name}", CYAN))
        if parent_name:
            header.append(color(f"Parent menu: {parent_name}", MAGENTA))

        header.append("")
        header.append(color(question, color_code))
        header.append("")

        return select("\n".join(header), options)

    # Main recursive builder
    def build(self, name: str = "Main Menu", parent=None) -> MenuNode:
        builder_header(name, parent)
        node = MenuNode(name=name)

        # Submenus
        has_sub = self._select_with_context(
            name,
            parent,
            "Does this menu have submenus?",
            CYAN,
            ["No", "Yes"],
        )

        if has_sub == "Yes":
            count = self.ask_int("How many submenus?", "0", CYAN)

            submenu_names = [
                self.ask(f"Name for submenu {i}:", color_code=CYAN)
                for i in range(1, count + 1)
            ]

            for submenu_name in submenu_names:
                child = self.build(submenu_name, parent=name)  # type: ignore
                node.add_submenu(child)

            builder_header(name, parent)

        # Commands
        has_cmd = self._select_with_context(
            name,
            parent,
            "Does this menu have commands?",
            MAGENTA,
            ["No", "Yes"],
        )

        if has_cmd == "Yes":
            print_title("Add Commands")
            print(
                "You can add:\n"
                "  • Single commands (one-off actions)\n"
                "  • Multi-enabled commands (used in batch / multi-select flows)\n"
            )

            # Single commands
            single_count = self.ask_int(
                "How many SINGLE commands?",
                "0",
                MAGENTA,
            )
            for i in range(1, single_count + 1):
                label = self.ask(f"Single Command {i} label:", color_code=MAGENTA)
                node.add_command(label)  # type: ignore

            # Multi-enabled commands
            multi_count = self.ask_int(
                "How many MULTI-enabled commands?",
                "0",
                MAGENTA,
            )
            if multi_count > 0:
                print(
                    "\nMulti-enabled commands will be available for\n"
                    "multi-select / batch-style handling inside the generated CLI.\n"
                )

            for i in range(1, multi_count + 1):
                label = self.ask(f"Multi Command {i} label:", color_code=MAGENTA)
                node.add_multi_command(label)  # type: ignore

        return node
