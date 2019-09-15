from typing import List, Union, Iterable

COLOR_TEMPLATE = 'hsl({hue}, {value}%, {value}%)'


def hsl_color(value: float, hue: Union[int, float], step: int) -> str:
    if isinstance(hue, float):
        hue *= 360
    return COLOR_TEMPLATE.format(hue=hue,
                                 value=39 + ((value % step) * 5))


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
