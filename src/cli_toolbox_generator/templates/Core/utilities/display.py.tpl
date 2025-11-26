from utilities.system import clear_screen

# ANSI Color Codes
RESET = "\033[0m"

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
WHITE = "\033[37m"


# Generic color formatter
def color_text(text, color):
    """Wrap text in ANSI color codes."""
    return f"{color}{text}{RESET}"


# Convenience wrappers for readability
def print_success(msg):
    print(color_text(f"[SUCCESS] {msg}", GREEN))


def print_error(msg):
    print(color_text(f"[ERROR] {msg}", RED))


def print_warning(msg):
    print(color_text(f"[WARNING] {msg}", YELLOW))


def pause(message="Press Enter to continue..."):
    input(message)
