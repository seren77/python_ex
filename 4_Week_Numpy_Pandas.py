import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


list=np.random.rand(50) # 문제 1)
print(list)
data=pd.Series(list) #문제 2)
plt.plot(data)
plt.show() #문제 3)
plt.hist(data)
plt.show #문제 4)