import numpy as np; np.random.seed(0)
import seaborn as sns; sns.set_theme()
import random

uniform_data = np.random.rand(10, 12)

ax = sns.heatmap(uniform_data)