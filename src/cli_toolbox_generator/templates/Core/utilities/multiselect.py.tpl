# This file remains only so older templates referencing
# `utilities.multiselect` do not crash.

from utilities.navigation import (
    arrow_multiselect_core,
    parse_number_multiselect as parse_number_multiselect_core,
)

def arrow_multiselect(labels):
    
    return arrow_multiselect_core(
        labels,
        use_color=False,
        style="pointer",
        debug_enabled=False,
    )

def parse_number_multiselect(raw, max_index):
    return parse_number_multiselect_core(raw, max_index)
