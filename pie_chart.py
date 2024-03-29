from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

# use a bar chart for a large data
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
# explode separates that particular data which has different value than 0
explode = [0, 0, 0, 0.2, 0.1]

plt.pie(slices, labels=labels, explode=explode, shadow=True, startangle=90, autopct='%1.1f%%',
        wedgeprops={'edgecolor': 'black'})

plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()
