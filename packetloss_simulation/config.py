'''This file is for setting configuration to the algorithm
'''

from enum import Enum
from typing import Dict, List

class data_packetloss_type:
    def __init__(
        self,
        original_data: int,
        packetloss_type: List,
    ):
        '''packetloss type: 0 -1 1

        -1 is normal reason, 0 in link fluctuation, 1 is node failure
        '''

        assert isinstance(
            packetloss_type,
            List
        ), \
            '''Must be a List for the packetloss reason
            '''

        self.original_data = original_data,
        self.packetloss_type = packetloss_type

if __name__ ==  "__main__":
    data = [1,2,2]
    tf = [0,0,1,-1]
    data_list = list()
    for data, tf in zip(data, tf):
        data_total = data_packetloss_type(
            data,
            tf
        )
        data_list.append(data_total)

    print (data_list[1].packetloss_type)




        
        