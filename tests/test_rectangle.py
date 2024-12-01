import svg
from svg.canvas import Canvas
from svg.server import svg_server
from svg.shapes import Rectangle

canvas = Canvas(500, 500)
rect1 = Rectangle(200, 100, canvas)
svg_server(canvas=canvas, port=8000)
