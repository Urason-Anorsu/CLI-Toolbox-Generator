from typing import List, Optional
from cli_toolbox_generator.Utilities.text_tools import slugify
from cli_toolbox_generator.Models.command_model import CommandNode

class MenuNode:
    def __init__(self, name: str, parent: Optional["MenuNode"] = None):
        self.name: str = name
        self.slug: str = slugify(name)
        self.parent: Optional["MenuNode"] = parent
        self.submenus: List["MenuNode"] = []
        self.commands: List[CommandNode] = []

    def add_submenu(self, submenu: "MenuNode"):
        submenu.parent = self
        self.submenus.append(submenu)
        return submenu

    def add_command(self, cmd_name: str):
        node = CommandNode(cmd_name, is_multi=False)
        self.commands.append(node)
        return node

    def add_multi_command(self, cmd_name: str):
        node = CommandNode(cmd_name, is_multi=True)
        self.commands.append(node)
        return node

    def path(self) -> List[str]:
        node: Optional["MenuNode"] = self
        parts = []
        while node:
            parts.append(node.slug)
            node = node.parent
        return list(reversed(parts))

    def has_multi(self) -> bool:
        return any(cmd.is_multi for cmd in self.commands)

    def is_root(self) -> bool:
        return self.parent is None

    def __repr__(self):
        return (
            f"MenuNode(name={self.name!r}, slug={self.slug!r}, "
            f"submenus={len(self.submenus)}, "
            f"commands={self.commands})"
        )
