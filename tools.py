"""MCP tools: dice roller and adder.

This module registers two small tools on a FastMCP instance:

- ``roll_dice(n_dice=1)``: Roll one or more six-sided dice and return the
  individual results as a list of integers.
- ``add_numbers(a, b)``: Add two numeric values and return their sum.

These functions are lightweight and intended as examples for wiring tools into
an MCP server.
"""

import random
from fastmcp import FastMCP


mcp = FastMCP(name="MyFastMCP")


@mcp.tool
def roll_dice(n_dice: int = 1) -> list[int]:
    """Roll one or more six-sided dice.

    Args:
        n_dice: Number of dice to roll. Must be a positive integer. Defaults to 1.

    Returns:
        A list of integers, each in the range 1..6, containing one entry per die.

    Raises:
        ValueError: If ``n_dice`` is less than 1.

    Example:
        >>> roll_dice(3)
        [2, 6, 1]
    """
    if n_dice < 1:
        raise ValueError("n_dice must be >= 1")
    return [random.randint(1, 6) for _ in range(n_dice)]


@mcp.tool
def add_numbers(a: float, b: float) -> float:
    """Return the sum of two numeric values.

    The function accepts integers or floats (or any types that support ``+``).
    When used with non-numeric types, Python's normal ``+`` semantics apply.

    Args:
        a: First addend.
        b: Second addend.

    Returns:
        The sum ``a + b``.

    Example:
        >>> add_numbers(1.5, 2.25)
        3.75
    """
    return a + b


if __name__ == "__main__":
    mcp.run()
