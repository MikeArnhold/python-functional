"""Tests"""
from unittest import TestCase
from pipe import PipeUnary, pipe_unary


class PipeUnaryClasTests(TestCase):
    """test Pipe class"""

    def test_init(self) -> None:
        """init func first in pipe"""

        def double(value: int) -> int:
            return value * 2

        stack = PipeUnary(double)

        self.assertEqual(4, stack(2))

    def test_2nd(self) -> None:
        """pipes 2 funcs"""

        def double(value: int) -> float:
            return float(value * 2)

        def to_string(value: float) -> str:
            return str(value)

        stack = PipeUnary(double).pipe(to_string)

        self.assertEqual(str(float(42)), stack(21))


class PipeUnaryFuncTests(TestCase):
    """test pipe function"""

    def test_pipe(self) -> None:
        """return Pipe object"""

        def double(_: int) -> float:
            raise NotImplementedError()

        stack = pipe_unary(double)

        self.assertTrue(isinstance(stack, PipeUnary))

    def test_pipe_call(self) -> None:
        """Pipe object has func"""

        def double(value: int) -> float:
            return value * 2

        stack = pipe_unary(double)

        self.assertEqual(42, stack(21))
