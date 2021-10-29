import matplotlib.pyplot as plt
import numpy as np

%matplotlib inline  

x = np.arange(0,4*np.pi,0.1)   # start,stop,step
y = np.sin(x)

plt.plot(x,y)
plt.legend(['sin(x)'])
plt.show()

x = np.arange(0,4*np.pi,0.1)   # start,stop,step
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y,x,z)
plt.legend(['sin(x)', 'cos(x)'])
plt.show()


x = np.arange(0,5*np.pi-1,0.1)   # start,stop,step
y = np.sin(x)
z = np.cos(x)
a = np.tan(x)

plt.plot(x,y,x,z)
plt.plot(x,a)
plt.xlabel('x values from 0 to 4pi')  # string must be enclosed with quotes '  '
plt.ylabel('sin(x) and cos(x)')
plt.title('Plot of sin, cos and tan from 0 to 4pi')
plt.legend(['sin(x)', 'cos(x)', 'tan(x)'])      # legend entries as seperate strings in a list
plt.show()
