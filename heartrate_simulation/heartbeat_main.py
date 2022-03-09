#! /usr/bin/python3
import matplotlib.pyplot as plt
from one_day_heartbeat import one_day
import pathlib
import os

_parent = pathlib.Path(__file__).parent
if __name__ == "__main__":
    one_day = one_day()
    days = 1
    heart_average = 80 # assume that average heart rate is 80
    heartrate_list = list() # create a list that is empty
    window = 60 # 4 seconds
    variance_normal = 0.1
    for i in range(0,days):
        one_day.heartbeat_oneday(
            heartrate_list,
            heart_average,
            window,
            variance_normal,
        )
    time_length = int(86400*days/window)
    time_x = [window*i for i in range(0,time_length)]
    plt.figure()
    plt.plot(time_x, heartrate_list)
    # os.system(f"rm {_parent}/final_output/*")
    plt.savefig(f'{_parent}/final_output/final_simulation.png')