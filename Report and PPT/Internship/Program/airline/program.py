import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler

from keras._tf_keras.keras.models import Sequential
from keras._tf_keras.keras.layers import Dense
from keras import metrics

df = pd.read_csv("AirPassengers.csv")

# print(df.iloc[:,1])

L = len(df)
X = np.array([range(1,L)])
Y = np.array([df.iloc[:,1]])

Y = Y[:,0:L-1]

plt.figure(1)
plt.plot(X[0,:],Y[0,:])
plt.show(block=False)

X1 = Y[:,0:L-4]
X2 = Y[:,1:L-3]
X3 = Y[:,2:L-2]


print(X1.shape,X2.shape,X3.shape)

X = np.concatenate([X1,X2,X3],axis=0)
X = np.transpose(X)
Y = np.transpose(Y[:,3:L-1])
print(X.shape,Y.shape)

scaler = MinMaxScaler()
scaler.fit(X)
X = scaler.transform(X)


scaler1 = MinMaxScaler()
scaler1.fit(Y)
Y = scaler1.transform(Y)

model = Sequential()

model.add(Dense(32,activation='relu',input_dim=3))

model.add(Dense(32,activation='relu'))

model.add(Dense(1,activation='sigmoid'))

model.compile(loss="mean_squared_error",optimizer='rmsprop',metrics=[metrics.mean_squared_error])

model.fit(X,Y, epochs = 500, batch_size=32 ,verbose=2)

predict = model.predict(X,verbose=1)
print(Y,predict)

plt.figure(2)
plt.scatter(Y,predict)
plt.show(block=False)

plt.figure(3)
Test = plt.scatter(X[:,0],Y)
Predict = plt.scatter(X[:,0],predict)
plt.legend([Predict,Test],["Predict Data","Real Data"])

plt.show()