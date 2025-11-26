## ⚙️ System Utilities

Provides safe, lightweight wrappers for common system-level operations.

### Safe Directory Creation

```python
from utilities.sys_utils import safe_mkdir

safe_mkdir("logs")
safe_mkdir("exports")
```

### Timer Utility

```python
from utilities.sys_utils import timer

with timer("Processing"):
    perform_task()
```

Outputs:

```
[Processing] started...
[Processing] finished in 0.42s
```

Useful for debugging performance or profiling your CLI workflows.
