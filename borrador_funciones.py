"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: functions.py : python script with general functions                                         -- #
# -- author: IvetteLandaverde                                                                       -- #
# -- license:                                              -- #
# -- repository: https://github.com/IvetteLandaverde/Laboratorio-1                                                                   -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

"""
An order book represents the list of buy orders and the list of sell orders 
for a given market organized by price level. 
In this context, a buy order or sell order indicates the amount of 
the base asset that a buyer or seller wishes to trade for a spot market or 
the amount of contracts for a derivatives market.
"""

# importar librerías: 
import numpy as np
import pandas as pd
import data as dt

# -------------------------------------- ORDER BOOKS ----------------------------------------- #

# Read input data
# aquí ya se alimenta del otro archivo
data_ob=dt.ob_data

# -----OB Metrics: ----- #

# -- (1) Median Time of orderBook update -- #
def median_time_OB(data_ob: dict = None) -> True:
    """
    Median Time of Order Book Update
    This function finds the median time of OB
    
    Parameters
    ----------

    Returns
    -------
    ob_m1 : Median Time 
    """
    ob_ts = list(data_ob.keys())
    l_ts = [pd.to_datetime(i_ts) for i_ts in ob_ts]
    ob_m1 = np.median([l_ts[n_ts+1]-l_ts[n_ts] for n_ts in range(0, len(l_ts)-1)]).total_seconds()*1000
    return ob_m1

# -- (2) Spread -- #
def spread_OB(data_ob: dict = None) -> True:
    """
    This function finds 
    
    Parameters
    ----------

    Returns
    -------
    ob_m1 : 
    """
    ob_ts = list(data_ob.keys())
    l_ts = [pd.to_datetime(i_ts) for i_ts in ob_ts]
    ob_m2 = [data_ob[ob_ts[i]]["ask"][0]- data_ob[ob_ts[i]]["bid"][0] for i in range (0,len(ob_ts))]
    return ob_m2

# -- (3) Midprice -- #
def midprice_ob(data_ob: dict = None) -> True:
    """
    This function finds 
    
    Parameters
    ----------

    Returns
    -------
    ob_m1 : 
    """
    ob_ts = list(data_ob.keys())
    ob_m3= [(data_ob[ob_ts[i]]["ask"][0]+data_ob[ob_ts[i]]["bid"][0])*0.5 for i in range(0,len(ob_ts))]
    return ob_m3

# -- (4) No. Price Levels --#
def price_levels_OB(data_ob: dict = None) -> True:
    """
    This function finds 
    
    Parameters
    ----------

    Returns
    -------
    ob_m1 : 
    """
    ob_ts = list(data_ob.keys())
    ob_m4 = [data_ob[i_ts].shape[0] for i_ts in ob_ts]
    return ob_m4

# -- (5) Bid Volume --#
def bid_volume_OB(data_ob: dict = None) -> True:
    """
    This function finds 
    
    Parameters
    ----------

    Returns
    -------
    ob_m1 : 
    """
    ob_ts = list(data_ob.keys())
    ob_m5 = [np.round(data_ob[i_ts]["bid_size"].sum(),6) for i_ts in ob_ts]
    return ob_m5

# -- (6) Ask Volume -- #
def ask_volume_OB(data_ob: dict = None) -> True:
    """
    This function finds 
    
    Parameters
    ----------

    Returns
    -------
    ob_m1 : 
    """
    ob_ts = list(data_ob.keys())
    ob_m6 = [np.round(data_ob[i_ts]["ask_size"].sum(),6) for i_ts in ob_ts]
    return ob_m6

# -- (7) Total Volume -- #
def total_volume_OB(data_ob: dict = None) -> True:
    """
    This function finds 
    
    Parameters
    ----------

    Returns
    -------
    ob_m1 : 
    """
    ob_ts = list(data_ob.keys())
    ob_m7 = [np.round(data_ob[i_ts]["bid_size"].sum() + data_ob[i_ts]["ask_size"].sum(),6)for i_ts in ob_ts]
    return ob_m7

