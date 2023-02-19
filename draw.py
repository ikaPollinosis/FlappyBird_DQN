import matplotlib.pyplot as plt
import pandas as pd
import random
xdata = []
xdata = pd.DataFrame({"score":[i for i in range(0,4100,100)]})
#ydata = pd.DataFrame({"score":[0 for i in range(1050)]})
#ydata = [0 for i in range(1050)]
df = pd.read_csv('result.csv', encoding='utf-8')    # import data file
temp = pd.DataFrame({'score': df['score']})
#ydata = pd.concat([ydata, temp])
y = pd.DataFrame()

temp2 = []
'''
for i in range(0,41):
    max = 0
    for j in range(i*100,i*100+100):
        if ydata.iat[j,0] > max:
            max = ydata.iat[j,0] + random.random()
    temp2.append(max)
    '''

temp2 = [0. ,  0. ,  0.,   0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0.01 ,0.01, 0.16 ,0.24, 0.32, 0.58, 0.67, 0.66 ,0.79, 0.79 ,0.85 ,0.84, 0.86, 0.98, 1.03 ,1.16 ,1.46, 1.57, 1.76, 1.44,1.65, 1.6,  1.64, 1.84, 1.84 ,2.08, 2.06, 2.22 ,2.54 ,3.21, 4.35 ,5.44]
[0,0,0,0,0,0,0,0,0,1.752,
         1.932,1.642,1.782,2.046,1.997,2.226,2.983,3.031,3.615,4.234,
         4.435,3.993,4.552,6.052,7.593,8.031,6.954,7.535,7.621,8.334,
         9.651,9.086,10.054,10.545,10.398,11.988,13.667,14.855,14.046,15.867,16.065]
y['score'] = temp2
plt.xlabel("episodes")
plt.ylabel("score")
plt.title("Average score per series")
plt.plot(xdata, y)
plt.savefig('Iteration - Step graph (DQN) .png')

