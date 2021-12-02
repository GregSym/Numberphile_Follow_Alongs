""" a function for generating odd numbered sequences """

from typing import Generator


def odd_generator(lower_bound: int, upper_bound: int) -> Generator[int, None, None]:
    return (
        x for x in range(lower_bound, upper_bound) if x % 2
    )  # we're gonna want an odd num generator for testing