# -- (8) Volume Imbalance -- #
# ob_m8 = [bid_volume / (bid_volume + ask_volume)]
def volume_imbalance_OB(data_ob: dict = None) -> True:
    """
    This function finds 
    
    Parameters
    ----------

    Returns
    -------
    ob_m1 : 
    """
    ob_ts = list(data_ob.keys())
    ob_m5 = [np.round(data_ob[i_ts]["bid_size"].sum(),6) for i_ts in ob_ts]
    ob_m6 = [np.round(data_ob[i_ts]["ask_size"].sum(),6) for i_ts in ob_ts]
    bid_volume = np.sum(ob_m5)
    ask_volume = np.sum(ob_m6)
    ob_m8 = [bid_volume/ (bid_volume + ask_volume)]
    return ob_m8


# -- (9) Weighted Midprice (A)-- TOB #
# W-MidPrice(A) = OrderBook Imbalance * MidPrice
# W-MidPrice(A) = [bid_volume[0] / (bid_volume[0] + ask_volume[0])] * (bid_price[0] + ask_price[0])/2
def WMA_OB(data_ob: dict = None) -> True:
    """
    This function finds 
    
    Parameters
    ----------

    Returns
    -------
    ob_m1 : 
    """
    ob_ts = list(data_ob.keys())
    ob_m5 = [np.round(data_ob[i_ts]["bid_size"].sum(),6) for i_ts in ob_ts]
    ob_m6 = [np.round(data_ob[i_ts]["ask_size"].sum(),6) for i_ts in ob_ts]
    ob_part1 = ob_m5[0] / (ob_m5[0] + ob_m6[0])
    ob_part2 = [data_ob[ob_ts[i]]["ask"][0]- data_ob[ob_ts[i]]["bid"][0] for i in range (0,len(ob_ts))][0]/2
    ob_m9 = np.round(ob_part1*ob_part2,4)
    return ob_m9

# puntos extra:
# -- (10) Weighted Midprice (B) -- #
# W-MidPrice(B) = [ask_volume / total_volume]*bid_price + [bid_volume/(total_volume)]*ask_price
# W-MidPrice(B) = (v[1]/np.sum(v[0] + v[1]))*p[0] + (v[0]/np.sum(v[0] + v[1]))*p[1]


# -- (11) Volume-Weighted Average Price -- #
#  VWAP

def VWA_price_OB(data_ob: dict = None) -> True:
    """
    This function finds 
    
    Parameters
    ----------

    Returns
    -------
    ob_m1 : 
    """
    ob_ts = list(data_ob.keys())
    ob_m3= [(data_ob[ob_ts[i]]["ask"][0]+data_ob[ob_ts[i]]["bid"][0])*0.5 for i in range(0,len(ob_ts))]
    ob_m7 = [np.round(data_ob[i_ts]["bid_size"].sum() + data_ob[i_ts]["ask_size"].sum(),6)for i_ts in ob_ts]
    ob_m11_1 =sum(ob_m3)*sum(ob_m7)
    ob_m11 = (sum(ob_m3)*sum(ob_m7))/(sum(ob_m7))
    return ob_m11


 #-- RESUMEN FUNCIÓN ---- #
def resumen_OB(data_ob: dict = None) -> True:
    """
    This function finds 
    
    Parameters
    ----------

    Returns
    -------
    ob_m1 : 
    """
    ob_ts = list(data_ob.keys())
    l_ts = [pd.to_datetime(i_ts) for i_ts in ob_ts]
    ob_m1 = np.median([l_ts[n_ts+1]-l_ts[n_ts] for n_ts in range(0, len(l_ts)-1)]).total_seconds()*1000
    ob_m2 = [data_ob[ob_ts[i]]["ask"][0]- data_ob[ob_ts[i]]["bid"][0] for i in range (0,len(ob_ts))]
    ob_m3= [(data_ob[ob_ts[i]]["ask"][0]+data_ob[ob_ts[i]]["bid"][0])*0.5 for i in range(0,len(ob_ts))]
    ob_m4 = [data_ob[i_ts].shape[0] for i_ts in ob_ts]
    ob_m5 = [np.round(data_ob[i_ts]["bid_size"].sum(),6) for i_ts in ob_ts]
    ob_m6 = [np.round(data_ob[i_ts]["ask_size"].sum(),6) for i_ts in ob_ts]
    ob_m7 = [np.round(data_ob[i_ts]["bid_size"].sum() + data_ob[i_ts]["ask_size"].sum(),6)for i_ts in ob_ts]
    bid_volume = np.sum(ob_m5)
    ask_volume = np.sum(ob_m6)
    ob_m8 = [bid_volume/ (bid_volume + ask_volume)]
    ob_part1 = ob_m5[0] / (ob_m5[0] + ob_m6[0])
    ob_part2 = [data_ob[ob_ts[i]]["ask"][0]- data_ob[ob_ts[i]]["bid"][0] for i in range (0,len(ob_ts))][0]/2
    ob_m9 = np.round(ob_part1*ob_part2,4)
    ob_m3= [(data_ob[ob_ts[i]]["ask"][0]+data_ob[ob_ts[i]]["bid"][0])*0.5 for i in range(0,len(ob_ts))]
    ob_m7 = [np.round(data_ob[i_ts]["bid_size"].sum() + data_ob[i_ts]["ask_size"].sum(),6)for i_ts in ob_ts]
    ob_m11_1 =sum(ob_m3)*sum(ob_m7)
    ob_m11 = (sum(ob_m3)*sum(ob_m7))/(sum(ob_m7))
    resumen = pd.DataFrame({'spread': ob_m2,'midprice': ob_m3,'n_levels': ob_m4,'bid_volume': ob_m5, 'ask_volume': ob_m6, 'total_volume': ob_m7})
    return resumen





