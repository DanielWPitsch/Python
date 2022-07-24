import pandas as pd
file_name = "binary.csv"

def retornaArq(file):
    df = pd.read_csv(file)
    return df.describe()
    
retornaArq(file_name)  