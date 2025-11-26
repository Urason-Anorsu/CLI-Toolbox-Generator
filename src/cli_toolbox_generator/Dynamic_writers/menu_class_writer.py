from pathlib import Path
from cli_toolbox_generator.Utilities.text_tools import slugify
from cli_toolbox_generator.Template_tools.template_writer import TemplateWriter


class MenuClassWriter:
    def __init__(self, template_root="src/cli_toolbox_generator/templates"):
        self.template_root = Path(template_root)
        self.template_writer = TemplateWriter(template_root)

        self.internal_template = (
            self.template_root / "Internal_Templates_NotReg" / "menu_class.py.tpl"
        )

        if not self.internal_template.exists():
            raise FileNotFoundError(
                f"Missing menu_class template:\n{self.internal_template}"
            )

    # Write Menu
    def write_menu_class(self, node, output_folder, config):
        slug = slugify(node.name)
        module_name = f"{slug}_menu"
        class_name = f"{slug.title().replace('_', '')}Menu"

        # Submenus
        submenu_prints = []
        submenu_handlers = []

        for sm in node.submenus:
            sm_slug = slugify(sm.name)

            submenu_prints.append(
                f'        options.append(("{sm_slug}", "{sm.name}", "submenu"))'
            )

            submenu_handlers.append(
                f'        if choice == "{sm_slug}": return "{sm_slug}"'
            )

        # Commands
        command_prints = []
        command_handlers = []
        command_methods = []

        for cmd in node.commands:
            cmd_slug = getattr(cmd, "slug", slugify(cmd.name))
            label = cmd.name

            if getattr(cmd, "is_multi", False):
                # Multi-Selection Command
                method_name = f"cmd_multi_{cmd_slug}"

                command_prints.append(
                    f'        options.append(("{method_name}", "{label}", "multi"))'
                )

                command_handlers.append(
                    f'        if choice == "{method_name}": return self.{method_name}()'
                )

                command_methods.append(
                    f"""    def {method_name}(self):
        \"\"\"TODO: Implement MULTI-SELECT command '{label}'\"\"\"
        # User will choose multiple items using UI.choose_multi()
        choices = self.ui.choose_multi([
            "Option A",
            "Option B",
            "Option C",
        ])

        if not choices:
            return None

        self.ui.clear()
        print("Running multi-select command for: {label}")
        print("Selected items:")
        for c in choices:
            print(" -", c)

        self.ui.pause("Press Enter to return...")
        return None

"""
                )

            else:
                # Single Command
                method_name = f"cmd_{cmd_slug}"

                command_prints.append(
                    f'        options.append(("{method_name}", "{label}", "command"))'
                )

                command_handlers.append(
                    f'        if choice == "{method_name}": self.{method_name}(); return None'
                )

                command_methods.append(
                    f"""    def {method_name}(self):
        \"\"\"TODO: Implement command '{label}'\"\"\"
        self.ui.clear()
        print("TODO: Command: {label}")
        self.ui.pause("Press Enter to return...")
        return None

"""
                )

        # Template Rendering
        output_rel = f"menus/{module_name}.py"
        project_root = Path(output_folder).parent

        self.template_writer.write(
            template_path=self.internal_template,
            target_project_root=project_root,
            output_rel=output_rel,
            # Template Vars
            menu_name=node.name,
            class_name=class_name,
            submenu_prints="\n".join(submenu_prints),
            submenu_handlers="\n".join(submenu_handlers),
            command_prints="\n".join(command_prints),
            command_handlers="\n".join(command_handlers),
            command_methods="\n".join(command_methods),
            multi_group_prints="",
            multi_group_handlers="",
            multi_group_methods="",
        )

        return slug, module_name, class_name
