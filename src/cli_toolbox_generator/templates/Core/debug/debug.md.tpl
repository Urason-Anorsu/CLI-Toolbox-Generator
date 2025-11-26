## 🐞 Debug Toolkit

Enables the optional `debug/` package with:

- `tools.py` — menu tree inspection functions  
- `inspector.py` — auto-discovers available debug hooks  
- `hooks.py` — where YOU add your custom debug functions  

### Activation

Inside your CLI, enter:

```
-1
```

to enter Debug Mode.

Each function defined in `debug/hooks.py` will be detected and run automatically.
