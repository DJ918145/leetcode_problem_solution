import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    reshaped_report = report.melt(id_vars=['product'],var_name='quarter', value_name='sales')
    return reshaped_report
