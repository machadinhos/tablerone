"""The tablerone package allows you to generate unicode tables from bi-dimensional sequences.

The main function is `tablerone`, which takes a bi-dimensional sequence and returns a string representation of the table
in unicode.
"""

from tablerone.table import tablerone
from tablerone.table_options import Alignment, Merge, PresetTableStyles, TableOptions
from tablerone.table_style import TableStyle

__all__ = [
    "TableOptions",
    "PresetTableStyles",
    "TableStyle",
    "Alignment",
    "Merge",
    "tablerone",
]
