import mt5_interface
import pandas


# Function to calculate a death cross event from Moving Averages
def generic_sma_death_cross_calculator(symbol, timeframe):
    # Retrieve 201 rows of timeframe data
    raw_data = mt5_interface.query_historic_data(symbol=symbol, timeframe=timeframe, number_of_candles=201)
    #### Split into required time periods
    # Convert raw data into Dataframe
    dataframe = pandas.DataFrame(raw_data)

    # Get the previous SMA 50
    prev_50_data = dataframe.iloc[-51:-1]
    # Calculate the mean
    prev_50 = prev_50_data['close'].mean()
    # Get the current SMA 50
    curr_50_data = dataframe.iloc[-50:]
    # Calculate the mean
    curr_50 = curr_50_data['close'].mean()

    # Get the previous SMA 200
    prev_200_data = dataframe.iloc[-201:-1]
    # Calculate the mean
    prev_200 = prev_200_data['close'].mean()
    # Get the current SMA 200
    curr_200_data = dataframe.iloc[-200:]
    # Calculate the mean
    curr_200 = curr_200_data['close'].mean()

    # Compare to see if a Cross of Death has occurred
    if prev_50 > prev_200 and curr_50 < curr_200:
        return True
    return False
