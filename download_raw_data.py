"""
download some daily electricity output data from california

"""
from datetime import datetime, timedelta
from urllib.error import HTTPError
from tqdm import tqdm
import wget
from pathlib import Path

start_date = datetime(year=2018, month=6, day=1)
end_date = datetime(year=2021, month=5, day=31)

out_path = Path("data/CA_daily_renewables")
skipped_dates = []
date = start_date
with tqdm(total=(end_date-start_date).days) as pbar:
    while date <= end_date:
        url = f"https://content.caiso.com/green/renewrpt/{date:%Y%m%d}_DailyRenewablesWatch.txt"
        try:
            wget.download(url, out=str(out_path))
        except HTTPError:
            print(f"Download failed for date {date:%Y%m%d}.")
        date += timedelta(days=1)
        pbar.update()

print("Complete.")
