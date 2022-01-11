'''This function simulates a long-term trend that the sensor node is running out of battery

This would cause the long-term pavket loss to be slowly increasing, until totally
unable to transmit packet. At this time sensor nodes can sense, but not producing packet transmitting
Therefore the general trend for this kind of packetloss would be a increasing probability of packetloss
until 100% loss of packet.

https://www.sciencedirect.com/topics/computer-science/sensor-node

'''

import numpy as np

x = np.arange(1,1000)
y = np.exp(x)

import matplotlib.pyplot as plt
plt.plot(x,y)
plt.show()