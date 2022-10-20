import mt5_interface
import pandas


# Function to search for a defined number of candles across a specified timeframe.
def generic_sma_calculator(symbol, timeframe, num_candles):
    # Retrieve the raw data from MT 5
    raw_data = mt5_interface.query_historic_data(symbol=symbol, timeframe=timeframe, number_of_candles=num_candles)
    # Convert the raw data into a Pandas Dataframe
    sma_data = pandas.DataFrame(raw_data)
    # Calculate the mean of rows
    sma = sma_data['close'].mean()
    # Return the mean
    return sma
