## 🔄 Data Converters

This module provides lightweight, safe helpers for working with JSON, CSV,
and number/string conversions.

### JSON Helpers

```python
from utilities.data_convert import json_to_dict, dict_to_json

data = json_to_dict("config.json")
dict_to_json(data, "backup.json")
```

### CSV Helpers

```python
from utilities.data_convert import csv_to_rows, rows_to_csv

rows = csv_to_rows("data.csv")
rows_to_csv(rows, "output.csv")
```

### Type Conversion Helpers

```python
from utilities.data_convert import to_int, to_float, is_numeric, round_decimal

value = to_float("4.2")
rounded = round_decimal(3.14159, 3)
```

These utilities are simple, predictable, and easy to modify for custom pipelines.
