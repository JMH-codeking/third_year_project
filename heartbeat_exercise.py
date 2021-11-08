from typing import List
import random
import matplotlib.pyplot as plt

class exercise_heart():
    def exercise_heartbeat (
        self,
        heart_average: int,
        heartrate_list: List,
        time_day: int, 
        window: int,
        flow_variance: float
    ):
        '''explanation of parameters

        here the time is counted as days, and actual time should be counted as seconds in the algorithm
        here the window is the time interval that is expected in seconds
        '''   

        actual_time_second = 3600*24*time_day  # actual time in seconds
        length = int(actual_time_second/window)
        for i in range(0,length):
            heartrate_list.append(random.randint(heart_average*0.9, heart_average*1.1))
            ''' here set the value of variance to +- 10% of possible average
            '''

        return (list(heartrate_list), length)

if __name__ == "__main__":
    heart_average = 80 # assume that average heart rate is 
    heartrate_list = list() # create a list that is empty
    time_day = 0.1 # 2 days
    window = 4 # 4 seconds
    normal_heart = normal_heart()
    heartrate_normal, time_length = normal_heart.normal_heartbeat(
        heart_average, 
        heartrate_list, 
        time_day, window
    )
    time_x = [window*i for i in range(0,time_length)]
    plt.figure()
    plt.plot(time_x, heartrate_normal)
    plt.show()
    plt.savefig('a.png')
    #plt.plot(time_x, np.transpose(final))z