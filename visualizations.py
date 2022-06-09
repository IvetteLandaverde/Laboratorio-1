
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: visualizations.py : python script with data visualization functions                         -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: THE LICENSE TYPE AS STATED IN THE REPOSITORY                                               -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import numpy as np
import pandas as pd
import plotly.graph_objects as go 

def plot_orderbook():
    """
    Limit OrderBook horizontal bars plot.

    Parameters
    __________


    Returns
    _______


    References
    __________
    """
    fig_ob=go.Figure()
    pass

# ====================================

def plot_publictrades():
    """
    Public Trades horizontal bars + traded price plot.

    Horizontal Colored-Bars (y-axis is volume, bar color is side) + line (traded price) with
    y-axis: volume, y1-axis: traded price, x-axis: timestamp

    Parameters
    __________


    Returns
    _______


    References
    __________
    """
    fig_ob=go.Figure()
    pass

# ----------- PUBLIC TRADES --------- #
import plotly.graph_objects as go
from plotly.subplots import make_subplots

 

# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig.add_trace(go.Scatter(x=data_x, y=data_y, name="traded price"),secondary_y=False,)
 

fig.add_trace(
    go.Bar(x=data_x, y=data_y1, name="volume"),
    secondary_y=True,
)

# Add figure title
fig.update_layout(title_text="Trades publicos")

# Set x-axis title
fig.update_xaxes(title_text="Timestamp")

# Set y-axes titles
fig.update_yaxes(title_text="<b>Traded Price</b> <br> BTC/USDT", secondary_y=False)
fig.update_yaxes(title_text="<b>Volume</b> <br> BTC", secondary_y=True)

fig.update_layout(legend_orientation='h', xaxis=dict(ticktext=list(data_pt['timestamp'])[0:499]) )

fig.show()