from typing import List
import random
import numpy as np
import matplotlib.pyplot as plt
class normal_packetloss:
    def random_pick(
        self,
        some_list, 
        probabilities
    ): 
        x = random.uniform(0,1) 
        cumulative_probability = 0.0 
        for item, item_probability in zip(some_list, probabilities): 
            cumulative_probability += item_probability 
            if x < cumulative_probability:
                break 
        return item 
    def paceketloss_normal (
        self,
        original_data: int,
        loss_rate: List,
    ):
        scale = 10000
        start_prop  = loss_rate[0] * scale
        end_prop  = loss_rate[1] * scale

        '''explanation of this algorithm

        For this algorithm, we set a random range of signal loss, 
        To maintain a random possibility, I take the random function
        e.g. to achieve a 10% I would choose if (random.ranint(1,10) == 1)
        '''

        possibility = random.randint(start_prop, end_prop) / scale

        list_pos = [original_data, None]
        proportion = [1-possibility, possibility]
        original_data = self.random_pick(list_pos, proportion)
        return original_data

if __name__ == "__main__":
    normal_packetloss = normal_packetloss()
    x = np.arange(0,100,1,dtype = int)
    y = np.sin(x)
    plt.subplot(1,2,1)
    plt.plot(x,y)
    plt.xlabel('x',fontsize=20)
    plt.ylabel('y',fontsize=20)
    plt.title('original data',fontsize=20)
    final_list = list()
    for data in y:
        data = normal_packetloss.paceketloss_normal(
                data, 
                [0.001, 0.1],
            )
        final_list.append(data)
    import matplotlib.pyplot as plt
    print (final_list)
    plt.subplot(1,2,2)
    plt.plot(x,final_list)
    plt.xlabel('x',fontsize=20)
    plt.ylabel('y',fontsize=20)
    plt.title('missing data',fontsize=20)
    plt.show()
    while None in final_list:
        final_list.remove(None)