import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

# style
plt.style.use("fivethirtyeight")

data = pd.read_csv('D:\Downloads\data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(10):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()
plt.barh(languages, popularity)

plt.title("Most Popular Languages")
plt.xlabel("Number of People who use")

plt.tight_layout()

plt.show()