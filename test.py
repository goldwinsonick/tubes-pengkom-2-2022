import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("daily_weather_data.csv")
print(df)
df.plot(kind="line")
plt.show()