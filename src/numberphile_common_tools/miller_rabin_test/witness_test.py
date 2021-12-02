def recursive_coeffecient_calculation(n_minus_1: int, m: int = 1) -> tuple[int, int]:
    """Recursively determine the coefficient d in the equation: n = 2**m * d + 1"""
    d_float: float = (
        n_minus_1 / 2
    )  # note: python will treat this as a float, typing aside
    assert d_float.is_integer()  # ensure int and then convert
    d: int = int(d_float)
    if d % 2 == 0:
        m += 1
        d, m = recursive_coeffecient_calculation(n_minus_1=d, m=m)
    return d, m


def naive_witness_test(n: int, a: int, verbose: bool = False) -> bool:
    """A naive implementation of a witness test that simply uses one witness
    - returns True if prime, false if not
    - remember, they're 'strong liars', so only False is certain
    """
    # check rules
    assert n > 2 and n % 2 == 1  # odd n greater than 2
    d, m = recursive_coeffecient_calculation(n_minus_1=n - 1)
    if verbose:
        print(d, m)

    # check accuracy of rearrangement
    # this sort of thing would go in a test file if packaged
    assert (
        n == (2 ** m) * d + 1
    ), f"fails fundamental equality, {n} != {(2 ** m) * d + 1}, m: {m}, d: {d}, witness or a: {a}"
    assert (
        a <= n - 2
    ), f"failed check: {a} <= {n}-2 - witness number, a, must be less than the number under inspection, n"
    ask_witness = (a ** d) % n
    if verbose:
        print(f"starting witness check: {ask_witness}")

    # basic case
    if ask_witness == 1 or ask_witness == n - 1:
        return True

    # higher exponent case (denoted as r for 1 < r < m)
    ask_witness_generator = (
        (a ** ((2 ** new_exponent) * d)) % n for new_exponent in range(1, m)
    )  # generate other witnesses for larger m
    for ask_witness in ask_witness_generator:
        if verbose:
            print(ask_witness)
        if ask_witness == n - 1:
            return True

    return False
