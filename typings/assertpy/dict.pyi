from typing import Any

from .assertpy import AssertionBuilder

__tracebackhide__: bool = ...


class DictMixin:
    def contains_key(self, *keys: Any) -> AssertionBuilder:
        ...

    def does_not_contain_key(self, *keys: Any) -> AssertionBuilder:
        ...

    def contains_value(self, *values: Any) -> AssertionBuilder:
        ...

    def does_not_contain_value(self, *values: Any) -> AssertionBuilder:
        ...

    def contains_entry(self, *args: Any, **kwargs: Any) -> AssertionBuilder:
        ...

    def does_not_contain_entry(
        self, *args: Any, **kwargs: Any
    ) -> AssertionBuilder:
        ...
