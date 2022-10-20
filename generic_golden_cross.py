import mt5_interface
import pandas


# Function to calculate a death cross event from Moving Averages
def generic_sma_golden_cross_calculator(symbol, timeframe):
    # Retrieve 51 rows of timeframe data
    raw_data = mt5_interface.query_historic_data(symbol=symbol, timeframe=timeframe, number_of_candles=51)
    # Convert raw data into Dataframe
    dataframe = pandas.DataFrame(raw_data)

    #### Split into required time periods
    # Get the previous SMA 15
    prev_15_data = dataframe.iloc[-16:-1]
    # Calculate the mean
    prev_15 = prev_15_data['close'].mean()
    # Get the current SMA 15
    curr_15_data = dataframe.iloc[-15:]
    # Calculate the mean
    curr_15 = curr_15_data['close'].mean()

    # Get the previous SMA 50
    prev_50_data = dataframe.iloc[-51:-1]
    # Calculate the mean
    prev_50 = prev_50_data['close'].mean()
    # Get the current SMA 50
    curr_50_data = dataframe.iloc[-50:]
    # Calculate the mean
    curr_50 = curr_50_data['close'].mean()

    # Compare to see if a Cross of Death has occurred
    if prev_15 < prev_50 and curr_15 > curr_50:
        return True
    return False
