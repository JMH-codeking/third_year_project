import random
from typing import List
from collections import defaultdict

class one_day():
    def possibilty_heartrate(
        self,
        arr1,
        arr2,
    ):
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

    def heartbeat_oneday():
        '''full sleep cycle assume to be a random number of 90-110, which is 1.5 - 1.8h

        https://my.clevelandclinic.org/health/articles/12148-sleep-basics
        '''

        #assume that a cycle of a day starts at 8:00 when the first activity would not be sleeping

        return 0

if __name__ == "__main__":
    one = one_day();
    arr = [0,1,2]
    arr2 = [0.2,0.5,0.3]
    list1 = list();   
    for i in range(10000):
        list1.append(one.possibilty_heartrate(arr,arr2))

    counter = defaultdict(int)
    for number in list1:
        counter[number]+=1
    print (counter)

        
    
