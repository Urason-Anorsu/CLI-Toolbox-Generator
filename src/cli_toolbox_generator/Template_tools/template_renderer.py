from pathlib import Path
import re


class TemplateRenderer:
    pattern = re.compile(r"{{\s*([a-zA-Z0-9_]+)\s*}}")

    def __init__(self, template_folder):
        self.template_folder = Path(template_folder).resolve()

        if not self.template_folder.exists():
            raise FileNotFoundError(
                f"Template folder not found: {self.template_folder}"
            )

    def load(self, filename):
        path = self.template_folder / filename
        if not path.exists():
            raise FileNotFoundError(f"Template not found: {path}")
        return path.read_text(encoding="utf-8")

    def render(self, filename, context):
        text = self.load(filename)

        def replace(match):
            key = match.group(1)
            return str(context.get(key, match.group(0)))

        return self.pattern.sub(replace, text)
