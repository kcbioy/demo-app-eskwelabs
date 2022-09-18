import pandas as pd

def load_data():
    # Load the data
    data = pd.read_csv(
        "data/micro_world.csv"
    )
    return data