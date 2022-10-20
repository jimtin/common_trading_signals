import generic_ema
import pandas


# Function to calculate a generic Cross of Death
def generic_ema_death_cross(symbol, timeframe):
    # Retrieve the 15 candle EMA
    ema_15 = generic_ema.calc_generic_ema_with_dataframe(symbol=symbol, timeframe=timeframe, ema_size=15, num_rows=1000)
    # Retrieve the 50 candle EMA
    ema_50 = generic_ema.calc_generic_ema_with_dataframe(symbol=symbol, timeframe=timeframe, ema_size=50, num_rows=1000)
    # Extract the previous values. Number_of_rows - 2 for both EMA 15 and EMA 50
    prev_15 = ema_15.loc[998, 'close']
    prev_50 = ema_50.loc[998, 'close']
    # Extract the current values. Number_of_rows - 1 for EMA 15 and EMA 50
    curr_15 = ema_15.loc[999, 'close']
    curr_50 = ema_50.loc[999, 'close']
    # Compare
    if prev_15 > prev_50 and curr_15 < curr_50:
        return True
    return False


# Calculate a 'classic' cross of death event
def ema_death_cross(symbol):
    return generic_ema_death_cross(symbol=symbol, timeframe="D1")