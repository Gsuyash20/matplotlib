import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn-v0_8')

data = pd.read_csv('D:/downloads/data_scat.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter(view_count, likes, c=ratio, cmap='summer',
            edgecolors='black', linewidths=1, alpha=0.75)

plt.xscale('log')
plt.yscale('log')
cbar = plt.colorbar()
cbar.set_label('Like/Dislike Ratio')

plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.tight_layout()

plt.show()
