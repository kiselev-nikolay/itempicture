from .svg import Element, iter_paths, iter_texts, parse
from .utils import generate_color_groups
from typing import List


def process_template(input_path: str,
                     hues: List[str],
                     text: str = None,
                     change_only: str = None) -> Element:
    with open(input_path) as file:
        svg = parse(file)
    paths = list(iter_paths(svg))
    paths_count = len(paths)
    gradient = paths_count // len(hues)
    color_groups = generate_color_groups(hues, gradient)
    for edit_path_node, color in zip(paths, color_groups):
        edit_path_node(color)
    if text:
        for edit_text_node in iter_texts(svg):
            edit_text_node(text, change_only)
    return svg


def test_process_template() -> None:
    svg = process_template('examples/leaf.svg', [190, 170], 'yeh', 'hey')
    assert '#3fbaa5' in svg.toxml()
    assert 'hey' not in svg.toxml()
    assert 'yeh' in svg.toxml()
