import os
from pathlib import Path

from cli_toolbox_generator.Wizard.wizard_state import WizardState
from cli_toolbox_generator.Wizard.wizard_aborter import Aborter

from cli_toolbox_generator.Builders.menu_builder import MenuTreeBuilder
from cli_toolbox_generator.Wizard.menu_tree_formatter import MenuTreeFormatter

from cli_toolbox_generator.Utilities.ui_tools import (
    clear_screen,
    print_title,
    print_success,
    print_warning,
    print_error,
)
from cli_toolbox_generator.Utilities.selector import select, multi_select

from cli_toolbox_generator.Models.project_model import ProjectConfig
from cli_toolbox_generator.Utilities.output_manager import OutputManager
from cli_toolbox_generator.Builders.project_builder import ProjectStructure
from cli_toolbox_generator.Template_tools.template_scanner import TemplateScanner


class GeneratorWizard:
    def __init__(self):
        self.state = WizardState()
        self.templates_root = Path(__file__).resolve().parent.parent / "templates"
        self.scanner = TemplateScanner(self.templates_root)

    def step_project_name(self):
        print_title("STEP 1 — Project Identity")
        self.state.cli_name = input("Project name [MyCLI]: ").strip() or "MyCLI"
        clear_screen()
        print_success(f"Project named: {self.state.cli_name}\n")

    def step_navigation(self):
        print_title("STEP 2 — Navigation Style")
        input("Press Enter to choose...")

        choice = select(
            "Select navigation style:",
            ["Numbers (1/2/3)", "Arrows (↑/↓ + ENTER)"],
        )
        if not choice:
            Aborter.abort()

        self.state.nav_style = "numbers" if choice.startswith("Numbers") else "arrows"  # type: ignore
        clear_screen()
        print_success(f"Navigation: {self.state.nav_style}\n")

    def step_arrow_style(self):
        if self.state.nav_style != "arrows":
            self.state.arrow_style = "pointer"
            return

        print_title("STEP 2.5 — Highlight Style")
        input("Press Enter to continue...")

        mapping = {
            "reverse": "bar",
            "underline": "underline",
            "bracketed": "bracket",
            "pointer": "pointer",
        }

        choice = select(
            "Select arrow highlight style:",
            list(mapping.keys()),
        )
        if not choice:
            Aborter.abort()
        self.state.arrow_style = mapping[choice]

        clear_screen()
        print_success(f"Highlight: {self.state.arrow_style}\n")

    def step_ui_style(self):
        print_title("STEP 3 — UI Style")
        input("Press Enter to choose...")

        choice = select("Select UI formatting:", ["clean", "minimal", "box"])
        if not choice:
            Aborter.abort()

        self.state.style = choice
        clear_screen()
        print_success(f"UI style: {self.state.style}\n")

    def _discover_optional_features(self) -> dict[str, str]:
        features: dict[str, str] = {}

        for kind, feature_name, rel_path, tpl_path in self.scanner.discover():
            if kind != "optional":
                continue

            if feature_name in features:
                continue

            label = None
            meta = None
            for fname in ("FEATURE_INFO.txt", "FEATURE_INFO.md"):
                candidate = tpl_path.parent / fname
                if candidate.exists():
                    meta = candidate
                    break

            if meta:
                text = meta.read_text(encoding="utf-8").strip()
                if text:
                    label = text.splitlines()[0]

            if not label:
                label = feature_name.replace("_", " ").title()

            features[feature_name] = label

        return features

    def step_features(self):
        print_title("STEP 5 — Optional Features")

        optional_root = self.templates_root / "Optional"
        feature_map: dict[str, dict] = {}

        if optional_root.exists():
            for namespace_dir in optional_root.iterdir():
                if not namespace_dir.is_dir():
                    continue

                namespace = namespace_dir.name

                for item in namespace_dir.iterdir():
                    if item.is_dir():
                        folder = item.name
                        feature_key = f"{namespace}/{folder}"

                        feature_map[feature_key] = {
                            "label": folder.replace("_", " ").title(),
                            "docs": [],
                            "tpls": [],
                        }

                        for tpl in item.rglob("*.tpl"):
                            if tpl.name.lower().endswith(".md.tpl"):
                                feature_map[feature_key]["docs"].append(tpl)
                            else:
                                feature_map[feature_key]["tpls"].append(tpl)
                        continue

                    if item.is_file() and item.suffix == ".tpl":
                        stem = item.stem
                        if stem.lower().endswith(".md"):
                            continue

                        feature_key = f"{namespace}/{stem}"

                        feature_map[feature_key] = {
                            "label": stem.replace("_", " ").title(),
                            "docs": [],
                            "tpls": [item],
                        }

        feature_map = {k: v for k, v in feature_map.items() if v["tpls"]}

        if not feature_map:
            print_warning("No optional features found.")
            self.state.selected_features = {}
            self.state.feature_details = {}
            input("Press Enter to continue...")
            clear_screen()
            return

        labels = {k: v["label"] for k, v in feature_map.items()}

        selected = multi_select(
            "Choose optional features:",
            options_dict=labels,
        )
        if selected is None:
            Aborter.abort()

        self.state.selected_features = {k: (k in selected) for k in feature_map}

        self.state.feature_details = feature_map

        clear_screen()

    def step_output_dir(self):
        print_title("STEP 6 — Output Directory")

        default = os.path.join(os.getcwd(), "generated")

        while True:
            path = input(f"Save project where? [{default}]: ").strip() or default

            try:
                os.makedirs(path, exist_ok=True)
                self.state.out_dir = path
                break
            except Exception as e:
                print_error(f"Invalid path: {e}")

        clear_screen()
        print_success(f"Output directory: {self.state.out_dir}\n")

    def step_menu_tree(self):
        print_title("STEP 7 — Menu Builder")
        builder = MenuTreeBuilder()
        self.state.menu_tree = builder.build(self.state.cli_name)  # type: ignore

    def step_review(self):
        clear_screen()
        print_title("STEP 8 — Final Review")

        print_success(f"Project Name : {self.state.cli_name}")
        print_success(f"Navigation   : {self.state.nav_style}")
        print_success(f"UI Style     : {self.state.style}")
        print_success(f"Output Dir   : {self.state.out_dir}")
        print()

        print_title("Features")

        if not self.state.selected_features:
            print_warning("No optional features available.")
        else:
            enabled = [k for k, v in self.state.selected_features.items() if v]
            disabled = [k for k, v in self.state.selected_features.items() if not v]

            if enabled:
                print_success("Enabled:")
                for k in enabled:
                    label = self.state.feature_details[k]["label"]
                    print(f"  • {label}")
            else:
                print_warning("No features enabled.")

            if disabled:
                print("\nDisabled:")
                for k in disabled:
                    label = self.state.feature_details[k]["label"]
                    print(f"  • {label}")
        print()

        print_title("Menu Structure")
        if self.state.menu_tree:
            print(MenuTreeFormatter.format(self.state.menu_tree))  # type: ignore
        else:
            print_warning("No menu tree defined.")
        print()
        input("Press Enter to continue to project generation...")
        proceed = select("Generate project?", ["No", "Yes"])
        if proceed != "Yes":
            Aborter.abort(self.state.out_dir)

    def generate_project(self):
        out_mgr = OutputManager(self.state.out_dir, self.state.cli_name)  # type: ignore
        project_path = out_mgr.prepare()

        config = ProjectConfig(
            cli_name=self.state.cli_name,
            formatting_style=self.state.style,
            use_color=self.state.use_color,
            base_output_dir=self.state.out_dir,
            arrow_style=self.state.arrow_style,
            navigation_style=self.state.nav_style,
            features=self.state.selected_features,
            feature_details=self.state.feature_details,
        )

        builder = ProjectStructure(config)
        builder.generate_project(self.state.menu_tree, project_path)

        zip_path = out_mgr.zip_project()

        print_title("Generation Complete!")
        print_success(f"Project Folder: {project_path}")
        print_success(f"Zip Archive:   {zip_path}\n")

    def run(self):
        self.step_project_name()
        self.step_navigation()
        self.step_arrow_style()
        self.step_ui_style()
        self.step_features()
        self.step_output_dir()
        self.step_menu_tree()
        self.step_review()
        self.generate_project()
