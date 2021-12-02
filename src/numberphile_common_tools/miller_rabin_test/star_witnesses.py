from abc import ABC, abstractmethod, abstractproperty
from numberphile_common_tools.miller_rabin_test import StarWitnessesInterface


smallest_possible = (2, 3)  # works for: 1_373_653
three_numbers = (2, 3, 5)  # works for 25_326_001
bigger_list_of_two = (31, 73)  # 9_080_191
squad_of_four = (2, 13, 23, 1_662_803)  # 1_122_004_669_633
friendly_five = (2, 3, 5, 7, 11)  # 2_152_302_898_747 ...oh, look, Matt's bow
twelve_angry_men = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)  # 10^23
# 318_665_857_834_031_151_167_461  --might not go in a regular int by my reckoning


class StarWitnessFoundation(ABC):
    @property
    @abstractmethod
    def star_witnesses(self) -> tuple[int, ...]:
        ...

    @property
    @abstractmethod
    def upper_bound(self) -> int:
        ...

    def __repr__(self) -> str:
        return f"star witnesses: {self.star_witnesses} valid for n < {self.upper_bound}"


class SmallestPossible:
    @property
    def star_witnesses(self) -> tuple[int, ...]:
        return (2, 3)

    @property
    def upper_bound(self) -> int:
        return 1_373_653


class ThreeWitnesses:
    @property
    def star_witnesses(self) -> tuple[int, ...]:
        return (2, 3, 5)

    @property
    def upper_bound(self) -> int:
        return 25_326_001


class BiggerListOfTwo:
    @property
    def star_witnesses(self) -> tuple[int, ...]:
        return bigger_list_of_two

    @property
    def upper_bound(self) -> int:
        return 9_080_191


class SquadOfFour:
    @property
    def star_witnesses(self) -> tuple[int, ...]:
        return squad_of_four

    @property
    def upper_bound(self) -> int:
        return 1_122_004_669_633


class FriendlyFive:
    @property
    def star_witnesses(self) -> tuple[int, ...]:
        return friendly_five

    @property
    def upper_bound(self) -> int:
        return 2_152_302_898_747


class TwelveAngryMen:
    @property
    def star_witnesses(self) -> tuple[int, ...]:
        return twelve_angry_men

    @property
    def upper_bound(self) -> int:
        return 318_665_857_834_031_151_167_461


list_of_star_witnesses: list[StarWitnessesInterface] = [
    SmallestPossible(),
    BiggerListOfTwo(),
    ThreeWitnesses(),
    SquadOfFour(),
    FriendlyFive(),
    TwelveAngryMen(),
]
