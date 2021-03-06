import math


def prime(n: int) -> int:
    """Computes all prime numbers below n.
    Computes the sieve of Eratosthenes
    >>> prime(20)
    {1, 2, 3, 5, 7, 11, 13, 17, 19}
    """
    assert n > 0, "Positive integers only"
    p = set(range(1, n))
    for i in range(2, int(math.sqrt(n)) + 1):
        p = p - set(x*i for x in range(2, n//i + 1))
    return p


prime(20)