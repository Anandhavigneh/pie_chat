import matplotlib.pyplot as plt
import numpy as np

y=np.array([35, 25, 25, 15])
datas=['Bitcoin','Ethereum','IOTX','NEON']

plt.pie(y, labels=datas, startangle=90, autopct='%1.1f%%', shadow=True)
plt.title('Cryptocurrency Market Share')
plt.show()