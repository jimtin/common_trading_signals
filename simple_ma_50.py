import generic_sma


# Function to calculate a 50-day SMA
def calc_50_sma(symbol):
    return generic_sma.generic_sma_calculator(symbol=symbol, timeframe="D1", num_candles=50)
