"""
from the raw downloaded files, extract hourly data for the different types of renewables.
"""
import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta

raw_dir = Path("data/CA_daily_renewables")

daily_data = []
for file in sorted(raw_dir.glob("*.txt")):
    try:
        hourly_data = pd.read_csv(
            file,
            delim_whitespace=True, skiprows=2, nrows=24,
            names=["HOUR", "GEOTHERMAL", "BIOMASS", "BIOGAS", "SMALL HYDRO", "WIND TOTAL", "SOLAR PV", "SOLAR THERMAL"],
        )
        date = datetime.strptime(file.name.split("_")[0], "%Y%m%d")
        hourly_data["HOUR"] = [date + timedelta(hours=hour-1) for hour in hourly_data["HOUR"]]
        hourly_data = hourly_data.rename(columns={"HOUR":"DATETIME"})
        daily_data.append(hourly_data)
    except pd.errors.ParserError:  # malformed file caused by insufficient data to calculate hourly information
        print(f"Couldn't parse file {file}")
    
all_data = pd.concat(daily_data, ignore_index=True)
all_data.to_csv("data/CA_daily_renewables.csv", index=False)
