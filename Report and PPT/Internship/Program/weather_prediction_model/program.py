import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

from keras._tf_keras.keras.models import Sequential
from keras._tf_keras.keras.layers import Dense
from keras import metrics

df = pd.read_csv("L A_Weather.csv")
print(df.shape)


Tavg  =np.array([df.iloc[:,3]])
Tmax = np.array([df.iloc[:,4]])
Tmin = np.array([df.iloc[:,5]])

# print(Tavg.shape)
fig = plt.figure(1)
ax=fig.add_subplot(111,projection="3d")

ax.scatter(Tmax,Tmin,Tavg,marker='o')
ax.set_xlabel('Max Temp')
ax.set_ylabel('Min Temp')
ax.set_zlabel('Average Temp')
plt.show(block = False)


Temp = np.concatenate([Tmax,Tmin],axis=0)
Temp = np.transpose(Temp)
Tavg = np.transpose(Tavg)
scaler = MinMaxScaler()
scaler.fit(Temp)
Temp = scaler.transform(Temp)
scaler1 = MinMaxScaler()
scaler1.fit(Tavg)
Tavg = scaler1.transform(Tavg)

X_train, X_test, Y_train, Y_test = train_test_split(Temp,Tavg,test_size=0.3)

model = Sequential()
model.add(Dense(32,activation='relu',input_dim=2))
model.add(Dense(32,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss = 'mean_squared_error',optimizer='rmsprop',metrics=[metrics.mean_absolute_error])
model.fit(X_train,Y_train,epochs=500,batch_size=32,verbose=2)
predict = model.predict(X_test,verbose=1)

plt.figure(2)
plt.scatter(Y_test,predict)
plt.show(block= False)

plt.figure(3)
Test = plt.plot(Y_test)
Predict = plt.plot(predict)
plt.legend([Predict,Test],["Predicted Data","Real Data"])
plt.show()