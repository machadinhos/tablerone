"""Exceptions raised by tablerone."""


class TableroneError(Exception):
    """Base class for all exceptions raised by tablerone."""


class InvalidStringError(TableroneError):
    """Raised when the string provided to generate a 'TableStyle' is not valid."""


class InvalidTableError(TableroneError):
    """Raised when the 2D Sequence provided to generate a table is not valid."""


class InvalidOptionsError(TableroneError):
    """Raised when the options provided to generate a table are not valid."""


class InvalidPaddingValueError(InvalidOptionsError):
    """Raised when the padding value provided to generate a table is not valid."""
