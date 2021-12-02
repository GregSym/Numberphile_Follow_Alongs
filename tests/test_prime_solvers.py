from numberphile_common_tools.miller_rabin_test import _PrimeDetectorInterface
from numberphile_common_tools.sequence_generators import gen_primes
from numberphile_common_tools.sequence_generators import odd_generator


def test_prime_detection(
    prime_checker: _PrimeDetectorInterface,
    test_start: int = 4,
    test_range: int = 100,
    verbose: bool = False,
):
    primes_gen = gen_primes()
    primes = [next(primes_gen) for _ in range(test_range)]
    if verbose:
        print(primes)
        [
            print(odd_num, prime_checker.prime_determination(n=odd_num))
            for odd_num in odd_generator(test_start, test_range)
        ]
    number_result_zipped = (
        (odd_num, prime_checker.prime_determination(n=odd_num))
        for odd_num in odd_generator(test_start, test_range)
    )
    for number, result in number_result_zipped:
        if result:
            assert (
                number in primes
            ), f"A number, {number}, was declared prime that cannot be found in test primes"
        elif not result:
            assert (
                number not in primes
            ), f"A number, {number},  was declared composite that can be found in test primes"


def test_individual_prime_detection(prime_checker: _PrimeDetectorInterface, n: int):
    """lighter weight, individual prime test
    test is bounded by: n < 2^64
    """
    from sympy import isprime

    assert n < 2 ** 64, f"Test is invalid for n < 2^64, given n={n}"

    print(
        f"sympy solution: {isprime(n)}, submitted prime checker's solution: {prime_checker.prime_determination(n)}"
    )
    assert isprime(n) == prime_checker.prime_determination(
        n
    ), "failed to match sympy implementation's prime check"
