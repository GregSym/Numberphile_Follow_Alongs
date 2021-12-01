"""
Common interfaces for calculating Miller Rabin Test related problems
"""

from typing import Protocol


class StarWitnessesInterface(Protocol):
  """ An interface for interacting with defined 
      test cases for the Miller Rabin Test 
  """
  @property
  def star_witnesses(self) -> tuple[int, ...]:...
  @property
  def upper_bound(self) -> int:...


class _PrimeDetectorInterface(Protocol):
    """ the methods to expect on a prime calculator from this package """
    def prime_determination(self, 
                            n: int, 
                            witness_group: StarWitnessesInterface# = SmallestPossible()
                            ) -> bool:... 