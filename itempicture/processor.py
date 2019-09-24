"""Process svg template."""

from .svg import Element, iter_paths, iter_texts, parse
from .utils import generate_color_groups
from typing import List


def process_template(input_path: str,
                     hues: List[str],
                     text: str = None,
                     change_only: str = None) -> Element:
    """
    Read and return svg.

    Change colors for <path> object. Change text in <text>.
    """
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
