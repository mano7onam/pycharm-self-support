# from __future__ import annotations
from typing import Self, Protocol


class MyProtocol(Protocol):
    def foo(self, bar: float) -> Self: ...


class MyClass:
    def foo(self, bar: float) -> MyClass:
        pass


def accepts_protocol(obj: MyProtocol) -> None:
    print(obj)


obj = MyClass()
accepts_protocol(obj)
