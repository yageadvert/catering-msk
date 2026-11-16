import pandas as pd

def show_missing_values(data):
    missing=pd.DataFrame({
        'missing_count': data.isna().sum(),
        'missing_percent': (
            data.isna().sum() /
            data.shape[0]*100
        ).map(lambda value: f'{value:.1f}%')
    })
    display(missing)