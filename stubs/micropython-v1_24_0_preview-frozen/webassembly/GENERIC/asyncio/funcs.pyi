from . import core as core
from _typeshed import Incomplete
from collections.abc import Generator

async def _run(waiter, aw) -> None: ...
async def wait_for(aw, timeout, sleep=...): ...
def wait_for_ms(aw, timeout): ...

class _Remove:
    @staticmethod
    def remove(t) -> None: ...

def gather(*aws, return_exceptions: bool = False) -> Generator[None, None, Incomplete]: ...