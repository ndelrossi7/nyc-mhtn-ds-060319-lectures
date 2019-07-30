# Start by importing necessary packages
import pandas as pd
import matplotlib.pyplot as plot
import seaborn as sns
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.tsa.arima_model import ARIMA


# Reading the dataframe
df = pd.read_csv('zillow_data.csv')

# Converting the zipcodes to string after seeing that there are some zipcodes that are less than 5 digits long
df['RegionName'] = df['RegionName'].astype(str)
# filtering to see those that are less than 5 digits long
test = df[(df.RegionName.str.len() < 5)]

# Converting to datetime
def get_datetimes(df, x):
    """Takes in the dataframe (df) and the start column number (x) and returns 
    the column in datetime format
    """
    return pd.to_datetime(df.columns.values[x:], format='%Y-%m')

df.columns.values[7:] = get_datetimes(df, 7)

# Converting the dataset from wide to long format
def melt_data(df):
    """Takes in the dataframe and melts it to arrange the data according to time. 
    Sets the index to the time/date and removes all other unnecessary parameters.
    """
    melted = pd.melt(df, id_vars=['RegionID', 'RegionName', 'City', 'State', 'Metro', 'CountyName', 'SizeRank'], var_name='time')
    melted['time'] = pd.to_datetime(melted['time'], infer_datetime_format=True)
    melted = melted.dropna(subset=['value'])
    return melted.groupby('time').aggregate({'value':'mean'})
long_df = melt_data(df)

# melting dataframe for easier access for data analysis
# def melt_eda(df):
#     melted = pd.melt(df, id_vars=['RegionID', 'RegionName', 'City', 'State', 'Metro', 'CountyName', 'SizeRank'], var_name='time')
#     melted['time'] = pd.to_datetime(melted['time'], infer_datetime_format=True)
#     melted = melted.dropna(subset=['value'])
#     return melted
# eda = melt_eda(df)

def dfuller(df, param):
    """Takes in the dataframe and parameter of interest and outputs the the 
    Dicky Fuller test results: test statistic, p-value, number of lags, 
    number of observations
    """
    dfuller = adfuller(df[param][1:-1])
    dfoutput = pd.Series(dfuller[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    return dfoutput

def difference(df, old_param, new_name):
    """Takes in the dataframe, parameter, and new name that you wish to create and 
    outputs a dataframe with the difference
    """
    diff = df.diff().fillna(df).rename(index = str, columns = {old_param: new_name})
    return diff

def acf(df, alpha):
    """Takes in the dataframe and an alpha value and outputs the relevant 
    autocorrelation plot
    """
    return plot_acf(df[:-1], alpha = alpha)

def pacf(df, alpha, lags):
    """Takes in the dataframe, alpha value, and number of lags and outputs 
    the relevant partial autocorrelation plot
    """
    return plot_pacf(df[:-1], alpha = alpha, lags = lags)

def ARIMA(df, order):
    """Takes in the dataframe and (pdq) order and outputs the relevant 
    ARIMA summary
    """
    model = ARIMA(df[:-1], order = order)
    model_fit = model.fit(disp=0)
    return model_fit.summary()
# see above -- keeps hitting the recursion limit?

