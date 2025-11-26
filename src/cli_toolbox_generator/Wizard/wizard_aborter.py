import os
import shutil
from cli_toolbox_generator.Utilities.ui_tools import clear_screen, print_warning, print_error


class Aborter:
    @staticmethod
    def abort(path=None):
        clear_screen()

        if path and os.path.exists(path):
            try:
                shutil.rmtree(path)
                print_warning(f"Cancelled — removed unfinished project:\n{path}\n")
            except Exception as e:
                print_error(f"Could not remove directory: {e}")
        else:
            print_warning("Generation cancelled.\n")

        exit(0)
