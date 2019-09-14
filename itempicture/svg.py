from xml.dom.minidom import parse
from xml.dom.minidom import Element
from functools import partial
from typing import Iterator, Tuple


def read_tree(file_path: str) -> Element:
    with open(file_path) as file:
        tree = parse(file)
    svg = tree.childNodes[0]
    return svg


def iter_element(svg: Element, name: str) -> Iterator[Element]:
    elements = svg.getElementsByTagName(name)
    for element in elements:
        yield element


def edit_fill(fill_color: str, element: Element) -> str:
    style = element.getAttribute('style')
    new_style = []
    for css in style.split(';'):
        term, value = [v.strip() for v in css.split(':')]
        if term == 'fill':
            new_style.append("{}:{}".format(term, fill_color))
        else:
            new_style.append(css)
    element.setAttribute('style', ';'.join(new_style))


def edit_text(text: str, element: Element):
    element.nodeValue = text
    breakpoint()


def iter_paths(svg):
    for path in iter_element(svg, 'path'):
        editor = partial(edit_fill, element=path)
        yield editor


def iter_texts(svg):
    for text in iter_element(svg, 'text'):
        editor = partial(edit_text, element=text)
        yield editor


def test_read_tree():
    svg = read_tree('examples/leaf.svg')
    for p in iter_paths(svg):
        p('#afaf00')
    for t in iter_texts(svg):
        t('bing-bong')
    assert svg
    with open('test.svg', 'w') as file:
        svg.writexml(file)
    breakpoint()
