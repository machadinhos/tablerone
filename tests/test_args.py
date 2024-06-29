import inspect
from functools import partial

import pytest
from tablerone import TableOptions, tablerone
from tablerone.exceptions import InvalidPaddingValueError


@pytest.fixture(scope="module")
def tablerone_partial() -> partial[str]:
    return partial(tablerone, data=[[1, 2], [3, 4]])


@pytest.mark.parametrize(
    "paddings",
    [
        (-1, 1, 1, 1),
        (1, -1, 1, 1),
        (1, 1, -1, 1),
        (1, 1, 1, -1),
        (-1, -1, 1, 1),
        (-1, -1, -1, 1),
        (-1, -1, -1, -1),
    ],
)
def test_negative_padding_values(tablerone_partial: partial[str], paddings: tuple[int, int, int, int]):
    with pytest.raises(ExceptionGroup) as exc_info:
        tablerone_partial(
            padding_horizontal_no_border=paddings[0],
            padding_vertical_no_border=paddings[1],
            padding_horizontal_with_border=paddings[2],
            padding_vertical_with_border=paddings[3],
        )
    assert all(isinstance(exc, InvalidPaddingValueError) for exc in exc_info.value.exceptions)


def test_tablerone_args_match_table_options():
    excluded_args = {"data", "table_options"}

    tablerone_args = {
        name: param.annotation
        for name, param in inspect.signature(tablerone).parameters.items()
        if name not in excluded_args
    }
    table_options_args = {name: param.annotation for name, param in inspect.signature(TableOptions).parameters.items()}

    assert tablerone_args == table_options_args
