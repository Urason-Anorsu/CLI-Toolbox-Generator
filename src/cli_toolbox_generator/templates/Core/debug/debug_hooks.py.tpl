# Example debug hooks.
# Add your own functions here.
# They will automatically appear in Debug Mode → Run Debug Hooks.

def sample_hook():
    print("Sample debug hook executed!")


def environment_check():
    import sys
    print("Python Version:", sys.version)
