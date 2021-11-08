#! /usr/bin/python3
import matplotlib.pyplot as plt
from heartbeat_normal import normal_heart

if __name__ == "__main__":
    heart_average = 80 # assume that average heart rate is 
    heartrate_list = list() # create a list that is empty
    time_day = 0.1 # 2 days
    window = 4 # 4 seconds
    normal_heart = normal_heart()
    heartrate_normal, time_length = normal_heart.normal_heartbeat(
        heart_average, 
        heartrate_list, 
        time_day, 
        window,
        0.1, # assume 10% varying of heartbeat data
    )
    time_x = [window*i for i in range(0,time_length)]
    plt.figure()
    plt.plot(time_x, heartrate_normal)
    plt.show()
    plt.savefig('./final_output/final_simulation.png')