"""Define the options for table generation."""

from collections.abc import Sequence
from dataclasses import dataclass
from enum import Enum, auto

from tablerone.exceptions import InvalidPaddingValueError
from tablerone.table_style import TableStyle


class Alignment(Enum):
    """Enum representing text alignment within a cell.

    Attributes:
    ----------
        TOP_LEFT: Align text to the top left of the cell.
        TOP_CENTER: Align text to the top center of the cell.
        TOP_RIGHT: Align text to the top right of the cell.
        MIDDLE_LEFT: Align text to the middle left of the cell.
        MIDDLE_CENTER: Align text to the middle center of the cell.
        MIDDLE_RIGHT: Align text to the middle right of the cell.
        BOTTOM_LEFT: Align text to the bottom left of the cell.
        BOTTOM_CENTER: Align text to the bottom center of the cell.
        BOTTOM_RIGHT: Align text to the bottom right of the cell.
        CENTER: Alias for MIDDLE_CENTER.
        LEFT: Alias for MIDDLE_LEFT.
        RIGHT: Alias for MIDDLE_RIGHT.

    """

    TOP_LEFT = auto()
    TOP_CENTER = auto()
    TOP_RIGHT = auto()
    MIDDLE_LEFT = auto()
    MIDDLE_CENTER = auto()
    MIDDLE_RIGHT = auto()
    BOTTOM_LEFT = auto()
    BOTTOM_CENTER = auto()
    BOTTOM_RIGHT = auto()

    # Aliases for convenience
    CENTER = MIDDLE_CENTER
    LEFT = MIDDLE_LEFT
    RIGHT = MIDDLE_RIGHT


class Merge(Enum):
    """Represent the direction in which to merge cells.

    Only used when wanting to merge cells in a table.

    Attributes:
    ----------
        UP: Merge the cell with the cell above.
        DOWN: Merge the cell with the cell below.
        LEFT: Merge the cell with the cell to the left.
        RIGHT: Merge the cell with the cell to the right.

    """

    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()


class PresetTableStyles:
    """Define preset table styles for easy selection.

    Attributes:
    ----------
        default: Default table style with specific characters for borders. "╔╗╚╝║═╬╠╣╦╩"
        thin: Thin table style with specific characters for borders. "┌┐└┘│─┼├┤┬┴"

    """

    default = TableStyle.from_string("╔╗╚╝║═╬╠╣╦╩")
    thin = TableStyle.from_string("┌┐└┘│─┼├┤┬┴")


@dataclass(eq=False, repr=False, slots=True)
class TableOptions:
    """Options for the table generator.

    Attributes:
    ----------
        table_style: TableStyle
            The style of the table.
        padding_horizontal_no_border: int
            The horizontal padding of the table when there are no borders.
        padding_vertical_no_border: int
            The vertical padding of the table when there are no borders.
        padding_horizontal_with_border: int
            The horizontal padding of the table when there are borders.
        padding_vertical_with_border: int
            The vertical padding of the table when there are borders.
        left_col_separator: bool
            Whether to add a separator to the right of the leftmost column.
        right_col_separator: bool
            Whether to add a separator to the left of the rightmost column.
        top_row_separator: bool
            Whether to add a separator to the bottom of the top row.
        bottom_row_separator: bool
            Whether to add a separator to the top of the bottom row.
        vertical_separator: bool
            Whether to add a vertical separator between every column.
        horizontal_separator: bool
            Whether to add a horizontal separator between every row.
        align: Sequence[Sequence[Alignment]] | Sequence[Alignment] | Alignment
            The alignment of the cells. Can be a Sequence of Sequences of Alignment (to define the alignment of each
            cell), a Sequence of Alignment (to define the alignment of all cells in each column), or a single Alignment
            (to define the alignment of all cells).
        align_header: Sequence[Sequence[Alignment]] | Sequence[Alignment] | Alignment | None
            The alignment of the header cells. Can be a Sequence of Sequences of Alignment (to define the alignment of
            each header cell), a Sequence of Alignment (to define the alignment of all header cells in each column), a
            single Alignment (to define the alignment of all body cells), or None (to use the value of `align`).
        align_body: Sequence[Sequence[Alignment]] | Sequence[Alignment] | Alignment | None
            The alignment of the body cells. Can be a Sequence of Sequences of Alignment (to define the alignment of
            each body cell), a Sequence of Alignment (to define the alignment of all body cells in each column), a
            single Alignment (to define the alignment of all body cells), or None (to use the value of `align`).

    """

    table_style: TableStyle
    padding_horizontal_no_border: int
    padding_vertical_no_border: int
    padding_horizontal_with_border: int
    padding_vertical_with_border: int
    left_col_separator: bool
    right_col_separator: bool
    top_row_separator: bool
    bottom_row_separator: bool
    vertical_separator: bool
    horizontal_separator: bool
    align: Sequence[Sequence[Alignment]] | Sequence[Alignment] | Alignment
    align_header: Sequence[Sequence[Alignment]] | Sequence[Alignment] | Alignment | None
    align_body: Sequence[Sequence[Alignment]] | Sequence[Alignment] | Alignment | None

    def __post_init__(self):
        """Check if the padding values are non-negative.

        Raises:
        ------
            InvalidOptionsError: If one of the padding values are negative.
            GroupException: If multiple padding values are negative.

        """
        paddings = [
            "padding_horizontal_no_border",
            "padding_vertical_no_border",
            "padding_horizontal_with_border",
            "padding_vertical_with_border",
        ]

        invalid_padding_error_message = "{} value must be non-negative, {} provided."
        exceptions = [
            InvalidPaddingValueError(invalid_padding_error_message.format(padding, getattr(self, padding)))
            for padding in paddings
            if getattr(self, padding) < 0
        ]

        if exceptions:
            exception_group_message = "Invalid option(s) provided."
            raise ExceptionGroup(exception_group_message, exceptions)
