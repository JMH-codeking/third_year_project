from typing import List
import random
import matplotlib.pyplot as plt

class exercise_heart():
    def exercise_heartbeat (
        self,
        heart_average: int,
        heartrate_list: List,
        time_minute: int, 
        window: int,
        variance: float
    ):
        '''explanation of parameters

        here the time is counted as days, and actual time should be counted as seconds in the algorithm
        here the window is the time interval that is expected in seconds
        '''   

        actual_time_second = 60*time_minute  # actual time in seconds
        length = int(actual_time_second/window)
        for i in range(0,length):
            normal_heartrate = random.randint(
                heart_average*(1-variance),
                heart_average*(1+variance),
            )
            heartrate_list.append(
                random.randint(
                    int(normal_heartrate*0.9), 
                    int(normal_heartrate*1.1),
                )
            )
            ''' here set the value of variance to above 50% of possible average
            '''

        return list(heartrate_list)

if __name__ == "__main__":
    heart_average = 80 # assume that average heart rate is 
    heartrate_list = list() # create a list that is empty
    time_minute = 60 # one hour
    window = 4 # 4 seconds
    exercise_heart = exercise_heart()
    heartrate_normal = exercise_heart.exercise_heartbeat(
        heart_average, 
        heartrate_list, 
        time_minute, 
        window,
        0.1,
    )
    time_length = int(time_minute*60/window)
    time_x = [window*i for i in range(0,time_length)]
    plt.figure()
    plt.plot(time_x, heartrate_normal)
    plt.show()
    plt.savefig('./final_output/exercise.png')
    #plt.plot(time_x, np.transpose(final))z