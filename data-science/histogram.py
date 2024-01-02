import matplotlib.pyplot as plt
        # creates the plot



plt.figure(1)
data = [163, 163, 164, 170, 170, 172, 173, 190]
plt.hist(data)


plt.figure(2)
plt.hist(data, color='g', edgecolor='k')
plt.title("My friends heights")
plt.ylabel("Number of friends")
plt.xlabel("Height")


plt.figure(3)
bins = [160, 170, 180, 190]
plt.hist(data, bins=bins, color='g', edgecolor='k')


#plt.show()


fig, ax = plt.subplots(1, 2)  # create a figure with 1 row and 2 columns of subplots

ax[0].hist(data)  # plot histogram on the first subplot
ax[0].set_title("Histogram of Data")
ax[0].set_xlabel("Value")
ax[0].set_ylabel("Frequency")

ax[1].hist(data, bins=bins, color='g', edgecolor='k')  # plot boxplot on the second subplot
ax[1].set_title("My friends heights")
ax[1].set_xlabel("Data")

plt.tight_layout()  # adjust the spacing between subplots
plt.show()


fig, ax = plt.subplots(1, 2)

my_data = [163, 163, 164, 170, 170, 172, 173, 190]
andy_data = [161, 172, 174, 175, 181, 183, 186, 190]
bins = [160, 170, 180, 190]
names = ["my friends", "Andy's friends"]

ax[0].hist([my_data, andy_data], bins=bins, label=names, color=['g', 'b'], edgecolor='k')
ax[0].set_title("Mine and Andy's friends' height")
ax[0].set_ylabel("Number of people")
ax[0].set_xlabel("Height in cm")
ax[0].legend()

ax[1].hist([my_data, andy_data], bins=bins, label=names, stacked=True, edgecolor='w')
ax[1].set_title("Mine and Andy's friends' height")
ax[1].set_ylabel("Number of people")
ax[1].set_xlabel("Height in cm")
ax[1].legend()

plt.show()

