"""Svg utils. Work with svg like with xml file."""

from xml.dom.minidom import parse
from xml.dom.minidom import Element
from functools import partial
from typing import Iterator, Callable


def read_tree(file_path: str) -> Element:
    """Read svg file like xml tree."""
    with open(file_path) as file:
        tree = parse(file)
    svg = tree.childNodes[0]
    return svg


def iter_element(svg: Element, name: str) -> Iterator[Element]:
    """Iterate elements in xml file with given tag name."""
    elements = svg.getElementsByTagName(name)
    for element in elements:
        yield element


def edit_fill(element: Element, fill_color: str) -> None:
    """Change fill in element. Usaly wrapped in partial with fixed element."""
    style = element.getAttribute('style')
    new_style = []
    for css in style.split(';'):
        term, value = [v.strip() for v in css.split(':')]
        if term == 'fill':
            new_style.append('{}:{}'.format(term, fill_color))
        else:
            new_style.append(css)
    element.setAttribute('style', ';'.join(new_style))


def find_text_node(element: Element) -> Element:
    """
    Find every text in element.

    Texxt object in any depth if is nested else return text element.
    """
    text_nodes = []
    for paragraph in element.childNodes:
        # If the text has no nesting, it always has just one element
        if paragraph.nodeName == '#text':
            return paragraph
        elif paragraph.hasChildNodes():
            text_nodes.append(find_text_node(paragraph))
    return text_nodes


def edit_text(element: Element, text: str,
              change_only: str = None) -> None:
    """Change fill in element. Usaly wrapped in partial with fixed element."""
    text_nodes = find_text_node(element)
    for text_node in text_nodes:
        if not change_only \
           or text_node.nodeValue.strip() == change_only.strip():
            text_node.nodeValue = text


def iter_paths(svg: Element) -> Iterator[Callable]:
    """Iterate change fill function for every path object."""
    for path in iter_element(svg, 'path'):
        editor = partial(edit_fill, path)
        yield editor


def iter_texts(svg: Element) -> Iterator[Callable]:
    """Iterate change inner text function for every text object."""
    for text in iter_element(svg, 'text'):
        editor = partial(edit_text, text)
        yield editor
