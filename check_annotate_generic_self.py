from __future__ import annotations
from typing import Self


class A:
    def foo(self: Self) -> list[Self]:
        res = list[A(), A()]
        return res


class B:
    def foo(self: Self) -> list[Self]:
        res = list[self, self]
        return res


class C:
    def foo(self: Self) -> Self:
        return C()


class D:
    def bar(self) -> Self:
        ...

    def foo(self: Self) -> Self:
        return self.bar()


class E:
    def bar(self) -> E:
        ...

    def foo(self: Self) -> Self:
        return self.bar()
