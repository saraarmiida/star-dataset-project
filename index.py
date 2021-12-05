import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

stars = pd.read_csv('./data.csv')

print(stars)

# fig , ax = plt.subplots(figsize = (13,10))

# R = stars[stars["Star type"] == 0]
# B = stars[stars["Star type"] == 1]
# W = stars[stars["Star type"] == 2]
# M = stars[stars["Star type"] == 3]
# S = stars[stars["Star type"] == 4]
# H = stars[stars["Star type"] == 5]

# ax.scatter(np.log(R["Temperature (K)"]), np.log(R["Luminosity(L/Lo)"]),5, label = 'Red dwarfs')
# ax.scatter(np.log(B["Temperature (K)"]), np.log(B["Luminosity(L/Lo)"]),7, label = 'Brown dwarfs')
# ax.scatter(np.log(W["Temperature (K)"]), np.log(W["Luminosity(L/Lo)"]),10, label = 'White dwarfs')
# ax.scatter(np.log(M["Temperature (K)"]), np.log(M["Luminosity(L/Lo)"]),15, label = 'Main sequence stars')
# ax.scatter(np.log(S["Temperature (K)"]), np.log(S["Luminosity(L/Lo)"]),30, label = 'Supergiants')
# ax.scatter(np.log(H["Temperature (K)"]), np.log(H["Luminosity(L/Lo)"]),50, label = 'Hypergiants')

# ax.invert_xaxis()
# ax.legend()
# plt.xlabel("Log Temperature")
# plt.ylabel("Log Luminosity")
# ax.grid()
# ax.set_facecolor("black")