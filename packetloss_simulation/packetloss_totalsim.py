from packetloss_normal import normal_packetloss

from typing import List
import random

'''the principle for this function 

'''
class packetlossTotalSim:
    def final_simulation_packetloss(
        self,
        simulation_time: float,
        input_data: List,
        possibility: float, 
        #this is a float number not a percentage
    ): 
        assert isinstance(possibility, float), \
            '''This input possibility should be 
            a float number
            '''

        assert isinstance(simulation_time, float), \
            '''This input is not a float
            '''

        assert isinstance(input_data, List), \
            '''This input data should be a list
            '''

        list_pos = [input_data, None]
        proportion = [1-possibility, possibility]
        original_data = self.random_pick(list_pos, proportion)
        return original_data

        normal_packetloss.random_pick()

if __name__ == "__main__":
    packetlossTotalSim = packetlossTotalSim()

