from time import sleep
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
df = pd.read_csv('1.csv')
df.head()


# Python
m = Prophet()
m.fit(df)
future = m.make_future_dataframe(periods=365)
future.tail()
forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
fig1 = m.plot(forecast)
fig2 = m.plot_components(forecast)
plt.show()
# from prophet.plot import plot_plotly, plot_components_plotly

# plot_plotly(m, forecast)