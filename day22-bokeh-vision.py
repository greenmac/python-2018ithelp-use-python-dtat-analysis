# https://ithelp.ithome.com.tw/articles/10196690
from bokeh.plotting import figure, show

"""
bokeh.plotting
"""
# p = figure(plot_width=500, plot_height=500)
# x = [1,2,3,4,5,6,7,8,9,10,11]
# y = [6,3,7,2,4,6,1,2,3,5,6]
# p.circle(x, y, size=20, color="gray", alpha=0.6)
# show(p)

"""
Single Lines
"""
# p = figure(plot_width=500, plot_height=500)
# x = [1,2,3,4,5,6,7,8,9,10,11]
# y = [6,3,4,2,5,2,5,1,3,5,4]
# p.line(x, y, line_width=3)
# show(p)

"""
Multiple Lines
"""
# p = figure(plot_width=500, plot_height=500)
# x1 = [1, 2, 3]
# x2 = [2, 3, 4, 5, 6]
# y1 = [3, 2, 5]
# y2 = [3, 2, 4, 1, 3]
# p.multi_line([x1,x2] , [y1, y2],
#              color=["firebrick", "navy"], alpha=[0.8, 0.3], line_width=5)
# show(p)

"""
Bars
"""
# p = figure(plot_width=500, plot_height=500)
# p.vbar(x=[1, 2, 3, 4], width=0.5, bottom=0,
#        top=[1.2, 2.5, 3.7, 2.9], color="black",alpha=0.4)
# show(p)

"""
Multiple Patches
"""
p = figure(plot_width=500, plot_height=500)
x1 = [1, 4, 5, 2]
x2 = [3, 4, 5, 6]
x3 = [1,3,2]
y1 = [2, 3, 5, 6]
y2 = [4, 7, 7, 5]
y3 = [7,8,5.5]
p.patches([x1,x2,x3 ], [y1,y2,y3],
          color=["black", "navy","firebrick"], alpha=[0.2, 0.2,0.3], line_width=2)
show(p)