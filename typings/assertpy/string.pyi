from typing import Any

from .assertpy import AssertionBuilder

__tracebackhide__: bool = ...


class StringMixin:
    def is_equal_to_ignoring_case(self, other: Any) -> AssertionBuilder:
        ...

    def contains_ignoring_case(self, *items: Any) -> AssertionBuilder:
        ...

    def starts_with(self, prefix: Any) -> AssertionBuilder:
        ...

    def ends_with(self, suffix: Any) -> AssertionBuilder:
        ...

    def matches(self, pattern: Any) -> AssertionBuilder:
        ...

    def does_not_match(self, pattern: Any) -> AssertionBuilder:
        ...

    def is_alpha(self) -> AssertionBuilder:
        ...

    def is_digit(self) -> AssertionBuilder:
        ...

    def is_lower(self) -> AssertionBuilder:
        ...

    def is_upper(self) -> AssertionBuilder:
        ...

    def is_unicode(self) -> AssertionBuilder:
        ...
