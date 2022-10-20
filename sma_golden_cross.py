import generic_golden_cross

# Function to calculate a 'classic' Golden Cross
def calc_sma_golden_cross(symbol):
    return generic_golden_cross.generic_sma_golden_cross_calculator(symbol=symbol, timeframe="D1")