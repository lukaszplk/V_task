import tkinter
from tkinter import filedialog
import pandas as pd
import datetime


def read_path():
    window = tkinter.Tk()
    window.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

def retrieve_types_from_cols(data: pd.DataFrame)->dict:
    result = {}
    for col_name, content in data.items():
        if(content['Data-Type']=='Data-Type'):
            continue
        elif(content['Data-Type']=='INT16'):
            result[col_name] = 'int16'
        elif(content['Data-Type']=='REAL32'):
            result[col_name] = 'float32'
        elif(content['Data-Type']=='REAL64'):
            result[col_name] = 'float64'
        elif(content['Data-Type']=='BIT'):
            result[col_name] = 'bool'
    return result

def apply_types(df: pd.DataFrame, types: dict, start_index: int = 0, end_index: int = None)->pd.DataFrame:
    return pd.concat([df.iloc[:start_index], df.iloc[start_index:].astype(types)])

def split_dataframe(df: pd.DataFrame, index: int)->pd.DataFrame:
    return df.iloc[:index], df.iloc[index:]

def prepare_json(df: pd.DataFrame, date_time: dict, path: str):
    result = {}
    result['path'] = path
    result.update(date_time.copy())
    for key, content in df.items():
        result[key] = content.mean()
    return result

def read_date_time(path: str):
    n_lines = 4
    result = {}
    with open(path,'r') as f:
        for _ in range(n_lines):
            line = f.readline()
            if('start' in line.lower()):
                result['start_date'] = line.split('\t')[-2]
                result['start_time'] = line.split('\t')[-1][:-4]
            elif('end' in line.lower()):
                result['end_date'] = line.split('\t')[-2]
                result['end_time'] = line.split('\t')[-1][:-4]
    return result

if __name__ == "__main__":
    pass
