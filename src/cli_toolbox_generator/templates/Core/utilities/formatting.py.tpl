# Basic reusable wrappers for text formatting

def header_clean(text):
    print("\n" + text)
    print("-" * len(text))


def header_box(text):
    line = "=" * (len(text) + 6)
    print("\n" + line)
    print(f"== {text} ==")
    print(line)


def header_minimal(text):
    print(f"\n=== {text} ===")
