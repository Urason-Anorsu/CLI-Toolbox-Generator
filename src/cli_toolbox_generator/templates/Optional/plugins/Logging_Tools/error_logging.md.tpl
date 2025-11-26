## ❗ Error Logging & Exception Wrapper

This feature provides decorators and helpers that let you wrap functions
with automatic error catching, logging, and user-friendly messaging.

### Basic Usage

```python
from utilities.error_logging import safe_run

@safe_run
def risky_operation():
    1 / 0
```

### Output Example

```
[ERROR] risky_operation failed: division by zero
```

### Manual Logging

```python
from utilities.error_logging import log_error

try:
    do_something()
except Exception as e:
    log_error("Something exploded!", e)
```

This keeps debugging painless without exposing ugly stack traces to end‑users.
