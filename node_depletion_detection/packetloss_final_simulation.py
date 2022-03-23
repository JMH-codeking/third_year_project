
from sympy import deg
import packetloss_nodefailure
import packetloss_normal
from typing import List, final


nodefailure = packetloss_nodefailure.packetlossTotalSim()
normal = packetloss_normal.normal_packetloss()

class final_simulation_packetloss:
        #this is the proportion by which the sensor can sense but cannot 
        #provide enough communication power, which means that packetloss will 
        #increase to 100%
    def final_simulation(
        self,
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

        '''split the data into two parts:

        Lossing part and the normal-working part
        '''

        division_point = int(sensing_quality_decline_proportion \
                              * len(original_datalist)
                            )
        normal_packets = original_datalist[:division_point]
        degrading_packets = original_datalist[division_point:]

        final_simulation_result = list()

        '''the two normal loss functions are both for one single packet, and 

        The two situations are independent
        So applied for every single pattern. 
        '''

        for normal_packet in normal_packets:
          normal_packet = normal.packetloss_normal(
            normal_packet,
            [0.0001, 0.01],
          )

          normal_packet = normal_packet.original_data[0]

          normal_packet = normal.packetloss_normal(
            normal_packet,
            [0.0005, 0.005], # assume five times of packetloss rate than normal
            True # trigger link failure
          )

          final_simulation_result.append(normal_packet.original_data[0])
          
        x,y,degrading_packets = nodefailure.node_failure_packetloss(
          degrading_packets,
          0.01,
        )

        final_simulation_result.extend(degrading_packets)
        return final_simulation_result

import matplotlib.pyplot as plt
import numpy as np
if __name__ == "__main__":

  '''create huge amount of datalist for ML classification
  
  basic concept: randomly set the starting proportion of node failure

  random (0.8- 0.95) depending on various situations assumed.
  '''

  dataset_labels = np.arange(1,2000).tolist() 
  '''set 10000 sets for training and testing
  '''

  import random
  loss_rate = [0.85, 0.95]

  final_simulation_packetloss = final_simulation_packetloss()

  for dataset_label in dataset_labels:
    scale = 1000
    start_prop  = loss_rate[0] * scale
    end_prop  = loss_rate[1] * scale
    possibility = random.randint(start_prop, end_prop) / scale

    sensing_quality_proportion = possibility

    x = np.arange(0,30000).tolist()
    input = [10] * 30000

    final_result = final_simulation_packetloss.final_simulation(
      4.2,
      sensing_quality_proportion,
      input
    )

    '''create and store data separately
    '''

    with open(f'datafile_new/datafile{dataset_label}.txt', 'w+') as f:
      f.write(str(possibility) + '\n')
      for _data in final_result:
        f.write(str(_data) + '\n')


  # plt.plot(x,y,marker = ".", markersize=1)
  # plt.xlabel('time / s')
  # plt.ylabel('packetloss (labeled as 10)')
  # plt.title('Plot of packets lost against time (linear increase)')
  # plt.savefig('packetlossVStime_linear.png')
  '''    
  plt.subplot(2,2,1)
  plt.plot(x, final_result)
  plt.xlim(0, 100)
  plt.subplot(2,2,2)
  plt.plot(x, final_result)
  plt.xlim(22500, 22600)
  plt.subplot(2,2,3)
  plt.plot(x, final_result)
  plt.xlim(27400, 27500)
  plt.savefig('simulation_result.png')
  '''