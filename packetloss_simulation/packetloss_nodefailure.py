'''This function simulates a long-term trend that the sensor node is 
   running out of battery

This would cause the long-term pavket loss to be slowly increasing, until totally
unable to transmit packet. At this time sensor nodes can sense, but not producing 
packet transmitting. Therefore the general trend for this kind of packetloss 
would be a increasing probability of packetloss until 100% loss of packet.

https://www.sciencedirect.com/topics/computer-science/sensor-node

'''

from packetloss_normal import normal_packetloss
from config import data_packetloss_type

from typing import List

'''the principle for this function 

Rate of packetloss increases from a value to 100% through a function.
'''

class packetlossTotalSim:
    def node_failure_packetloss(
        self,
        input_data: List,#assume that this list is long-enough to reach 100%
        possibility: float, #this is a float number not a percentage
    ): 
        assert isinstance(possibility, float), \
            '''This input possibility should be 
            a float number
            '''
        
        assert isinstance(input_data, List), \
            '''This input data should be an integer list
            '''

        '''create a packetloss function 

        This function consists of a continuous function 
        which will reach 100% at last
        Assume that this function is exponential in this scenario
        '''
        ##############
        '''assume this equation is y = exp(x) + 1 - possibility

        so that this equation starts with possibility and ends with 100
        '''

        import cmath
        import random

        proportion = random.randint(2300, 2700)
        x = np.arange(
            possibility*proportion,
            len(input_data)+possibility*proportion,
            step=1).tolist()
        ########################
        '''exponential increase
        y = [cmath.exp(_x/200)*possibility for _x in x]
        
        '''

        ########################


        y = [_x/proportion for _x in x]
        ########################
        '''linear decay

        '''

        ########################
        y = [abs(_y) for _y in y] #this contains imaginary part, so take abs

        y_final = list()
        for _y in y:
            if _y <= 1:
                y_final.append(_y)
            else:
                y_final.append(1)

        final_result = list()

        for data,y_prob in zip(input_data,y_final):    
            list_pos = [data, None]
            proportion = [1-y_prob, y_prob]
            original_data = normal_packetloss.random_pick(
                normal_packetloss,
                list_pos, 
                proportion,
            )
            '''change datatype to packetloss_type with type 1 (node failure)
            
            original_data = data_packetloss_type(
                original_data,
                1, #node failure
            )
            '''


            final_result.append(original_data)

        return x,y_final,final_result

import numpy as np
import matplotlib.pyplot as plt
if __name__ == "__main__":
    packetlossTotalSim = packetlossTotalSim()
    input = [10] * 3000
    x, y, final_result = packetlossTotalSim.node_failure_packetloss(
        input,
        0.001,
    )
    print (y)
    # plt.subplot(2,1,1)
    # plt.plot(x,final_result)
    # plt.title('final simulation result')
    # plt.xlabel('time / s')
    # plt.ylabel('IoT sensor value (assumed)')

    plt.subplot(2,1,2)
    plt.plot(x,y)
    plt.title('packet loss possibility change plot')
    plt.xlabel('time / s')
    plt.ylabel('packet loss possibility')
    plt.show()


