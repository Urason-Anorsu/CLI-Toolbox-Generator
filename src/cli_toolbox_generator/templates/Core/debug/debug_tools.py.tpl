from utilities.display import print_success, print_error

def dump_environment():
    """Show environment diagnostics."""
    import os, sys
    print_success("Environment Diagnostics:")
    print("Python:", sys.version)
    print("CWD:", os.getcwd())

def list_installed_packages():
    """List installed pip packages."""
    try:
        import pkg_resources
        print_success("Installed Packages:")
        for pkg in pkg_resources.working_set:
            print(f" - {pkg.project_name} {pkg.version}")
    except Exception as e:
        print_error(f"Error: {e}")
