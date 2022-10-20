import generic_death_cross


# Function to calculate a Death Cross event
def calc_sma_death_cross(symbol):
    return generic_death_cross.generic_sma_death_cross_calculator(symbol=symbol, timeframe="D1")
