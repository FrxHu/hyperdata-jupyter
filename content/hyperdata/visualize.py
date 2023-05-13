from hyperdata.db import read_table,load_credentials
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import HTML
from matplotlib.animation import FuncAnimation, ArtistAnimation, Animation

def animate(stream_name,df):

    def update(num, column_name, step_size):
        index = num * step_size
        ax.clear()
        ax.plot(df["timestamp"][:index:step_size], df[column_name][:index:step_size], marker='o', linestyle='-')
        ax.set_title(f"Time Series Animation: Step {num}, Column: {column_name}")
        plt.xticks(rotation=45)
        plt.xlabel("timestamp")
        plt.ylabel(column_name)

  
    fig, ax = plt.subplots()
    step_size = max(1, len(df) // 25)
    num_frames = (len(df) + step_size - 1) // step_size
    ani = FuncAnimation(fig, update, frames=num_frames, fargs=(stream_name, step_size), interval=100, repeat=False)
    HTML(Animation.to_jshtml(ani))
