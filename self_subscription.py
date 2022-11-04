from typing import Self, Generic, TypeVar

T = TypeVar("T")


class A(Generic[T]):
    def foo(self):
        x: Self[int]
