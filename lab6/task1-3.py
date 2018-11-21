import pandas as panda
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (10, 5)
contain=panda.read_csv('NYC_Jobs.csv')
 #print(contain[:10])
# print(contain['Agency'][:10])
# print(contain[['Agency','Business Title','Work Location']])

complaint_counts = contain['Agency'].value_counts()
print(complaint_counts)

complaint_counts.plot(kind='bar')
plt.show()