from .debug_inspector import list_debug_hooks, list_tools
from utilities.display import print_success, print_error

def run_debug_menu(ui, menus, current_menu):
    while True:
        ui.clear()
        print("=== Debug Mode ===\n")

        print("1) Run Debug Hooks")
        print("2) Inspect All Menus")
        print("3) Inspect Current Menu")
        print("4) Debug Tools")
        print("0) Exit Debug Mode\n")

        choice = input("> ").strip()

        # Exit debug mode
        if choice == "0":
            return

        # Run hooks
        elif choice == "1":
            hooks = list_debug_hooks()
            if not hooks:
                print_error("No hooks defined.")
            else:
                for name, fn in hooks:
                    print_success(f"Running hook: {name}")
                    try:
                        fn()
                    except Exception as e:
                        print_error(f"Error running {name}: {e}")
            input("\nPress Enter to continue...")

        # Inspect menu tree
        elif choice == "2":
            print_success("Registered Menus:")
            for key in menus:
                print(f" - {key}")
            input("\nPress Enter to continue...")

        # Inspect current menu
        elif choice == "3":
            print_success(f"Inspecting: {current_menu.__class__.__name__}")
            for attr in dir(current_menu):
                if attr.startswith("cmd_"):
                    print(f"  Command: {attr}")
            input("\nPress Enter to continue...")

        # Tools
        elif choice == "4":
            tools = list_tools()
            if not tools:
                print_error("No debug tools defined.")
            else:
                for name, fn in tools:
                    print_success(f"Running tool: {name}")
                    try:
                        fn()
                    except Exception as e:
                        print_error(f"Tool {name} failed: {e}")
            input("\nPress Enter to continue...")
