"""Tests for itempicture module."""

from itempicture.processor import process_template
from itempicture.svg import read_tree, iter_paths, iter_texts
from itempicture.utils import generate_color_groups
import itertools


def test_process_template():
    """Test itempicture processor."""
    svg = process_template('examples/leaf.svg', [190, 170], 'yeh', 'hey')
    assert '#3fbaa5' in svg.toxml()
    assert 'hey' not in svg.toxml()
    assert 'yeh' in svg.toxml()


def test_read_tree():
    """Test itempicture svg."""
    svg = read_tree('examples/leaf.svg')
    for i, edit_path_node in enumerate(iter_paths(svg)):
        edit_path_node(['#ff1111', '#00bebe'][i])
    for edit_text_node in iter_texts(svg):
        edit_text_node('yes!')
    assert svg
    assert 'yes!' in svg.toxml()
    assert '#00bebe' in svg.toxml()


def test_generator():
    """Test itempicture utils."""
    hsl_strings = []
    color_generator = generate_color_groups(range(0, 360, 10), 3)
    for hsl_string in itertools.islice(color_generator, 360):
        hsl_strings.append(hsl_string)
    assert len(set(hsl_strings)) == 36 * 3
