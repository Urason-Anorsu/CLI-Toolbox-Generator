## 🧰 Extended UI Helpers

The UI Extras package adds higher-level formatting and input helpers to your CLI.

### Display helpers

```python
from utilities.ui_extras import banner, hr, title_block, section
```

- `banner("Title")` — ASCII banner block  
- `title_block("Section")` — larger header block  
- `section("Name")` — simple section label  
- `hr()` — horizontal rule  

### Input helpers

```python
from utilities.ui_extras import ask_yes_no, ask_int, ask_choice, select_from_list
```

- `ask_yes_no("Continue?")`  
- `ask_int("Enter amount")`  
- `ask_choice("Pick one:", ["A", "B", "C"])`  
- `select_from_list(items)` — numbered selector  

### Progress Bars

```python
from utilities.ui_extras import progress, progress_bar

for i in range(101):
    progress(i/100)
```

```python
for item in progress_bar(my_list):
    ...
```

Great for tracking long operations visibly.
