from dataclasses import dataclass
from typing import Dict, Optional
from cli_toolbox_generator.Builders.menu_builder import MenuNode


@dataclass
class WizardState:
    cli_name: Optional[str] = None
    nav_style: Optional[str] = None
    arrow_style: str = "reverse"
    style: Optional[str] = None
    use_color: Optional[bool] = None

    selected_features: Optional[Dict[str, bool]] = None

    out_dir: Optional[str] = None
    menu_tree: Optional[MenuNode] = None
