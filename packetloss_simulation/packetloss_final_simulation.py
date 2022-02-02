import packetloss_nodefailure
import packetloss_normal
from typing import List


nodefailure = packetloss_nodefailure.packetlossTotalSim()
normal = packetloss_normal.normal_packetloss()

class final_simulation_packetloss:
        #this is the proportion by which the sensor can sense but cannot 
        #provide enough communication power, which means that packetloss will 
        #increase to 100%
    def final_simulation(
        battery_power: float,
        sensing_quality_decline_proportion: float,
        original_datalist: List,
    )-> List:
        ''' This algorithm is designed to arrange the three packetloss models

        The first two reasons happen at all time, while node-failure is always
          the last event. These three events are independent of each other.
        '''

        assert isinstance(
          battery_power,
          float,
        ), \
          '''This input battery power should be a float number in years

          e.g. 4.2 years
          '''

        assert isinstance(
          sensing_quality_decline_proportion,
          float,             
        ), \
          '''This input proportion should be a proportion in float

          e.g. 0.7 (70%)
          '''

        assert isinstance(
          original_datalist,
          List,
        ), \
          '''The original dataset should be a List

          e.g. [123, 89, 90, 98 ...]
          '''

        nodefailure.node_failure_packetloss()

        '''link fluctuation:

        Link fluctuation is caused by sudden movement or signal interference
          So that this is fairly caused by a random situation, so that the 
          possibility of triggering this event would be set as a random value.
        '''
        
        possibility_link = 0.01
        link_fail_posibility = packetloss_normal.normal_packetloss.random_pick(
          [0,1],
          [1-possibility_link, possibility_link],
        ) 
        
















