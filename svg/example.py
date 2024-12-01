from canvas import Canvas
from link import Link
from server import svg_server
from shapes import Circle, Rectangle

canvas = Canvas(500, 500)
link = Link("https://google.com", canvas)
circle = Circle(cx=15, cy=20, r=50, parent=link)
svg_server(canvas)
