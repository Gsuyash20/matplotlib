import numpy as np
import csv
from collections import Counter
from matplotlib import pyplot as plt

# style
plt.style.use("fivethirtyeight")

with open('D:\Downloads\data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    language_counter = Counter()

    row = next(csv_reader)
    # clean a data a bit
    # print(row['LanguagesWorkedWith'].split(';'))

    for row in csv_reader:
        language_counter.update(row["LanguagesWorkedWith"].split(';'))

languages = []
popularity = []

for item in language_counter.most_common(10):
    languages.append(item[0])
    popularity.append(item[1])

# since the data is too much, so we use horizontal bar plot
# plt.bar(languages, popularity)
languages.reverse()
popularity.reverse()
plt.barh(languages, popularity)

# print(languages)
# print(popularity)
# output
# ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript']
# [59218, 55465, 47544, 36442, 35916, 31991, 27097, 23030, 20524, 18523]


plt.title("Most Popular Languages")
plt.xlabel("Number of People who use")

plt.tight_layout()

plt.show()
