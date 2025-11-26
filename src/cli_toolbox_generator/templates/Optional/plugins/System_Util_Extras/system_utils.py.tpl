# System Utilities & Helpers

import os
import time
from contextlib import contextmanager

# Directory Helpers
def safe_mkdir(path):
    """Create a directory recursively if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def ensure_file(path):
    """Ensure the parent directory of a file exists."""
    folder = os.path.dirname(path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)

# Timing / Benchmarking
@contextmanager
def timer(label="Task"):
    """
    Context manager that prints how long a block takes.
    
    Usage:
        with timer("Processing"):
            do_something()
    """
    start = time.time()
    yield
    end = time.time()
    print(f"{label} took {end - start:.4f}s")

# Sleeping Helpers
def sleep(seconds):
    time.sleep(seconds)

# File & System Checks
def file_exists(path):
    return os.path.isfile(path)

def folder_exists(path):
    return os.path.isdir(path)

# Environment Helpers
def get_env(name, default=None):
    return os.environ.get(name, default)
