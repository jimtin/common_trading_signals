import generic_ema


# Function to calculate 50-day EMA. Precision set to 1000 rows
def calc_ema_50(symbol):
    return generic_ema.calc_generic_ema(symbol=symbol, timeframe="D1", ema_size=15, num_rows=1000)