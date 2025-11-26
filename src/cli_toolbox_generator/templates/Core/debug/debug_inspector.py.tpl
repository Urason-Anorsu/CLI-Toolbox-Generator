import debug.debug_hooks as hooks
import debug.debug_tools as tools

def list_debug_hooks():
    funcs = []
    for name in dir(hooks):
        if name.startswith("_"):
            continue
        fn = getattr(hooks, name)
        if callable(fn):
            funcs.append((name, fn))
    return funcs

def list_tools():
    funcs = []
    for name in dir(tools):
        if name.startswith("_"):
            continue
        fn = getattr(tools, name)
        if callable(fn):
            funcs.append((name, fn))
    return funcs
