'''
conda install bokeh::bokeh
'''

from bokeh.plotting import figure, show
from bokeh.models import HoverTool

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [8, 1, 9, 3, 23, 5, 1, 18, 4, 7]
sizes = [10, 5, 10, 5, 5, 20, 5, 5, 20, 30]

p = figure(title='Ma courbe', x_axis_label='x', y_axis_label='y')
p.line(x, y, line_width=3)
p.scatter(x, y, size=sizes, color='red')

hover = HoverTool()
hover.tooltips = [('X', '$x'), ('Y', '$y')]
p.add_tools(hover)

show(p)