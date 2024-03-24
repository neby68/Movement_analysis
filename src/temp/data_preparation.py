import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px



df = pd.read_csv(r"data\NONAN_Gaitprint\S001\S001\S001_G01_D01_B01_T01.csv")
print(df.info())
df.shape


list(df.columns)

col_to_keep = [
'time',
'Foot Accel Sensor X RT (mG)',
'Foot Accel Sensor Y RT (mG)',
'Foot Accel Sensor Z RT (mG)',
'Noraxon MyoMotion-Segments-Foot RT-Acceleration-x (mG)',
'Noraxon MyoMotion-Segments-Foot RT-Acceleration-y (mG)',
'Noraxon MyoMotion-Segments-Foot RT-Acceleration-z (mG)',
'Noraxon MyoMotion-Segments-Foot RT-Gyroscope-x (deg/s)',
'Noraxon MyoMotion-Segments-Foot RT-Gyroscope-y (deg/s)',
'Noraxon MyoMotion-Segments-Foot RT-Gyroscope-z (deg/s)'
]

df = df.head(1000)
df = df[col_to_keep]

df.head()

fig = px.line(df, y=col_to_keep, x='time')
fig.write_html(r"output\raw_datas.html")

plt.plot(df["Foot Accel Sensor Z RT (mG)"])
start = 400
stop = 650

df.iloc[start:stop, :].to_csv(r"data\NONAN_Gaitprint\S001\S001\S001_1_cycle.csv")