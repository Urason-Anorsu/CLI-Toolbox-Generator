# Error Logging & Exception Handling Helpers
import traceback
import datetime
import os

# Crash Log Writer
def _ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def write_crash_log(exception, log_dir="logs"):
    """
    Writes a crash log with timestamp and traceback.
    Returns the path to the log file.
    """
    _ensure_dir(log_dir)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"crash_{timestamp}.log"
    full_path = os.path.join(log_dir, filename)

    with open(full_path, "w", encoding="utf-8") as f:
        f.write("=== CRASH LOG ===\n")
        f.write(f"Timestamp: {timestamp}\n\n")
        f.write("Exception:\n")
        f.write(str(exception) + "\n\n")
        f.write("Traceback:\n")
        f.write("".join(traceback.format_exc()))

    return full_path

# Decorator: safe_execute
def safe_execute(fn):
    """
    A decorator that wraps any function in a try/except,
    logs errors, and prints a clean message.
    """
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)

        except Exception as e:
            log_path = write_crash_log(e)
            print("An error occurred while running this command.")
            print(f"Crash log saved to: {log_path}")

            # Re-raise for debugging OR suppress?
            # Comment out the next line to suppress exceptions:
            # raise e

            return None

    return wrapper

# try_run helper
def try_run(callable_fn, *args, **kwargs):
    """
    Runs a callable and logs any errors that occur.
    Use for functions that should NOT crash the program.
    """
    try:
        return callable_fn(*args, **kwargs)

    except Exception as e:
        path = write_crash_log(e)
        print(f"Error logged to: {path}")
        return None
