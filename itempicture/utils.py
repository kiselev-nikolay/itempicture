from typing import List, Union, Iterable
import colorsys


def hsl_color(value: float, hue: Union[int, float], step: int) -> str:
    if isinstance(hue, int):
        hue /= 360
    value = 49 + ((value % step) * 5)
    value /= 100
    rgb = colorsys.hls_to_rgb(hue, value, value)
    rgb = tuple(int(c * 255) for c in rgb)
    return '#%02x%02x%02x' % tuple(rgb)


def generate_color_groups(colors: List[float], steps: int) -> Iterable[str]:
    while True:
        for color in colors:
            for i in range(steps):
                yield hsl_color(i, color, steps)


def test_generator() -> None:
    import itertools
    hsl_strings = []
    color_generator = generate_color_groups(range(0, 360, 10), 3)
    for hsl_string in itertools.islice(color_generator, 360):
        hsl_strings.append(hsl_string)
    assert len(set(hsl_strings)) == 36 * 3
