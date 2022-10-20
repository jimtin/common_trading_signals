import json
import os
import mt5_interface
import generic_ema
import ema_golden_cross


# Set up the import filepath
import_filepath = "settings.json"


# Function to import settings from settings.json
def get_project_settings(importFilepath):
    # Test the filepath to sure it exists
    if os.path.exists(importFilepath):
        # Open the file
        f = open(importFilepath, "r")
        # Get the information from file
        project_settings = json.load(f)
        # Close the file
        f.close()
        # Return project settings to program
        return project_settings
    else:
        return ImportError


# Main function
if __name__ == '__main__':
    # Import project settings
    project_settings = get_project_settings(import_filepath)
    # Start MT5
    mt5_interface.start_mt5(project_settings["username"], project_settings["password"], project_settings["server"],
                            project_settings["mt5Pathway"])
    mt5_interface.initialize_symbols(project_settings['symbols'])

    # Queries
    #ema = generic_ema.calc_generic_ema(symbol=project_settings['symbols'][0], timeframe="D1", ema_size=15, num_rows=1000)
    ema = ema_golden_cross.ema_golden_cross(symbol=project_settings['symbols'][0])
    print(ema)
