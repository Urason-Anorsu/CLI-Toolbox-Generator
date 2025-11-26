from pathlib import Path
import re


class TemplateWriter:
    _pattern = re.compile(r"{{\s*([a-zA-Z0-9_]+)\s*}}")

    def __init__(self, template_root):
        self.template_root = Path(template_root).resolve()

    def _render_dynamic(self, template_path: Path, context: dict) -> str:
        text = template_path.read_text(encoding="utf-8")

        def replace(match):
            key = match.group(1)
            return str(context.get(key, match.group(0)))

        return self._pattern.sub(replace, text)

    def write(self, template_path, target_project_root, output_rel=None, **context):
        template_path = Path(template_path).resolve()
        target_project_root = Path(target_project_root).resolve()

        raw_text = template_path.read_text(encoding="utf-8")

        is_dynamic = bool(self._pattern.search(raw_text))
        rendered = (
            self._render_dynamic(template_path, context) if is_dynamic else raw_text
        )

        # Compute output path IF caller didn't override it
        if output_rel is None:
            rel = template_path.relative_to(self.template_root)
            parts = list(rel.parts)

            # Strip only Core/ or only Optional/
            if parts[0].lower() == "core":
                parts = parts[1:]
            elif parts[0].lower() == "optional":
                parts = parts[1:]
                # Do NOT remove the next folder (it's the output folder!)

            # Remove .tpl suffix
            rel_no_tpl = Path(*parts).with_suffix("")
            output_rel = rel_no_tpl.as_posix()

        # Write to disk
        out_path = target_project_root / output_rel
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(rendered, encoding="utf-8")

        return out_path
