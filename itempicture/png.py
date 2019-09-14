import subprocess


def make_png(input_file: str, output_file: str):
    p = subprocess.Popen(["inkscape", "-z", "-e", input_file, output_file],
                         stdout=subprocess.PIPE)
    p.communicate()
