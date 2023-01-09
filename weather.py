import pandas as pds

file =("data/weather.xlsx")
df = pds.read_excel(file, engine='openpyxl')

def temp(State):
    filt=(df['States']==State)
    a=df.loc[filt,"Rain"]
    b=df.loc[filt,"Temp"]
    c=df.loc[filt,"Humidity"]
    return [[r for r in a],[a for a in b],[s for s in c]]