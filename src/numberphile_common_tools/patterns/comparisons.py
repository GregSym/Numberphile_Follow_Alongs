import sys

if float(f"{sys.version_info[0]}.{sys.version_info[1]}") >= 3.8:
    from typing import Protocol
else:
    print("python version lower than 3.9 detected")
    from typing_extensions import (  # type: ignore
        Protocol,
    )  # < 3.8 Protocol lives in a different package


class _StrComparablePattern(Protocol):
    def __call__(self) -> str:
        """
        returns a kind of str repr of the pattern for comparison to other datastructures of the same pattern
        """


class _ComparableStructureForGridPattern(Protocol):
    @property
    def str_pattern(self) -> _StrComparablePattern:
        """Any datastructure for a grid pattern that implements a str repr should have this"""
