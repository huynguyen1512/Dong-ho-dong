import random
import numpy as np
'''khong doi lua chon'''
stay=0 
'''doi lua chon'''
switch=0 
attempt=100000
for i in range(attempt):
    doors = np.array([1,0,0])
    random.shuffle(doors)
    choose = random.randint(0,2)
    possible_doors = [i for i in range(3) if i != choose and doors[i] == 0]
    opened=random.choice(possible_doors)
    remaining=[i for i in range(3) if i != choose and i != opened]
    '''Cua con lai trong truong hop nguoi choi doi cua'''
    if (doors[choose]==1):
        stay +=1
    elif(doors[remaining]==1):
        switch+=1
print("Xac suat trung khi khong doi lua chon la: " + str(stay/attempt*100)+"%")
print("Xac suat trung khi doi lua chon la: " + str(switch/attempt*100)+"%")

