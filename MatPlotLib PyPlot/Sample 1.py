import matplotlib
import random

matplotlib.use('TkAgg')
import matplotlib.pyplot as plot

# plot values
#CHANGES: change the x, y1 and y2 values. You can enter the numbers by hand, use the range function or a random function.
# len(x), len(y1) and len(y2) must be at least 8 - done
x = list(range(0,8))
y1 = list(random.sample(range(0,9),8))
plot.plot(x, y1, label='curve 1',\
          marker='s', color='c', linestyle='-') #CHANGES: change color and marker. - done

y2 = list(random.sample(range(0,9),8))
plot.plot(x, y2, label='curve 2',\
          marker='*', color='purple', linestyle='--') #CHANGES: change color and the marker. - done

#CHANGES: include a third curve. You shoud provide the y values, marker, color and linestyle for this curve. - done
y3 = list(random.sample(range(0,9),8))
plot.plot(x, y3, label='curve 3',\
          marker='x', color='r', linestyle='-.')

# customize plot
plot.xlabel('x axis')
plot.ylabel('y axis')
#CHANGES: Provide a new title for the plot. - done
plot.title('comparing three random plots')
plot.legend()
plot.grid()

# add space around the border of the axes
#CHANGES: redefine the axis limits based on the new values of x. - done
plot.xlim(-0.1, 8.1)
#CHANGES: redefine the axis limits based on the values of y from all the curves. - done
plot.ylim(-1, 10)

# save and view plot
plot.savefig("sample-plot.pdf") # saves file in PDF
plot.savefig("sample-plot.png") # saves file in PNG format
plot.show()  # allows for interactive exploration of the plot