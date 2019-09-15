import itertools
from typing import List

COLOR_TEMPLATE = 'hsl({hue}, {value}%, {value}%)'


def color(value: float, hue: float, step: int) -> str:
    return COLOR_TEMPLATE.format(hue=hue * 360,
                                 value=39 + ((value % step) * 5))


def generate_colorpairs(colors: List[float]):
    i = 0
    colors_generator = itertools.cycle(colors)
    while True:
        yield color(i, next(colors_generator), len(colors))
        i += 1


def test_generator() -> None:
    for hsl_string in itertools.islice(generate_colorpairs([.5, .5]), 10):
        print(hsl_string)
