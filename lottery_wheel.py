import random
import time

def lottery_wheel(lottery_list): 
    hit_list = []
    for lottery_user in lottery_list:
        number = random.randint(1, 100)

        if number == 1:
            #あたり
            hit_list.append(lottery_user)
    if len(hit_list) == 0:
        print("当選者０人")
    else :   
        print("当選者")
        for hit_user in hit_list:
            print(hit_user)
    return hit_list
