# 📦 CLI Toolbox Generator

**A modular, template-driven generator for beautiful, structured Python
CLIs.** Generate ready-to-use command-line applications for Python in seconds using
the fully template-driven generator with zero boilerplate.

Looking for an example of this being used? Check the Documents/ !

------------------------------------------------------------------------

## 🚀 Features

-   **100% Template-Driven Output**\
    The final project structure is based entirely on `.tpl` files. There's no
    code writing needed.

-   **Core Templates (Always Included)**\
    Everything to run a complete CLI tool:

    -   UI helpers
    -   A full menu navigation system
    -   Utility functions
    -   Project structure

-   **Built-In Optional QoL Plugin Packs**\
    Usable immediately upon download. No setup required.\
    Includes optional features such as:
    
    -   basic logging tools
    -   data conversion assistance
    -   formatting add-ons
    -   screen/spacing helpers
    -   layout utilities

        Simply toggle them during generator setup.

-   **Full Customization During Generation**\
    The generator prompts for:

    -   CLI name
    -   Menu structure
    -   Number of menus
    -   Nested menu trees
    -   Single & multi-command stubs
    -   Navigation style
    -   Optional features to include

        These settings fully shape the output directory.

-   **Automatic Menu Tree Generation**\
    Based on user input, the generator creates:

    -   menu directories
    -   menu classes
    -   navigation logic
    -   stubs for each menu option

        The stubs act as placeholders where you add your
        project-specific code either directly or as a method call.

-   **Zero External Dependencies**\
    No external libraries required.
    
    The generated projects run on standard Python installations.

-   **Fully Ready on Download**\
    This repository is complete and usable as-is.
    
    No pre-configuration, environment customization, or template
    authoring required.

------------------------------------------------------------------------

## 📂 Template System (In 20 Seconds)

    templates/
        Core/                 
            utilities/
            ui/
            menu/
            main/
            documentation/
            debug/
        Optional/             
            colors/
            debug/
            qol/

Adding a file is as simple as:

    templates/Core/ui/input_utils.py.tpl
    → ui/input_utils.py

------------------------------------------------------------------------

## 🧠 Why I Made This

I love building small systems, prototypes, data tools, utilities, workflow
helpers, etc.\
But every time I start a new project, I spend way too long rebuilding:

-   a good-looking CLI
-   a reasonable folder structure
-   usable utilities
-   input helpers
-   clean menus and submenus
-   debug helpers
-   formatting consistency

It always eats time before I can work on the part I *actually* care
about. While a CLI isn't necessary, it helps me visualize my systems and
properly test them out.

Eventually I realized:

> "I'm rebuilding the same CLI scaffolding over and over again. Surely I can just
> automate this..."

This project is the result:

A **modular, template-first generator** that creates a fully structured
CLI project with:

-   a working navigation system
-   menu trees
-   helper utilities
-   optional QoL modules
-   ready-to-fill action stubs

You can use it once for a single project, or shape it into your personal
CLI framework for years of small tools. Have a must-have file for every project?
Drop it in here and use it for everything! Got some utilities that are good for
some projects but bad for others? Throw it into an Optional section! This project
is not revolutionary nor inherently that complex, but it is a nice tool.

------------------------------------------------------------------------

# 📘 What the Generator Actually Produces

Depending on your choices during setup, the generator builds:

------------------------------------------------------------------------

## ✔ Dynamic Menu Trees

If you specify multiple menus or submenus, the generator creates:

    menus/
        main_menu.py
        tools_menu.py
        system_menu.py

The generator handles the distinction, connection, and loading itself. No need
to worry about tying these together even if they are sub-menus!

------------------------------------------------------------------------

## ✔ Menu Option Stubs (Where You Add Your Logic)

Each menu contains placeholder methods such as:

``` python
def option_one(self):
    print("TODO: implement option one")
```

You simply fill in your logic after generation. The print is simply there to
let you test out your menu and ensure it works on generation.

------------------------------------------------------------------------

## ✔ UI Manager

    ui/
        ui_manager.py

Our manager takes care of everything for your menu's to work cleanly based off
your selected preferences.

------------------------------------------------------------------------

## ✔ Utility Modules

    utilities/
        display.py
        formatting.py
        input.py
        multi_command.py
        navigation.py
        system.py

These modules provide you with some nice general utilities while also helping
the menus and navigation work well.

------------------------------------------------------------------------

## ✔ Pre-installed (Optional) QoL Features

A few of my favorites built in should you choose to enable them:

    CLI_Text_Extras/
    Data_Conversion_Tools/
    Logging_Tools/
    System_Util_Extras/

Includes helpers like:
- ascii art assistance & ui customization options
- dealing with JSON and dictionary conversions as well as CSVs
- logging helpers to keep things consistent, organized, and pretty
- system helpers for timers, sleeping, directory/file checks, etc.
- spacing and borders

------------------------------------------------------------------------

## ✔ Documentation and Main Entrypoint

    main.py
    documentation/
        README.md

------------------------------------------------------------------------

## 🛠 Installation

``` bash
git clone https://github.com/Urason-Anorsu/CLI-Toolbox-Generator.git
cd cli-toolbox-generator
python cli_gen.py
```

------------------------------------------------------------------------

## 🎨 Customization

During generation, you can select:

-   CLI name
-   description
-   navigation style
-   menu layout
-   submenu depth
-   optional feature packs

All shape the final output.

To customize even further, modify files under:

    templates/Core/
    templates/Optional/<feature>/

------------------------------------------------------------------------

## 🤝 Contributing

PRs are welcome! Although I'm unsure what could be added.\
You can add:

-   new feature packs
-   menu templates
-   QoL helpers
-   documentation additions

------------------------------------------------------------------------

## 📄 License

MIT License.

------------------------------------------------------------------------

## ❤️ Attribution

This project uses the MIT License, so attribution is not required.  
But if you build something cool from this toolkit, a link back or shoutout would be greatly appreciated!
Regardless, happy building! I hope this saves you some time.

------------------------------------------------------------------------

## 🗺️ Road-Map

While I don't think I'll make large changes to this project, here is a basic
road-map of things I'd love to add:

-   dynamic terminal sizing for compatibility
-   more customization options for navigation & formatting
-   pre-built templates for different project types
-   better dynamic loading for less bloat (specifically with navigation features)
-   language generation selection (Java, Lua, etc.)
-   proper pip-integration for easy one-offs 
-   user selection of programming paradigm preference
-   usage of user defined variables for dynamic replacement in templates
