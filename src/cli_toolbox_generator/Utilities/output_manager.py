from pathlib import Path
import shutil


class OutputManager:
    def __init__(self, base_dir: str, project_name: str):
        self.base_dir = Path(base_dir).expanduser().resolve()
        self.project_name = project_name
        self.project_path = self.base_dir / project_name

    def prepare(self, clear_existing=False):
        if clear_existing and self.project_path.exists():
            shutil.rmtree(self.project_path)
        self.project_path.mkdir(parents=True, exist_ok=True)
        return self.project_path

    def zip_project(self):
        zip_path = self.base_dir / f"{self.project_name}.zip"
        shutil.make_archive(
            base_name=str(zip_path.with_suffix("")),
            format="zip",
            root_dir=str(self.project_path),
        )
        return zip_path
