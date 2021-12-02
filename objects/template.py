from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader("objects"),
    autoescape=select_autoescape()
)
