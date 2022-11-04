from typing import Self


class A:
    pass


class B:
    def foo(self: Self, something: Self):
        assert isinstance(A(), Self)
        assert issubclass(A, Self)
