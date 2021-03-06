import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

'''
Test file to explore functionality to read and group data in an excel sheet. raw_data_testing_Geology_strips is the file that
actually analyzes the power strip data.
'''

excel_file = 'D:\School_class_folders\Capstone\Data\Geology Meter Power Strips.xlsx'

data = pd.read_excel(excel_file, sheet_name='Pre Power Strips', header=20)

data["* Start"] = pd.to_datetime(data["* Start"], infer_datetime_format=True, exact=False, errors='coerce').dt.date
#data["Start"] = pd.to_timedelta(data["Start"], errors='ignore')

#data["Total Time"] = dt.datetime.combine()

watSum = data.groupby(['* Start']).sum()
watData = data.groupby(['* Start', 'Start']).sum()

watDataPrint = watData.loc[:, ['kWh/5min']]

watSumPrint = watSum.loc[:, ['kWh/5min']]

#data.set_index("* Start")

print(watSumPrint)
print(watDataPrint)