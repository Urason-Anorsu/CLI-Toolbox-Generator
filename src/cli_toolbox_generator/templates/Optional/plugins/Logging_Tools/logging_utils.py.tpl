# Lightweight Logging Utilities
import datetime
import os

LOG_LEVELS = ["DEBUG", "INFO", "WARN", "ERROR"]

def _timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log(message, level="INFO"):
    """
    Print a formatted log message.
    
    Example:
        log("Something happened")
        log("Something broke", level="ERROR")
    """
    level = level.upper()
    if level not in LOG_LEVELS:
        level = "INFO"

    ts = _timestamp()
    print(f"[{ts}] [{level}] {message}")

# File Logger Helpers
def log_to_file(message, path="logs/app.log", level="INFO"):
    """
    Append a log entry to a file, creating directories automatically.
    """
    level = level.upper()
    if level not in LOG_LEVELS:
        level = "INFO"

    ts = _timestamp()
    folder = os.path.dirname(path)

    if folder and not os.path.exists(folder):
        os.makedirs(folder)

    try:
        with open(path, "a", encoding="utf-8") as f:
            f.write(f"[{ts}] [{level}] {message}\n")
    except Exception as e:
        print(f"[LOG ERROR] Unable to write to '{path}': {e}")

# Combined Logger (print + file)
def log_both(message, path="logs/app.log", level="INFO"):
    log(message, level=level)
    log_to_file(message, path=path, level=level)
