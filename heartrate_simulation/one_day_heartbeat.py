import random
from typing import List

from heartbeat_normal import normal_heart
from heartbeat_exercise import exercise_heart
from heartbeat_sleep import sleep_heart


class one_day():
    def possibilty_normal_sleep(
        self,
        arr1,
        arr2,
    ):
        '''parameters:

        arr1 is the list of possible values
        arr2 is the possibility of each possible value
        '''

        assert len(arr1) == len(arr2), "Length does not match."
        assert sum(arr2) == 1 , "Total rate is not 1."

        sup_list = [len(str(i).split(".")[-1]) for i in arr2]
        top = 10 ** max(sup_list)
        new_rate = [int(i*top) for i in arr2]
        rate_arr = []
        for i in range(1,len(new_rate)+1):
            rate_arr.append(sum(new_rate[:i]))
            rand = random.randint(1,top)
            data = None
        for i in range(len(rate_arr)):
            if rand <= rate_arr[i]:
                data = arr1[i]
                break
        return data

    def heartbeat_oneday(
        self,
        heartrate: List,
        average_heartrate: int,
        window: int,
        variance_normal: float,
    ):
        sleep = sleep_heart()
        normal = normal_heart()
        exercise = exercise_heart()
        arr_mode = [0,1] 
        #here I assume that 0 is normal condition, and 1 is exercise condition
        arr_possibility = [0.7,0.3] 
        # here I assume that normal condition is more possible, at 70%
        sleep_cycle_number = random.randint(4,6)
        sleep_period = list()
        for i in range(0,sleep_cycle_number):
            sleep_cycle = random.randint(90,110);
            sleep_period.append(sleep_cycle)

        sleep_time_length = sum(sleep_period) #total time of sleep

        sleep_time = random.randint(22*60, 24*60)
        wakeup_time = sleep_time+sleep_time_length-24*60
        '''here, choice is for one hour
        '''

        for time in range(wakeup_time,sleep_time):
            choice = self.possibilty_normal_sleep(arr_mode, arr_possibility)
            if choice: #zero is normal condition"
                normal.normal_heartbeat(
                    average_heartrate,
                    heartrate,
                    1,
                    window,
                    variance_normal,
                )
            else:
                exercise.exercise_heartbeat(
                    average_heartrate,
                    heartrate,
                    1,
                    window,
                    variance_normal,
                )

        '''full sleep cycle assume to be a random number of 90-110, which is 1.5 - 1.8h

        https://my.clevelandclinic.org/health/articles/12148-sleep-basics
        '''
        
        for i in range (0,sleep_cycle_number):
            sleep_length = sleep_period[i]
            sleep.sleep_heartbeat(
                average_heartrate,
                heartrate,
                int(sleep_length),
                window,
                variance_normal,
            )
        return heartrate

if __name__ == "__main__":
    window = 4
    variance_normal = 0.1
    normal_heartrate = 70
    heartrate = list()
    one_day = one_day()
    one_day.heartbeat_oneday(
        heartrate,
        normal_heartrate,
        window,
        variance_normal,
    )
    print (len(heartrate))
    
    
            


        
    
