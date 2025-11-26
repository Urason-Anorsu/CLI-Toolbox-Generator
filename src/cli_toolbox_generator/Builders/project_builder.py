from pathlib import Path

from cli_toolbox_generator.Dynamic_writers.menu_class_writer import MenuClassWriter
from cli_toolbox_generator.Dynamic_writers.documentation_writer import DocumentationWriter
from cli_toolbox_generator.Dynamic_writers.main_writer import MainWriter

from cli_toolbox_generator.Template_tools.template_scanner import TemplateScanner
from cli_toolbox_generator.Template_tools.template_writer import TemplateWriter


class ProjectStructure:
    def __init__(self, config):
        self.config = config

        self.menu_writer = MenuClassWriter()
        self.doc_writer = DocumentationWriter()
        self.main_writer = MainWriter()

        self.templates_root = Path(__file__).resolve().parent.parent / "templates"

        self.scanner = TemplateScanner(template_root=self.templates_root)
        self.template_writer = TemplateWriter(template_root=self.templates_root)

    def generate_project(self, menu_tree, project_path):
        project_path = Path(project_path).resolve()
        project_path.mkdir(parents=True, exist_ok=True)

        menus_dir = project_path / "menus"
        menus_dir.mkdir(parents=True, exist_ok=True)
        (menus_dir / "__init__.py").write_text("# Menus package\n")

        # Core templates
        for kind, _feature, _rel_output, tpl_path in self.scanner.discover():
            if kind != "core":
                continue

            self.template_writer.write(
                template_path=tpl_path,
                target_project_root=project_path,
                cli_name=self.config.cli_name,
                formatting_style=self.config.formatting_style,
                navigation_style=self.config.navigation_style,
                use_color=self.config.use_color,
                arrow_style=self.config.arrow_style,
                features=self.config.features,
            )

        # Optional templates
        for feature_key, detail in (self.config.feature_details or {}).items():
            if not self.config.features.get(feature_key, False):
                continue

            for tpl_path in detail.get("tpls", []):
                self.template_writer.write(
                    template_path=tpl_path,
                    target_project_root=project_path,
                    cli_name=self.config.cli_name,
                    formatting_style=self.config.formatting_style,
                    navigation_style=self.config.navigation_style,
                    use_color=self.config.use_color,
                    arrow_style=self.config.arrow_style,
                    features=self.config.features,
                )

        # Menu Classes
        menu_info = self._write_all_menus(
            root_node=menu_tree,
            menus_dir=str(menus_dir),
        )

        # Documentation
        self.doc_writer.write(
            project_root=str(project_path),
            project_name=self.config.cli_name,
            config=self.config,
        )

        # Main.py
        self.main_writer.write(
            project_path=str(project_path),
            root_menu=menu_tree,
            menu_info=menu_info,
            navigation_style=self.config.navigation_style,
            formatting_style=self.config.formatting_style,
            arrow_style=self.config.arrow_style,
        )

        return project_path

    def _write_all_menus(self, root_node, menus_dir):
        queue = [(root_node, None)]
        info = {}

        while queue:
            node, parent_slug = queue.pop(0)

            slug, module_name, class_name = self.menu_writer.write_menu_class(
                node=node,
                output_folder=menus_dir,
                config=self.config,
            )

            info[slug] = {
                "module": module_name,
                "class_name": class_name,
                "parent": parent_slug,
            }

            for submenu in node.submenus:
                queue.append((submenu, slug)) #type: ignore

        return info
