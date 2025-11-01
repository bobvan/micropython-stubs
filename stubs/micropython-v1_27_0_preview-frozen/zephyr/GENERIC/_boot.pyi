from _typeshed import Incomplete

FlashArea: Incomplete
DiskAccess: Incomplete
_FLASH: str
_FLASH_LIB: str
_STORAGE_KEY: str
_FLASH_EXISTS: bool

def create_flash_partition():
    """Create an LFS2 filesystem on the partition labeled storage
    and mount it on /flash.
    Return True if successful, False otherwise.
    """

def mount_all_disks():
    """Now mount all the DiskAreas (if any)."""
