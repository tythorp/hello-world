'Tyler Thorpe'

from matplotlib.pyplot import *
from numpy import *

t = arange(0,1,0.01)
y = 2.0*sin(2*pi*t)

import copy
y_sat = copy.copy(y)

figure(1)
clf()
plot(t,y,'r--')

y_sat[y_sat < 0.5] = 0.5

plot(t, y_sat, label = '$y(t)$', linewidth = 3.0)
ylabel('$y(t)$')
xlabel('Time (sec.)')
legend(loc = 1)

show()