import matplotlib.pyplot as plt
import csv
import numpy as np

x=range(430)
y=[]

with open('data2.txt', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        print row[0]
       
        """x.append(str(row[0]))"""
        y.append(float(row[1]))


plt.plot(x,y, marker='o',ms=2)

plt.title('Intent Event Throughput Based On OpenFlow')

plt.xlabel('Time Points (second)')
plt.ylabel('Throughput (events/second)')
plt.yticks(np.arange(0,10000,step=1000))
plt.grid()


plt.show()
