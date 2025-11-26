from ui.ui_manager import UIManager
{{menu_imports}}

PARENTS = {
{{parent_dict}}
}

def build_menus(ui):
    menus = {}
{{menu_builder}}
    return menus

def main():
    ui = UIManager(
        navigation_mode="{{navigation_style}}",
        style="{{formatting_style}}",
        arrow_style="{{arrow_style}}"
    )

    menus = build_menus(ui)
    current = "{{root_slug}}"

    while current is not None:
        menu = menus.get(current)
        if not menu:
            print(f"Invalid menu: {current}")
            break

        result = menu.handle()

        if result == "__back__":
            current = PARENTS.get(current)
            continue

        if isinstance(result, str) and result in menus:
            current = result
            continue

        if result == "-1":
            from debug.debug_menu import run_debug_menu
            run_debug_menu(ui, menus, menu)
            continue



if __name__ == "__main__":
    main()
