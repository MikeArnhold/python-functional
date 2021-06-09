"""Pipe"""
from functools import partial
from typing import Any, Callable, Generic, TypeVar

T1 = TypeVar("T1")
T2 = TypeVar("T2")
T3 = TypeVar("T3")


class PipeUnary(Generic[T1, T2]):
    """Pipe

    Thenable function composition via pipe method.
    All callbacks must be unary.
    """

    def __init__(self, func: Callable[[T1], T2]) -> None:
        self.func = func

    def __call__(self, value: T1) -> T2:
        return self.func(value)

    def pipe(self, func: Callable[[T2], T3]) -> "PipeUnary[T1, T3]":
        """Enque the next callable"""

        def local_pipe(value: T1) -> T3:
            return func(self(value))

        return PipeUnary(local_pipe)


class PipeArbitrary(Generic[T1]):
    """Pipe

    Thenable function composition via pipe method.
    First callback can be arbitrary. Other callbacks must be unary.
    """

    def __init__(self, func: Callable[..., T1]) -> None:
        self.func = func

    def __call__(self, *args: Any, **kwargs: Any) -> T1:
        return self.func(*args, **kwargs)

    def pipe(self, func: Callable[[T1], T2]) -> "PipeArbitrary[T2]":
        """Enque the next callable"""

        def local_pipe(*args: Any, **kwargs: Any) -> T2:
            return func(self(*args, **kwargs))

        return PipeArbitrary(local_pipe)


pipe_unary = partial(PipeUnary)
pipe_arbitrary = partial(PipeArbitrary)