# -- (12) OHLCV : Open, High, Low, Close, Volume (Quoted volume) con el mid price -- # (calcularlas para ambas)
#ob_m12A = 
#ob_m12B =
# hint de 12: resample o pd.DataFrame.ohlc

# -- (13) stats: Mediana, varianza, sesgo kurtosis para el ob_m8
# ob_m13 sería una lista con los 4 calculos estadisticos 
# ob_m13 : [mediana, varianza, sesgo, kurtosis]


# -------------------------------------- PUBLIC TRADES ----------------------------------------- #


def f_publictrades_metrics(data_pt:dict)-> dict:
    """
    """

    # resampling period: 1H 
    # for each period
    # Contar la cantidad de trades que ocurren cada hora
    pt_data.index = pd.to_datetime(pt_data['timestamp'])
    n_pt_data = pt_data['side'].resample('240T').count()
    v_pt_data = pt_data['amount'].resample('240T').sum()

    # -- (1) Buy trade Count -- #
    pt_m1 = data_pt[data_pt["side"]=='buy']['side'].resample(t).count()
    # -- (2) Sell trade count -- # 
    pt_m2 = data_pt[data_pt["side"]=='sell']['side'].resample(t).count()
    # -- (3) Total trade count -- #
    pt_m3 = data_pt['side'].resample(t).count() 
    # -- (4) Difference in trade count (Buy - Sell) -- #
    pt_m4 = pt_m1 - pt_m2

    # Quantity of Buy-side, sell-side and Total trades per period
    
    # -- (5) Sell volume -- #

     # pt_m5 = 

    # -- (6) Buy volume -- # 

     # pt_m6 = 

    # -- (7) Total volume  -- #

     # pt_m7 = 

    # -- (8) Difference in volume (Buy - Sell) -- #

     # pt_m8 = 

    # -- (9) OHLC : Open, High, Low, Close, Volume (Traded Volume) con el traded price-- #

     # pt_m9 = 

    """
    # Crear un dataframe con los precios OHLCVV (pista, utilizar resamples y algo más o menos tipo "fill")
    # Cada hora

    # Resample OHLC
    open_rs = ob_ohlc["open"].resample(ts_resample,closed="left",label="left").bfill()
    high_rs = ob_ohlc["high"].resample(ts_resample,closed="left",label="left").max()
    low_rs = ob_ohlc["low"].resample(ts_resample,closed="left",label="left").min()
    close_rs = ob_ohlc["close"].resample(ts_resample,closed="left",label="left").bfill()
    vol_rs = ob_ohlc["volume"].resample(ts_resample,closed="left",label="left").sum()
    ohlc_data = pd.concat([open_rs,high_rs,low_rs,close_rs,vol_rs],axis=1)
    """

    pt_data = pd.read_csv("btcusdt_binance.csv",header=0)
    pt_data.drop('index',inplace=True, axis=1)

    # para OB: # -- (10) stats: Mediana, varianza, sesgo kurtosis para el ob_m8
    # para PT: 
    pass