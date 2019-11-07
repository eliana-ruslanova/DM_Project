

import pandas as pd
import random
# read original dataset
data = pd.read_csv('Amazon_Unlocked_Mobile.csv')

# choose 10 000 random reviews without replacement
data_random_10000 = data.sample(n=10000)

# choose 1000 reviews for labelling from new subset
data_random_1000 = data_random_10000.sample(n=1000)

# delete reviews for labelling from the subset
data_without_random = data_random_10000.drop(data_random_1000.index)

# save datasets to csv files
data_without_random.to_csv(r'C:\Users\linar\OneDrive\Desktop\STUDY\Data Mining I\DM project\data_without_random_samples.csv')
data_random_1000.to_csv(r'C:\Users\linar\OneDrive\Desktop\STUDY\Data Mining I\DM project\random_data_1000.csv')
