import tkinter
from tkinter import filedialog
import pandas as pd

from helpers.functions import *

def main():
    path = read_path()
    data = pd.read_csv(path, sep="\t", skiprows=5, skipfooter=2, engine='python')
    data.set_index('Name', inplace=True)
    data = data[data.columns.drop(list(data.filter(regex='Name')))]
    data_types = retrieve_types_from_cols(data)
    _, data_with_types = split_dataframe(data, 19)
    
    json_response = prepare_json(data_with_types.astype(data_types),
                                read_date_time(path),
                                path)
    df_response = apply_types(df = data, types = data_types, start_index=19)
    print(json_response)
    print(df_response)

if __name__ == "__main__":
    main()
