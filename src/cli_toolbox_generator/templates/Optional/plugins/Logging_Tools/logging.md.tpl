## 📝 Lightweight Logging

A minimal structured logging helper that prints readable log statements
without requiring any external dependencies.

### Usage

```python
from utilities.logging_utils import log

log("Application started")
log("Processing item...", level="INFO")
log("Something went wrong", level="ERROR")
```

### Output Example

```
[INFO] Application started
[INFO] Processing item...
[ERROR] Something went wrong
```

This keeps your CLI output consistent and easy to scan during long operations.
