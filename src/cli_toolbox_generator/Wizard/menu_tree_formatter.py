from typing import List
from cli_toolbox_generator.Models.menu_model import MenuNode


class MenuTreeFormatter:
    @staticmethod
    def format(node: MenuNode, indent: int = 0) -> str:
        pad = "    " * indent
        lines: List[str] = []

        submenu_count = len(node.submenus)
        command_count = len(node.commands)
        multi_count = sum(1 for c in node.commands if getattr(c, "is_multi", False))

        header = (
            f"{pad}- #{node.name} (Menus: {submenu_count} | Commands: {command_count}"
        )

        if multi_count:
            header += f" | Multi: {multi_count}"

        header += ")"
        lines.append(header)

        for sub in node.submenus:
            lines.append(MenuTreeFormatter.format(sub, indent + 1))

        for cmd in node.commands:
            marker = "[M]" if getattr(cmd, "is_multi", False) else "[ ]"
            lines.append(f"{pad}    * {marker} {cmd.name}")

        return "\n".join(lines)
