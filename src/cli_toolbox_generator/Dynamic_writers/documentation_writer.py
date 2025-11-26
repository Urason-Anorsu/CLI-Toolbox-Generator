from pathlib import Path
from datetime import datetime
from cli_toolbox_generator.Template_tools.template_writer import TemplateWriter


class DocumentationWriter:
    def __init__(self, template_root="src/cli_toolbox_generator/templates"):
        self.template_root = Path(template_root)
        self.template_writer = TemplateWriter(template_root)

        self.internal_root = self.template_root / "Internal_Templates_NotReg"

        self.core_usage_template = self.internal_root / "USAGE_GUIDE.md.tpl"

    # Write Documentation
    def write(self, project_root: str | Path, project_name: str, config):
        project_root = Path(project_root)
        date = datetime.now().strftime("%Y-%m-%d")

        # Load optional feature documentation
        plugin_docs_raw = []

        for feature_key, enabled in config.features.items():
            if not enabled:
                continue

            details = config.feature_details.get(feature_key)
            if not details:
                continue

            for entry in details.get("templates", []):
                tpl_path = entry.get("tpl_path")
                if tpl_path and tpl_path.suffix == ".md.tpl":
                    text = tpl_path.read_text(encoding="utf-8").strip()
                    plugin_docs_raw.append(text)

        plugin_docs = (
            "\n\n---\n\n".join(plugin_docs_raw)
            if plugin_docs_raw
            else "*No optional features enabled.*"
        )

        # Validate USAGE GUIDE location
        core_tpl = self.core_usage_template
        if not core_tpl.exists():
            raise FileNotFoundError(
                "SYSTEM TEMPLATE MISSING:\n"
                f"Expected USAGE_GUIDE.md.tpl at:\n{core_tpl}\n\n"
                "Because all dynamic system-level templates must live in:\n"
                "templates/Internal_Templates_NotReg/"
            )

        # Render the final documentation
        return self.template_writer.write(
            template_path=core_tpl,
            target_project_root=project_root,
            output_rel="USAGE_GUIDE.md",
            project_name=project_name,
            date=date,
            plugin_docs=plugin_docs,
        )
