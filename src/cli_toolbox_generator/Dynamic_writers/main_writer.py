from pathlib import Path
from cli_toolbox_generator.Template_tools.template_writer import TemplateWriter
from cli_toolbox_generator.Utilities.text_tools import slugify


class MainWriter:
    def __init__(self, template_root="src/cli_toolbox_generator/templates"):
        self.template_root = Path(template_root)
        self.template_writer = TemplateWriter(template_root)

        self.internal_template = (
            self.template_root / "Internal_Templates_NotReg" / "main.py.tpl"
        )

    def write(
        self,
        project_path,
        root_menu,
        menu_info,
        navigation_style,
        formatting_style,
        arrow_style,
    ):
        root_slug = slugify(root_menu.name)

        # Build dynamic blocks
        menu_imports = []
        parent_entries = []
        builder_entries = []

        for slug, data in menu_info.items():
            menu_imports.append(
                f"from menus.{data['module']} import {data['class_name']}"
            )

            parent_entries.append(f"    '{slug}': {repr(data['parent'])},")

            builder_entries.append(f"    menus['{slug}'] = {data['class_name']}(ui)")

        # Write template
        return self.template_writer.write(
            template_path=self.internal_template,
            target_project_root=Path(project_path),
            output_rel="main.py",
            menu_imports="\n".join(menu_imports),
            parent_dict="\n".join(parent_entries),
            menu_builder="\n".join(builder_entries),
            navigation_style=navigation_style,
            formatting_style=formatting_style,
            arrow_style=arrow_style,
            root_slug=root_slug,
        )
