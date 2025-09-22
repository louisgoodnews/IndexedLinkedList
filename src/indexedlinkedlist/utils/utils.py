"""
Author: Louis Goodnews
Date: 2025-09-22
"""

from typing import Any, Final


__all__: Final[list[str]] = ["invert_dict"]


def invert_dict(dictionary: dict[Any, Any]) -> dict[Any, Any]:
    """
    Invert a dictionary.

    Args:
        dictionary (dict[Any, Any]): The dictionary to invert.

    Returns:
        dict[Any, Any]: The inverted dictionary.
    """

    # Return the inverted dictionary
    return {
        value: key
        for (
            key,
            value,
        ) in dictionary.items()
    }
