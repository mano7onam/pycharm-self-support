from typing import Self


class A:
    def foo(self: Self) -> list[Self]:
        res = list[A(), A()]
        return res


class B:
    def foo(self: Self) -> list[Self]:
        res = list[self, self]
        return res
