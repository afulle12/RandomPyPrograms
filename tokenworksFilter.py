from datetime import datetime
import pandas as pd
import os

monthArr    = ["ERROR", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month       = monthArr[datetime.now().month]
day         = datetime.now().day
filename = input("Enter a filename: ")
output   = "Tokenworks Scans " + str(month) + " " + str(day) + "th.csv" 

f=pd.read_csv(filename)
keep_col = ['AddDate','DeviceName','Age']
new_f = f[keep_col]
new_f.to_csv(output, index=False)
os.remove(filename)