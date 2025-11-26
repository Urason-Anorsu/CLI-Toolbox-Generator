"""
Auto-generated multi-select command helper.

HOW TO USE THIS FILE:

1. Add/edit the OPTIONS list inside build_options().
2. Add your logic for processing selections inside run_selected().
3. Leave everything below 'DO NOT EDIT BELOW' unchanged.

Supports BOTH:
    • Number-based multi-select (1,3-5)
    • Arrow-based checkbox UI (↑/↓ + SPACE + ENTER)

Selection mode automatically follows your global UI settings.
"""


class MultiCommand:

    def __init__(self, ui):
        """
        ui: instance of UIManager (handles UI + navigation)
        """
        self.ui = ui

    # Define selectable options
    def build_options(self):
        """
        Return list[str] of items to choose from.

        Examples:
            return ["Alpha", "Beta", "Gamma"]
        """

        OPTIONS = [
            # TODO: Add your selectable items here:
            "Option A",
            "Option B",
            "Option C",
        ]
        return OPTIONS

    # Handle the chosen items
    def run_selected(self, chosen_items):
        """
        chosen_items: list[str]

        Replace this with your own logic.
        """

        # TODO: Implement your custom multi-select behavior
        self.ui.clear()
        print("You selected:")
        for item in chosen_items:
            print(" -", item)

        self.ui.pause("Press Enter to return...")
        return

    # DO NOT EDIT BELOW THIS LINE
    def handle(self):
        """
        Entry point used by the generated menu system.
        Uses UIManager.choose_multi() so the UI style and navigation
        (numbers vs arrows) is *automatically* respected.
        """
        options = self.build_options()

        # Let UIManager handle all display/UI logic
        chosen_labels = self.ui.choose_multi(options)

        return self.run_selected(chosen_labels)
