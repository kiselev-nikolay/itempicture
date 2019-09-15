import random
from fire import Fire
from .processor import process_template
from cairosvg import svg2png
import os


def cli(input_template: str,
        colors_count: int,
        text: str = None,
        change_only_text: str = None,
        output: str = 'result.png'):
    """ Generate image from svg template """
    colors = [random.random() for _ in range(colors_count)]
    svg = process_template(input_template, colors, text, change_only_text)
    if output[-3:] == 'svg':
        svg_path = output
    else:
        svg_path = output + '.svg'
    with open(svg_path, 'w') as file:
        svg.writexml(file)
    if output[-3:] == 'png':
        svg2png(url=svg_path, write_to=output)
        os.remove(svg_path)


def main():
    Fire(cli)
