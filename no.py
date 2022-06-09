
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: functions.py : python script with general functions                                         -- #
# -- author: IvetteLandaverde                                                                      -- #
# -- license: THE LICENSE TYPE AS STATED IN THE REPOSITORY                                               -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""
import numpy as np
import pandas as pd
import data as dt

# Read input data
data_ob=dt.ob_data

def f_descriptive_ob(data_ob:dict)-> dict:
    """
    """

    pass




# -- OrderBook, Imbalance (v:volume, d:depth)
# v[0] Bid volume, v[1] Ask Volume

obimb = lambda v, d: np.sum(v[0][:d])/np.sum([v[0][:d],v[1][:d]])
#obimb(v=data_1,d=10)

























# -- (1) Median Time of orderBook update -- #
ob_ts = list(data.ob.keys())
l_ts = [pd.to_datetime(i_ts) for i_ts in ob_ts]
ob_m1 = np.median([l_ts[n_ts+1]-l_ts[n_ts] for n_ts in range(0, len(l_ts)-1)]).total_seconds()*1000

# -- (2) Spread -- #
ob_m2 = [data_ob[ob_ts[i]]["ask"][0]- data_ob[ob_ts[i]]["bid"][0] for i in range (0,len(ob_ts))]

# -- (3) Midprice -- #
ob_m3= [(data_ob[ob_ts[i]]["ask"][0]+data_ob[ob_ts[i]]["bid"][0])*0.5 for i in range(0,len(ob_ts))]

# -- (4) No. Price Levels --#
ob_m4 = [data_ob[i_ts].shape[0] for i_ts in ob_ts]

# -- (5) Bid Volume --#
ob_m5 = [np.round(data_ob[i_ts]["bid_size"].sum(),6) for i_ts in ob_ts]

# -- (6) Ask Volume -- #
ob_m6 = [np.round(data_ob[i_ts]["ask_size"].sum(),6) for i_ts in ob_ts]

# -- (7) Total Volume -- #
ob_m7 = [np.round(data_ob[i_ts]["bid_size"].sum() + data_ob["i_ts"]["ask_size"].sum(),6)for i_ts in ob_ts]


# -- (8) Volume Imbalance -- #

# pista de la 8: ob_m8 = [bid_volume / (bid_volume + ask_volume)]

# -- (9) Weighted Midprice (A)-- TOB #

# W-MidPrice(A) = OrderBook Imbalance * MidPrice
# W-MidPrice(A) = [bid_volume[0] / (bid_volume[0] + ask_volume[0])] * (bid_price[0] + ask_price[0])/2

# -- (10) Weighted Midprice (B) PUNTOS EXTRA ESTA PARTE -- #

# W-MidPrice(B) = [ask_volume / total_volume]*bid_price + [bid_volume/(total_volume)]*ask_price
# W-MidPrice(B) = (v[1]/np.sum(v[0] + v[1]))*p[0] + (v[0]/np.sum(v[0] + v[1]))*p[1]

# -- (11) Volume-Weighted Average Price -- #

#  VWAP

# -- (12) OHLCV : Open, High, Low, Close, Volume (Quoted volume) con el mid price -- # (calcularlas para ambas)

# hint de 12: resample o pd.DataFrame.ohlc

# -- (13) stats: Mediana, varianza, sesgo kurtosis para el ob_m8
# ob_m13 sería una lista con los 4 calculos estadisticos 
# ob_m13 : [mediana, varianza, sesgo, kurtosis]



r_data = {'median_ts_ob':ob_m1,'spread': ob_m2,'midprice': ob_m3,'n_levels': ob_m4,'bid_volume': ob_m5, 'ask_volume': ob_m6, 'total_volume': ob_m7}


return r_data

# ========= Public trades metrics ==== #
# ========= Public trades metrics ==== #

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

    # pt_m1 = 

    # -- (2) Sell trade count -- # 

    # pt_m2 = 

    # -- (3) Total trade count -- #

     # pt_m3 = 

    # -- (4) Difference in trade count (Buy - Sell) -- #

     # pt_m4 = 

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



