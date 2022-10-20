import mt5_interface
import pandas


# Define function to calculate an arbitrary EMA
def calc_generic_ema(symbol, timeframe, ema_size, num_rows):
    raw_data = mt5_interface.query_historic_data(symbol=symbol, timeframe=timeframe, number_of_candles=num_rows)
    # Convert into Dataframe
    dataframe = pandas.DataFrame(raw_data)
    # Create column string
    ema_name = "ema_" + str(ema_size)
    # Create the multiplier
    multiplier = 2/(ema_size + 1)
    # Calculate the initial value (SMA)
    # pandas.set_option('display.max_columns', None) # <- use this to show all columns
    # pandas.set_option('display.max_rows', None) # <- use this to show all the rows
    initial_mean = dataframe['close'].head(ema_size).mean()

    # Iterate through Dataframe
    for i in range(len(dataframe)):
        if i == ema_size:
            dataframe.loc[i, ema_name] = initial_mean
        elif i > ema_size:
            ema_value = dataframe.loc[i, 'close'] * multiplier + dataframe.loc[i-1, 'close']*(1-multiplier)
            dataframe.loc[i, ema_name] = ema_value
        else:
            dataframe.loc[i, ema_name] = 0.00
    # print(dataframe) # <- use this to print the dataframe if you want to inspect
    return dataframe.loc[num_rows-1, ema_name]


# Define function to calculate an arbitrary EMA and return Dataframe
def calc_generic_ema_with_dataframe(symbol, timeframe, ema_size, num_rows):
    raw_data = mt5_interface.query_historic_data(symbol=symbol, timeframe=timeframe, number_of_candles=num_rows)
    # Convert into Dataframe
    dataframe = pandas.DataFrame(raw_data)
    # Create column string
    ema_name = "ema_" + str(ema_size)
    # Create the multiplier
    multiplier = 2/(ema_size + 1)
    # Calculate the initial value (SMA)
    # pandas.set_option('display.max_columns', None) # <- use this to show all columns
    # pandas.set_option('display.max_rows', None) # <- use this to show all the rows
    initial_mean = dataframe['close'].head(ema_size).mean()

    # Iterate through Dataframe
    for i in range(len(dataframe)):
        if i == ema_size:
            dataframe.loc[i, ema_name] = initial_mean
        elif i > ema_size:
            ema_value = dataframe.loc[i, 'close'] * multiplier + dataframe.loc[i-1, 'close']*(1-multiplier)
            dataframe.loc[i, ema_name] = ema_value
        else:
            dataframe.loc[i, ema_name] = 0.00
    # print(dataframe) # <- use this to print the dataframe if you want to inspect
    return dataframe
