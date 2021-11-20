"""game guess number"""

import numpy as np

number = np.random.randint(1, 101) # make num

#num of counts
count = 0

while True:
    count+=1
    predict_number = int(input("guess num from 1 to 100: "))
    
    if predict_number > number:
        print("should be less")
        
    elif predict_number < number:
        print("should be more")
        
    else:
        print(f"you won, its = {number}, for {count} steps")
        break # end of the game and exit from cycle