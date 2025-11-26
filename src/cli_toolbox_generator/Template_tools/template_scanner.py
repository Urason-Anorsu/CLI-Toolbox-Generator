from pathlib import Path


class TemplateScanner:
    def __init__(self, template_root):
        self.template_root = Path(template_root).resolve()
        self.core_root = self.template_root / "Core"
        self.optional_root = self.template_root / "Optional"
        self.internal_root = self.template_root / "Internal_Templates_NotReg"

    # Ensure We Skip Internal Templates
    def _is_internal(self, tpl_path: Path) -> bool:
        try:
            tpl_path.relative_to(self.internal_root)
            return True
        except ValueError:
            return False

    # Core Template Discovery
    def discover(self):
        """
        Yields:
            kind      → "core"
            feature   → None
            rel_path  → Path under Core/ (still has .tpl)
            tpl_path  → absolute Path
        """
        if self.core_root.exists():
            for tpl_path in self.core_root.rglob("*.tpl"):
                if self._is_internal(tpl_path):
                    continue

                rel = tpl_path.relative_to(self.core_root)
                yield ("core", None, rel, tpl_path)
