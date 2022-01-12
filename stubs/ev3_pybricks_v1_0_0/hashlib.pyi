from typing import Any

_sha224: Any
_sha256: Any
_sha384: Any
_sha512: Any

def init() -> None: ...
def new() -> None: ...

class sha1:
    def digest() -> None: ...
    def update() -> None: ...

class sha224:
    block_size: int
    def copy() -> None: ...
    def digest() -> None: ...
    digest_size: int
    digestsize: int
    def hexdigest() -> None: ...
    def update() -> None: ...

class sha256:
    def digest() -> None: ...
    def update() -> None: ...

class sha384:
    block_size: int
    def copy() -> None: ...
    def digest() -> None: ...
    digest_size: int
    digestsize: int
    def hexdigest() -> None: ...
    def update() -> None: ...

class sha512:
    block_size: int
    def copy() -> None: ...
    def digest() -> None: ...
    digest_size: int
    digestsize: int
    def hexdigest() -> None: ...
    def update() -> None: ...

uhashlib: Any