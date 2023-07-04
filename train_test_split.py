import pandas as pd

all_data = pd.read_csv("data/CA_daily_renewables.csv")
all_data["DATETIME"] = pd.to_datetime(all_data["DATETIME"])

test_cutoff = pd.Timestamp(year=2021, month=5, day=1)

train = all_data[all_data["DATETIME"] < test_cutoff]
test = all_data[all_data["DATETIME"] >= test_cutoff]

train.to_csv("data/train.csv", index=False)
test.to_csv("data/test.csv", index=False)
