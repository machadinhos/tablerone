"""Defines the main functionality of the tablerone package."""

from collections.abc import Sequence
from typing import Protocol

from tablerone.table_options import Alignment, Merge, PresetTableStyles, TableOptions
from tablerone.table_style import TableStyle


class Stringifiable(Protocol):
    """A protocol to represent objects that can be converted to strings.

    Any object that adheres to this protocol must implement the __str__ method, which returns a string representation of
    the object.

    This protocol is used to indicate that objects of this type can be converted to strings via the `str` function.
    """

    def __str__(self) -> str:
        """Return a string representation of the object."""
        raise NotImplementedError


class _Table:
    __slots__ = ("data", "options", "_max_widths", "_max_heights")

    data: Sequence[Sequence[Stringifiable | Merge]]
    options: TableOptions
    _max_widths: Sequence[int]
    _max_heights: Sequence[int]

    def __init__(self, data: Sequence[Sequence[Stringifiable | Merge]], options: TableOptions):
        self.data = data
        self.options = options
        self._max_widths = self._get_max_widths()
        self._max_heights = self._get_max_heights()

    def _get_max_widths(self) -> Sequence[int]:
        """Get the maximum width of each column."""
        # TODO: Implement the method
        raise NotImplementedError

    def _get_max_heights(self) -> Sequence[int]:
        # TODO: Implement the method
        raise NotImplementedError

    def to_unicode(self) -> str:
        # TODO: Implement the method
        raise NotImplementedError

    def to_markdown(self) -> str:
        # TODO: Implement the method
        raise NotImplementedError


def tablerone(  # noqa: PLR0913
    data: Sequence[Sequence[Stringifiable | Merge]],
    table_style: TableStyle = PresetTableStyles.default,
    *,
    padding_horizontal_no_border: int = 1,
    padding_vertical_no_border: int = 1,
    padding_horizontal_with_border: int = 1,
    padding_vertical_with_border: int = 0,
    left_col_separator: bool = False,
    right_col_separator: bool = False,
    top_row_separator: bool = False,
    bottom_row_separator: bool = False,
    vertical_separator: bool = False,
    horizontal_separator: bool = False,
    align: Sequence[Sequence[Alignment]] | Sequence[Alignment] | Alignment = Alignment.CENTER,
    align_header: Sequence[Sequence[Alignment]] | Sequence[Alignment] | Alignment | None = None,
    align_body: Sequence[Sequence[Alignment]] | Sequence[Alignment] | Alignment | None = None,
    table_options: TableOptions | None = None,
) -> str:
    """Convert a bi-dimensional Sequence into a unicode table.

    Args:
    ----
        data: Sequence[Sequence[Stringifiable | Merge]]
            The data to be converted into a table. Each element of the outer Sequence  represents a row, and each
            element of the inner Sequence represents a cell. The cells can be any object that can be converted to a
            string via the 'str' function, or a 'Merge' object, which represents the action of merging cells.
        table_style: TableStyle, default=PresetsTableStyles.default
            The style of the table.
        padding_horizontal_no_border: int, default=1
            The horizontal padding of the table when there are no borders.
        padding_vertical_no_border: int, default=1
            The vertical padding of the table when there are no borders.
        padding_horizontal_with_border: int, default=1
            The horizontal padding of the table when there are borders.
        padding_vertical_with_border: int, default=0
            The vertical padding of the table when there are borders.
        left_col_separator: bool, default=False
            Whether to add a separator to the right of the leftmost column.
        right_col_separator: bool, default=False
            Whether to add a separator to the left of the rightmost column.
        top_row_separator: bool, default=False
            Whether to add a separator to the bottom of the top row.
        bottom_row_separator: bool, default=False
            Whether to add a separator to the top of the bottom row.
        vertical_separator: bool, default=False
            Whether to add a vertical separator between every column.
        horizontal_separator: bool, default=False
            Whether to add a horizontal separator between every row.
        align: Sequence[Sequence[Alignment]] | Sequence[Alignment] | Alignment, default=Alignment.CENTER
            The alignment of the cells. Can be a Sequence of Sequences of Alignment (to define the alignment of each
            cell), a Sequence of Alignment (to define the alignment of all cells in each column), or a single Alignment
            (to define the alignment of all cells).
        align_header: Sequence[Sequence[Alignment]] | Sequence[Alignment] | Alignment | None, default=None
            The alignment of the header cells. Can be a Sequence of Sequences of Alignment (to define the alignment of
            each header cell), a Sequence of Alignment (to define the alignment of all header cells in each column), a
            single Alignment (to define the alignment of all body cells), or None (to use the value of `align`).
        align_body: Sequence[Sequence[Alignment]] | Sequence[Alignment] | Alignment | None, default=None
            The alignment of the body cells. Can be a Sequence of Sequences of Alignment (to define the alignment of
            each body cell), a Sequence of Alignment (to define the alignment of all body cells in each column), a
            single Alignment (to define the alignment of all body cells), or None (to use the value of `align`).
        table_options: TableOptions, default=None
            The options for the table generator. If provided, it will override the other options provided to this
            function.

    Returns:
    -------
        str: The unicode representation of the table.

    Raises:
    ------
        InvalidOptionsError: If a given option is invalid.

    """
    return _Table(
        data,
        table_options
        or TableOptions(
            table_style=table_style,
            padding_horizontal_no_border=padding_horizontal_no_border,
            padding_vertical_no_border=padding_vertical_no_border,
            padding_horizontal_with_border=padding_horizontal_with_border,
            padding_vertical_with_border=padding_vertical_with_border,
            left_col_separator=left_col_separator,
            right_col_separator=right_col_separator,
            top_row_separator=top_row_separator,
            bottom_row_separator=bottom_row_separator,
            vertical_separator=vertical_separator,
            horizontal_separator=horizontal_separator,
            align=align,
            align_header=align_header,
            align_body=align_body,
        ),
    ).to_unicode()
