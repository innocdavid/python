import numpy 
import matplotlib.pyplot as plt

x = numpy.arange(0, 1, 0.1)
print(x)

##plotting style
plt.xkcd()

##plotting
plt.plot(x, x, 'v-', x, x**2, 'x-', x, x**3, 'o-' )
plt.show()