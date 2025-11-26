from pathlib import Path


def discover_optional_features(optional_root: Path) -> dict[str, Path]:
    features: dict[str, Path] = {}

    if not optional_root.exists():
        return features

    for tpl_path in optional_root.rglob("*.tpl"):
        # Skip internal or special files
        if tpl_path.name.startswith("_") or tpl_path.name.startswith("__"):
            continue

        # Feature name derived from filename
        # Ex: "ascii_art.py.tpl" → "ascii_art"
        name = tpl_path.name.replace(".tpl", "")
        if name.endswith(".py"):
            name = name[:-3]

        features[name] = tpl_path

    return features
