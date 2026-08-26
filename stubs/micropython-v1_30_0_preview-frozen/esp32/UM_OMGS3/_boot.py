# Micropython v1.30.0-preview frozen stubs
import gc

import vfs
from flashbdev import bdev

try:
    if bdev:
        vfs.mount(bdev, "/")
except OSError:
    import inisetup

    inisetup.setup()

gc.collect()
