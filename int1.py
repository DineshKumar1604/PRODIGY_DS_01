import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data=pd.read_csv(r"C:\Users\Asus\PycharmProjects\pythonProject\int1\adult.csv")
print(data.head())
age=data['age']
print(age)

mean_age = np.mean(age)
print('Average age of the population:',mean_age)

plt.figure(figsize=(10,6))
plt.hist(age,bins=10,edgecolor='black',alpha=0.7)
plt.title('Visualzition of Age in a population')
plt.xlabel('Age')
plt.ylabel('workclass')
plt.show()