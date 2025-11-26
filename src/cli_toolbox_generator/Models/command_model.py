from dataclasses import dataclass
from cli_toolbox_generator.Utilities.text_tools import slugify

@dataclass
class CommandNode:
    name: str
    is_multi: bool = False

    def __post_init__(self):
        self.slug: str = slugify(self.name)

    def __repr__(self) -> str:
        flag = "multi" if self.is_multi else "single"
        return f"CommandNode(name={self.name!r}, slug={self.slug!r}, type={flag})"
