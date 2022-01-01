import matplotlib.pyplot as plt
import numpy as np

x = np.array(["walking", "cycling", "car", "bus","train"])
y = np.array([29, 15, 35, 18,3])

plt.title("mode of transport")
plt.xlabel("transport")
plt.ylabel("frequency")

plt.bar(x,y,width=.1,color='g')
plt.show()