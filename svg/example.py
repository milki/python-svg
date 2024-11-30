from canvas import Canvas
from link import Link
from server import svg_server
from shapes import Rectangle

canvas = Canvas(500, 500)
link = Link("Something", "https://google.com", canvas)
rect = Rectangle(100, 200, link)
svg_server(canvas)
