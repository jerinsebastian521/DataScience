import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri'])
y = np.array([300, 450, 150, 400, 650])

plt.subplot(2, 1, 1)
plt.title("sales data 1", loc ='right')
plt.xlabel("Days of week")
plt.ylabel("sales of drink")
plt.plot(x,y,'o:',color = 'cyan', marker ='H', mec = 'k', mfc ='m')
plt.grid(color = 'blue', linestyle = '--')

#plot 2:
x = np.array(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri'])
y = np.array([400, 500, 350, 300, 500])

plt.subplot(2, 1, 2)
plt.title("sales data 2")
plt.xlabel("Days of week")
plt.ylabel("sales of food")
plt.plot(x,y,'o--',color = 'y', marker ='D', mec = 'r', mfc ='g')

plt.grid(color = 'blue', linestyle = '--')
plt.subplots_adjust(top=2.5, bottom=1.5, wspace=0.4, hspace=0.4)
plt.show()