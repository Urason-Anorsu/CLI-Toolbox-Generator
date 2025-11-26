from dataclasses import dataclass, field
from typing import Dict, Any

# Default feature flags (remember to never change this dict directly)
DEFAULT_FEATURES = {
    "ui_extras": False,
    "converters": False,
    "system_utils": False,
    "logging": False,
    "ascii_art": False,
    "error_logging": False,
}


@dataclass
class ProjectConfig:
    cli_name: str
    formatting_style: str
    use_color: bool
    base_output_dir: str
    arrow_style: str
    navigation_style: str = "numbers"

    # Simple bool feature flags
    features: Dict[str, bool] = field(default_factory=lambda: DEFAULT_FEATURES.copy())

    # Rich metadata for each feature (wizard-created)
    feature_details: Dict[str, Dict[str, Any]] = field(default_factory=dict)

    # Helpers
    def is_enabled(self, feature: str) -> bool:
        return self.features.get(feature, False)

    def enable(self, feature: str):
        self.features[feature] = True

    def disable(self, feature: str):
        self.features[feature] = False

    def validate(self):
        if self.navigation_style not in ("numbers", "arrows"):
            raise ValueError("navigation_style must be 'numbers' or 'arrows'")

        if self.formatting_style not in ("clean", "box", "minimal"):
            raise ValueError("formatting_style must be one of: clean, box, minimal")

        return True

    def summary(self):
        enabled = [name for name, v in self.features.items() if v]

        return {
            "cli_name": self.cli_name,
            "style": self.formatting_style,
            "navigation": self.navigation_style,
            "enabled_features": enabled,
            "feature_details": self.feature_details,
        }
