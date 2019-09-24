"""Itempicture utils for color processing."""

from typing import List, Union, Iterable
import colorsys


def hsl_color(value: float, hue: Union[int, float], step: int) -> str:
    """
    Generete a hex color from value and hue.

    Step set how often color light resets.
    """
    if isinstance(hue, int):
        hue /= 360
    value = 49 + ((value % step) * 5)
    value /= 100
    rgb = colorsys.hls_to_rgb(hue, value, value)
    r_255, g_255, b_255 = [int(c * 255) for c in rgb]
    return '#%02x%02x%02x' % (r_255, g_255, b_255)


def generate_color_groups(colors: List[float], steps: int) -> Iterable[str]:
    """
    Generate color groups.

    Colors is hue list. Step set how often color light resets.
    """
    while True:
        for color in colors:
            for i in range(steps):
                yield hsl_color(i, color, steps)
