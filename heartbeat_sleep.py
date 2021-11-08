from typing import List
import random
import matplotlib.pyplot as plt

class sleep_heart():
    def sleep_heartbeat (
        self,
        heart_average: int,
        heartrate_list: List,
        time_hour: int, 
        window: int,
        flow_variance: float
    ):
        '''explanation of parameters

        here the time is counted as days, 
            and actual time should be counted as seconds in the algorithm 
        here the window is the time interval that is expected in seconds
        '''   

        actual_time_second = 3600*time_hour  # actual time in seconds
        '''reference:
        
        https://www.cnet.com/health/sleep/sleeping-heart-rate-breathing-rate-and-hrv-what-your-sleep-data-means/
        '''

        length = int(actual_time_second/window)
        '''assume three stages of sleep: REM, deep and light

        assume 50%-60% in light sleep, followed by deep sleep, and fianlly 20%-25% in rapid eye movement(REM)
        '''
        light_sleep_period = random.randint(length*0.5,length*0.6) #generate a random number for light sleep and deep sleep classification
        rem_period = random.randint(length*0.75,length*0.8) #generate a random number for REM classification

        for i in range (0,light_sleep_period): #here I suppose that a person is in light sleep
            '''reference:

            https://www.researchgate.net/publication/261257673_Heart_Rate_During_Sleep_Implications_for_Monitoring_Training_Status
            '''

            heartrate_list.append(
                random.randint(
                    heart_average*(1-flow_variance), 
                    heart_average*(1+flow_variance),
                )*0.9  # assume that people's heart rate during sleep is 0.9 times the normal
            )
            print ("i")
        for i in range (light_sleep_period,rem_period):# here light and rem has a transition of deep sleep
            heartrate_list.append(
                random.randint(
                    heart_average*(1-flow_variance), 
                    heart_average*(1+flow_variance),
                )*0.9*0.8  # assume that people's heart rate during deep sleep is 0.8 times light sleep
            )
            print ("j")
        for i in range(rem_period,length): # rem sleep
            heartrate_list.append(
                random.randint(
                    heart_average*(1-flow_variance), 
                    heart_average*(1+flow_variance),
                )*0.9  # assume that people's heart rate during rem sleep is 0.9 times the normal random, 
                        #and may soar but not exceed normal
            )
            print ("k")
        ''' here set the value of variance to +- 10% of possible average for normal
        '''

        return (list(heartrate_list), length)

if __name__ == "__main__":
    heart_average = 80 # assume that average heart rate is 
    heartrate_list = list() # create a list that is empty
    time_hour = 9 # 2 days
    window = 4 # 4 seconds
    sleep_heart = sleep_heart()
    heartrate_sleep, time_length = sleep_heart.sleep_heartbeat(
        heart_average, 
        heartrate_list, 
        time_hour, 
        window,
        0.1, # assume 10% varying of heartbeat data
    )
    time_x = [window*i for i in range(0,time_length)]
    plt.figure()
    plt.plot(time_x, heartrate_sleep)
    plt.show()
    plt.savefig('./final_output/sleepmode.png')
    #plt.plot(time_x, np.transpose(final))