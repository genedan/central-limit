# start with the uniform distribution, the first discussed in Wackerly

import plotly.express as px

from numpy import mean
from plotly.offline import plot
from scipy.stats import uniform


hist_data = []
for x in range(1000):
    sample = uniform.rvs(loc=0, scale=1, size=5)
    x_bar = mean(sample)
    hist_data.append(x_bar)

fig = px.histogram(hist_data)

plot(fig)

# Increase the sample size, and the distribution will look more normal
for x in range(1000):
    sample = uniform.rvs(loc=0, scale=1, size=1000)
    x_bar = mean(sample)
    hist_data.append(x_bar)

fig2 = px.histogram(hist_data)

plot(fig2)