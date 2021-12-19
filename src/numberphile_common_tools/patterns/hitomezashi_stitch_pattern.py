import matplotlib.pyplot as plt
import sys

if float(f"{sys.version_info[0]}.{sys.version_info[1]}") >= 3.8:
    from typing import Protocol
else:
    print("python version lower than 3.9 detected")
    from typing_extensions import (  # type: ignore
        Protocol,
    )  # < 3.8 Protocol lives in a different package


class HitomezashiRepr:
    """An abstraction layer from the encoding of the pattern on the sides of the grid"""

    def __init__(self, side_one: list[int], side_two: list[int], *args, **kwargs):
        self.side_one = side_one
        self.side_two = side_two

    def _vector_grid_general(
        self, index_side: list[int], magnitude_side: list[int]
    ) -> dict[int, list[tuple[int, int]]]:
        """returns vectors for either of 2 dimensions in the hitomezashi pattern
        - this means the vectors are naturally 1D vectors in either the x or y direction
        """
        vector_map: dict[int, list[tuple[int, int]]] = {}
        for index, bit in enumerate(index_side):
            vector_map[index] = []
            for index_value_pair, index_value_pair1 in zip(
                enumerate(magnitude_side), list(enumerate(magnitude_side))[1:]
            ):
                if bit == 1:
                    if index_value_pair[0] % 2 == 0 and index_value_pair1[0] % 2 == 1:
                        vector_map[index].append(
                            (index_value_pair[0], index_value_pair1[0])
                        )
                else:
                    if index_value_pair[0] % 2 == 1 and index_value_pair1[0] % 2 == 0:
                        vector_map[index].append(
                            (index_value_pair[0], index_value_pair1[0])
                        )
        return vector_map

    @property
    def vector_grid_ltr(self) -> dict[int, list[tuple[int, int]]]:
        return self._vector_grid_general(
            index_side=self.side_one, magnitude_side=self.side_two
        )

    @property
    def vector_grid_btt(self) -> dict[int, list[tuple[int, int]]]:
        return self._vector_grid_general(
            index_side=self.side_two, magnitude_side=self.side_one
        )

    def _line_segments_general(
        self, grid_single_direction: dict[int, list[tuple[int, int]]]
    ) -> dict[int, dict[int, tuple[int, int]]]:  # typealias this maybe?
        """returns segmented vectors in the format required by plt.Line2D -> (x1, x2), (y1, y2)
        - returns only one of the dimension tuples
        """
        return {
            index: {
                internal_index: vector
                for internal_index, vector in enumerate(list_tuple)
            }
            for (index, list_tuple) in grid_single_direction.items()
        }

    @property
    def line_segments_ltr(
        self,
    ) -> dict[int, dict[int, tuple[int, int]]]:  # typealias this maybe?
        return self._line_segments_general(grid_single_direction=self.vector_grid_ltr)

    @property
    def line_segments_btt(
        self,
    ) -> dict[int, dict[int, tuple[int, int]]]:  # typealias this maybe?
        return self._line_segments_general(grid_single_direction=self.vector_grid_btt)


class _VisualiserInterfaceHitomezashi(Protocol):
    """Interface for visualisation of a Hitomezashi Stitch Pattern"""

    def __call__(self, pattern: HitomezashiRepr, verbose: bool) -> None:
        ...


def visualise_hitomezashi_pattern(pattern: HitomezashiRepr, verbose: bool = False):
    """(pattern) -> visualisation of hitomezashi stitch pattern"""

    def _plotting(
        line_segments: dict[int, dict[int, tuple[int, int]]],
        direction: str = "ltr",
    ):
        for key, vector_dict in line_segments.items():
            for vector in vector_dict.values():
                plt.gca().add_line(
                    plt.Line2D(xdata=vector, ydata=(key, key), linewidth=2.5)
                ) if direction == "ltr" else plt.gca().add_line(
                    plt.Line2D(xdata=(key, key), ydata=vector, linewidth=2.5)
                )

    if verbose:
        print(pattern.vector_grid_ltr)
        print(pattern.vector_grid_btt)
        print(pattern.line_segments_ltr)
        print(pattern.line_segments_btt)
    plt.axes()
    _plotting(pattern.line_segments_ltr)
    _plotting(pattern.line_segments_btt, direction="btt")
    plt.axis("scaled")
    plt.show()
