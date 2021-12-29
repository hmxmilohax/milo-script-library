#  Copyright (c) 1999-2000  Harmonix Music Systems  All rights reserved

import os
import os.path
import hx

# prepends the root path to the given relative path.
def get_absolute_path (relative):
    return os.path.join (root, relative)

# Default root is current directory
root = hx.get_freq_root()

# load up all standard python stuff for freq:
execfile (get_absolute_path ('global/defaults.py'), globals())
