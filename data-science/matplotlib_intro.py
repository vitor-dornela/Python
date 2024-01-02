import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()  # this creates a figure paired with axes

x = np.linspace(0, 10, 200)  # x data
y = np.sin(x) + x            # y data
ax.plot(x, y)                # creates the plot
plt.show()                   # this will show your plot in case your environment is not interactive


fig, ax = plt.subplots(figsize=(8,6)) # length and width of the plot
fig.suptitle('This is the title of the plot', fontsize=20) # title of the plot

color = 'tab:red' # color of the plot
linestyle = 'dashdot'  # style of the plot
linewidth = 2     # width of the plot
ax.plot(x, y, c=color, linestyle=linestyle, linewidth=linewidth)

ax.set_xlabel('argument', fontsize = 10) # x label
ax.set_ylabel('function', fontsize = 10) # y label


x = np.linspace(0, 10, 200)  # x data
y = np.sin(x) + x            # y data

plt.show()                   # this will show your plot in case your environment is not interactive

fig, axes = plt.subplots(1, 2, figsize=(8,6)) # subplots with 1 row and 2 columns
ax1, ax2 = axes

x = np.linspace(0,10,200)
y1 = np.sin(x)
y2 = np.cos(x)

ax1.set_ylabel('sin(x)', fontsize=15)
ax1.set_xlabel('x', fontsize=15)
ax2.set_ylabel('cos(x)', fontsize=15)
ax2.set_xlabel('x', fontsize=15)

fig.tight_layout(pad=2) # this will add some padding between the plots

ax1.plot(x, y1, c='r', linewidth=2)
ax2.plot(x, y2, c='g', linewidth=2)
plt.show()   


fig, ax = plt.subplots()
plt.close()

for i in range(10):
    plt.figure(i)

plt.close('all') # this will close all the figures
plt.show()