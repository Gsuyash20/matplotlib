from matplotlib import pyplot as plt

# adding the style - use plt.style.available to see all styles
# we don't need to add style manually if we use below cmd
plt.style.use('fivethirtyeight')

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(ages_x, js_dev_y,color='#abab1a', marker='.',linewidth='5', label="JavaScript")
# just plots the data
plt.plot(ages_x, py_dev_y,color='b', marker='.', label="Python")
plt.plot(ages_x, dev_y, color='#0abeef', linestyle='--', label="All Devs")

# Adding the labels
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")

# adding the title
plt.title("Median Salary (USD) by Age")

# adding the legend
plt.legend()

# add a grid
plt.grid(True)

# automatically adjust the plot parameters
plt.tight_layout()

# save the plot manually
# plt.savefig('plot.png')

# used to display the plot
plt.show()
