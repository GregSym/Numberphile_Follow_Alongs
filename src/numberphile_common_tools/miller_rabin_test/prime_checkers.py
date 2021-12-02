from typing import Any, Callable, Union

from sympy.multipledispatch.dispatcher import RaiseNotImplementedError
from numberphile_common_tools.miller_rabin_test import StarWitnessesInterface

from numberphile_common_tools.miller_rabin_test.witness_test import naive_witness_test
from numberphile_common_tools.miller_rabin_test import list_of_star_witnesses
from numberphile_common_tools.miller_rabin_test import SmallestPossible
from sympy import isprime


class PrimeDetector:
    witness_groups: list[
        StarWitnessesInterface
    ] = list_of_star_witnesses  # let's just borrow that from above

    miller_rabin_rule: Callable[..., Union[bool, Any]] = (
        lambda self, n: n > 2 and n % 2 == 1
    )

    def witness_group_factory(self, n: int) -> StarWitnessesInterface:
        """factory for returning appropriate witness groups"""
        for witness_group in self.witness_groups:
            if n < witness_group.upper_bound:
                return witness_group
        raise RaiseNotImplementedError

    def prime_determination(
        self, n: int, witness_group: StarWitnessesInterface = SmallestPossible()
    ) -> bool:
        assert self.miller_rabin_rule(
            n
        ), f"number must be greater than 2 and odd - number found {n}"

        if (
            n >= witness_group.upper_bound
        ):  # assign an appropriate, larger witness group if necessary
            witness_group = self.witness_group_factory(n=n)

        # print([naive_witness_test(n=n, a=witness_number) for witness_number in witness_group.star_witnesses])
        return all(
            [
                naive_witness_test(n=n, a=witness_number)
                for witness_number in witness_group.star_witnesses
            ]
        )


class PrimeDetectorSympy:
    """Wraps sympy prime verification to match interface so it can plug in as an alternative checker
    when mine gets too slow at higher ranges
    """

    def prime_determination(
        self, n: int, witness_group: StarWitnessesInterface = SmallestPossible()
    ) -> bool:
        is_prime: bool = isprime(n)
        return is_prime
