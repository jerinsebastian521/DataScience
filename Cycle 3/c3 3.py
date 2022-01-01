import matplotlib.pyplot as plt
import numpy as np

m = np.array(['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'])
x = np.array([173, 153, 195, 147, 120, 144, 148, 109, 174, 130, 172, 131])
plt.scatter(m, x, color = 'hotpink')

m = np.array(['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'])
y = np.array([189, 189, 105, 112, 173, 109, 151, 197, 174, 145, 177, 161])
plt.scatter(m, y, color = 'yellow')

m = np.array(['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'])
z = np.array([185, 185, 126, 134, 196, 153, 112, 133, 200, 145, 167, 110])
plt.scatter(m, z, color = 'blue')

plt.title("sales data")
plt.xlabel("Months")
plt.ylabel("sales of segments")



plt.show()