"""Tests"""
from unittest import TestCase

from functional.pipe import PipeArbitrary, PipeUnary


class PipeUnaryTests(TestCase):
    """test Pipe class"""

    def test_init(self) -> None:
        """init func first in pipe"""

        def double(value: int) -> float:
            return float(value * 2)

        stack = PipeUnary(double)

        self.assertEqual(4.0, stack(2))

    def test_2nd(self) -> None:
        """pipes 2 funcs"""

        def double(value: int) -> float:
            return float(value * 2)

        def to_string(value: float) -> str:
            return str(value)

        stack = PipeUnary(double).pipe(to_string)

        self.assertEqual(str(42.0), stack(21))


class PipeArbitraryTests(TestCase):
    """test Pipe class"""

    def test_init(self) -> None:
        """init func first in pipe"""

        def _sum(fst: int, snd: float) -> float:
            return float(fst) + snd

        stack = PipeArbitrary(_sum)

        self.assertEqual(7.0, stack(2, 5.0))

    def test_2nd(self) -> None:
        """pipes 2 funcs"""

        def _sum(fst: int, snd: float) -> float:
            return float(fst) + snd

        def to_string(value: float) -> str:
            return str(value)

        stack = PipeArbitrary(_sum).pipe(to_string)

        self.assertEqual(str(42.0), stack(20, 22.0))
