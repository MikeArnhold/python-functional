"""Pipe"""

from typing import Callable, Generic, TypeVar

T1 = TypeVar("T1")
T2 = TypeVar("T2")
T3 = TypeVar("T3")


class PipeUnary(Generic[T1, T2]):
    """Pipe

    Thenable function composition via pipe method.
    All parameters must be unary.
    """

    def __init__(self, func: Callable[[T1], T2]):
        self.func = func

    def __call__(self, value: T1) -> T2:
        return self.func(value)

    def pipe(self, func: Callable[[T2], T3]) -> "PipeUnary[T1, T3]":
        """Enque the next callable"""

        def local_pipe(value: T1) -> T3:
            return func(self(value))

        return PipeUnary(local_pipe)


def pipe_unary(func: Callable[[T1], T2]) -> PipeUnary[T1, T2]:
    """Return new PipeUnary object"""
    return PipeUnary(func)
