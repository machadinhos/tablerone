"""Defines the `TableStyle` class to represent the border style of a table."""

from dataclasses import dataclass

from tablerone.exceptions import InvalidStringError


@dataclass(eq=False, frozen=True, repr=False, slots=True)
class TableStyle:
    """A class to represent the border style of a table.

    Attributes:
    ----------
        top_left : str
            The character representing the top left corner of the table.
        top_right : str
            The character representing the top right corner of the table.
        bottom_left : str
            The character representing the bottom left corner of the table.
        bottom_right : str
            The character representing the bottom right corner of the table.
        vertical : str
            The character representing the vertical separator of the table.
        horizontal : str
            The character representing the horizontal border of the table.
        joint : str
            The character representing the intersection of vertical and horizontal separators.
        joint_left : str
            The character representing the intersection of horizontal separator and left border.
        joint_right : str
            The character representing the intersection of horizontal separator and right border.
        joint_top : str
            The character representing the intersection of vertical separator and top border.
        joint_bottom : str
            The character representing the intersection of vertical separator and bottom border.

    """

    top_left: str
    top_right: str
    bottom_left: str
    bottom_right: str
    vertical: str
    horizontal: str
    joint: str
    joint_left: str
    joint_right: str
    joint_top: str
    joint_bottom: str

    @classmethod
    def from_string(cls, string: str) -> "TableStyle":
        """Create a `TableStyle` object from a string.

        Args:
        ----
            string : str
                A string of exactly 11 characters representing the table style.
                The order of the characters is as follows:
                    1 - top left corner
                    2 - top right corner
                    3 - bottom left corner
                    4 - bottom right corner
                    5 - vertical separator
                    6 - horizontal border
                    7 - joint
                    8 - joint left
                    9 - joint right
                    10 - joint top
                    11 - joint bottom

        Raises:
        ------
            InvalidStringError
                If the length of the string is invalid.

        Returns:
        -------
            TableStyle
                The table style object created from the string.

        """
        max_length = 11
        if len(string) != max_length:
            error_message = (
                f"Invalid string length: String must be exactly 11 characters long, {len(string)} characters provided."
            )
            raise InvalidStringError(error_message)

        return cls(*string)
