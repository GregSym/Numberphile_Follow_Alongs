from __future__ import annotations
from dataclasses import dataclass
import numpy as np
import numpy.typing as npt
from numberphile_common_tools.patterns import hitomezashi_stitch_pattern as hsp


@dataclass
class MazeWalls:
    """A struct of bools representing a truth table of wall positions relative to a cell"""

    left: bool
    right: bool
    top: bool
    bottom: bool


@dataclass
class MazeCell:
    """Representation of maze cell"""

    index: tuple[int, int]
    walls: MazeWalls

    def __eq__(self, other) -> bool:
        if not isinstance(other, MazeCell):
            return False
        return other.index[0] == self.index[0] and other.index[1] == self.index[1]


@dataclass
class Maze:
    maze_cells: list[list[MazeCell]]

    def cmd_line_display(self):
        for yindex, row in enumerate(self.maze_cells):
            printables = ""
            top_row = ""
            for xindex, cell in enumerate(row):
                left = "|" if cell.walls.left else " "
                right = "|" if cell.walls.right else " "
                bottom = "_" if cell.walls.bottom else " "
                if yindex == 0:
                    top_row += " "
                    top_row += "_" if cell.walls.top else " "
                    if xindex == len(row) - 1:
                        top_row += " "
                printables += left
                printables += bottom
                if xindex == len(row) - 1:
                    printables += right
            if yindex == 0:
                print(top_row)
            print(printables)

    def find_one_path(self) -> list[MazeCell]:
        """Represents one of two maze cell paths through the pattern"""
        colour: list[MazeCell] = [self.maze_cells[0][0]]
        not_colour: list[MazeCell] = []

        def _compare_and_add_cells(cell1: MazeCell, cell2: MazeCell, wall: bool):
            # check colour
            if cell1 not in colour and cell2 in colour:
                not_colour.append(cell1) if wall else colour.append(cell1)
            if cell1 in colour and cell2 not in colour:
                not_colour.append(cell2) if wall else colour.append(cell2)
            # check not_colour
            if cell1 not in not_colour and cell2 in not_colour:
                colour.append(cell1) if wall else not_colour.append(cell1)
            if cell1 in not_colour and cell2 not in not_colour:
                colour.append(cell2) if wall else not_colour.append(cell2)

        for yindex, cell_row in enumerate(self.maze_cells):
            for xindex, cell in enumerate(cell_row):
                # add to colour
                if xindex > 0:
                    _compare_and_add_cells(
                        cell1=self.maze_cells[yindex][xindex - 1],
                        cell2=cell,
                        wall=cell.walls.left,
                    )
                if xindex < len(self.maze_cells) - 1:
                    _compare_and_add_cells(
                        cell1=self.maze_cells[yindex][xindex + 1],
                        cell2=cell,
                        wall=cell.walls.right,
                    )
                if yindex > 0:
                    _compare_and_add_cells(
                        cell1=self.maze_cells[yindex - 1][xindex],
                        cell2=cell,
                        wall=cell.walls.top,
                    )
                if yindex < len(self.maze_cells) - 1:
                    _compare_and_add_cells(
                        cell1=self.maze_cells[yindex + 1][xindex],
                        cell2=cell,
                        wall=cell.walls.bottom,
                    )

        return colour

    @classmethod
    def from_pattern(cls, pattern: hsp.HitomezashiRepr) -> Maze:
        maze_cells: list[list[MazeCell]] = []
        for (yindex_top, horizontal_vectors_top), (
            yindex_bottom,
            horizontal_vectors_bottom,
        ) in zip(
            reversed(list(pattern.vector_grid_ltr.items())),
            reversed(list(pattern.vector_grid_ltr.items())[:-1]),
        ):
            cell_row: list[MazeCell] = []
            for (xindex_left, vertical_vectors_left), (
                xindex_right,
                vertical_vectors_right,
            ) in zip(
                list(pattern.vector_grid_btt.items()),
                list(pattern.vector_grid_btt.items())[1:],
            ):
                walls = MazeWalls(
                    left=vertical_vectors_left[0][0] == yindex_bottom % 2,
                    right=vertical_vectors_right[0][0] == yindex_bottom % 2,
                    top=horizontal_vectors_top[0][0] == xindex_left % 2,
                    bottom=horizontal_vectors_bottom[0][0] == xindex_left % 2,
                )
                cell_row.append(
                    MazeCell(index=(xindex_left, yindex_bottom), walls=walls)
                )
            maze_cells.append(cell_row)

        return cls(maze_cells=maze_cells)

    @property
    def colour_map(self) -> npt.NDArray[np.float64]:
        # init numpy.ndarray of correct shape
        _colour_map = np.zeros((len(self.maze_cells), len(self.maze_cells)))

        # iterate over cells in path and paint those
        for cell in self.find_one_path():
            _colour_map[cell.index[1], cell.index[0]] = 1

        return _colour_map
